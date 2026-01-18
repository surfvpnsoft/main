"""Horoscope API integration service."""
import logging
from datetime import datetime
from typing import Optional
import httpx

from bot.config import HOROSCOPE_API_URL, CACHE_TTL
from bot.utils.cache import HoroscopeCache
from bot.services.translator import TranslationService

logger = logging.getLogger(__name__)


class HoroscopeService:
    """Service for fetching and caching horoscopes."""
    
    def __init__(self):
        """Initialize horoscope service."""
        self.cache = HoroscopeCache(ttl_seconds=CACHE_TTL)
        self.translator = TranslationService()
    
    async def get_horoscope(self, sign: str, day: str = "today") -> Optional[str]:
        """Get horoscope for a zodiac sign.
        
        Args:
            sign: Zodiac sign name (e.g., 'aries', 'taurus')
            day: Day for horoscope ('today', 'yesterday', 'tomorrow')
            
        Returns:
            Horoscope text in Russian or None if failed
        """
        # Check cache first
        date_str = datetime.now().strftime("%Y-%m-%d")
        cached = self.cache.get(sign, date_str)
        if cached:
            logger.info(f"Cache hit for {sign} on {date_str}")
            return cached
        
        # Fetch from API
        try:
            horoscope_text = await self._fetch_from_api(sign, day)
            if horoscope_text:
                # Translate to Russian
                translated = await self.translator.translate_to_russian(horoscope_text)
                
                # Cache the result
                self.cache.set(sign, translated, date_str)
                
                return translated
            return None
        except Exception as e:
            logger.error(f"Error fetching horoscope for {sign}: {e}")
            return None
    
    async def _fetch_from_api(self, sign: str, day: str = "today") -> Optional[str]:
        """Fetch horoscope from external API.
        
        Args:
            sign: Zodiac sign name
            day: Day for horoscope
            
        Returns:
            Horoscope text in English or None if failed
        """
        try:
            params = {
                'sign': sign,
                'day': day
            }
            
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(HOROSCOPE_API_URL, params=params)
                response.raise_for_status()
                
                data = response.json()
                
                # Extract horoscope text from response
                # The API returns: {"data": {"date": "...", "horoscope_data": "..."}, "status": 200, "success": true}
                if data.get('success') and 'data' in data:
                    horoscope_data = data['data'].get('horoscope_data', '')
                    return horoscope_data
                
                logger.warning(f"Unexpected API response format: {data}")
                return None
                
        except httpx.HTTPError as e:
            logger.error(f"HTTP error fetching horoscope: {e}")
            return None
        except Exception as e:
            logger.error(f"Error parsing horoscope response: {e}")
            return None
