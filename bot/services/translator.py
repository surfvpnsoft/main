"""Translation service for horoscope text."""
import logging
from typing import Optional
from googletrans import Translator

logger = logging.getLogger(__name__)


class TranslationService:
    """Service for translating text to Russian."""
    
    def __init__(self):
        """Initialize translation service."""
        self.translator = Translator()
    
    async def translate_to_russian(self, text: str) -> str:
        """Translate English text to Russian.
        
        Args:
            text: Text to translate
            
        Returns:
            Translated text in Russian, or original text if translation fails
        """
        try:
            # googletrans is synchronous, but we can still use it in async context
            result = self.translator.translate(text, src='en', dest='ru')
            return result.text
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            # Return original text with a note if translation fails
            return f"{text}\n\n(Перевод недоступен)"
