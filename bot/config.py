"""Bot configuration and constants."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Bot configuration
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
CACHE_TTL = int(os.getenv('CACHE_TTL', '86400'))  # Default: 24 hours

# Validate required configuration
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is required")

# Horoscope API configuration
HOROSCOPE_API_URL = "https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily"
