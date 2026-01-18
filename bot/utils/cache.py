"""Simple in-memory caching for horoscope data."""
from datetime import datetime, timedelta
from typing import Optional, Any


class HoroscopeCache:
    """Simple cache for horoscope data with TTL support."""
    
    def __init__(self, ttl_seconds: int = 86400):
        """Initialize cache with TTL in seconds.
        
        Args:
            ttl_seconds: Time to live for cache entries (default: 24 hours)
        """
        self._cache = {}
        self._ttl = ttl_seconds
    
    def _get_cache_key(self, sign: str, date: str) -> str:
        """Generate cache key for a sign and date.
        
        Args:
            sign: Zodiac sign name
            date: Date string
            
        Returns:
            Cache key string
        """
        return f"{sign}:{date}"
    
    def get(self, sign: str, date: str = None) -> Optional[str]:
        """Get horoscope from cache.
        
        Args:
            sign: Zodiac sign name
            date: Date string (default: today)
            
        Returns:
            Cached horoscope text or None if not found/expired
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        key = self._get_cache_key(sign, date)
        entry = self._cache.get(key)
        
        if entry is None:
            return None
        
        # Check if cache entry is expired
        if datetime.now() > entry['expires_at']:
            del self._cache[key]
            return None
        
        return entry['data']
    
    def set(self, sign: str, data: str, date: str = None) -> None:
        """Store horoscope in cache.
        
        Args:
            sign: Zodiac sign name
            data: Horoscope text to cache
            date: Date string (default: today)
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        key = self._get_cache_key(sign, date)
        expires_at = datetime.now() + timedelta(seconds=self._ttl)
        
        self._cache[key] = {
            'data': data,
            'expires_at': expires_at
        }
    
    def clear(self) -> None:
        """Clear all cache entries."""
        self._cache.clear()
    
    def cleanup_expired(self) -> None:
        """Remove expired entries from cache."""
        now = datetime.now()
        expired_keys = [
            key for key, entry in self._cache.items()
            if now > entry['expires_at']
        ]
        for key in expired_keys:
            del self._cache[key]
