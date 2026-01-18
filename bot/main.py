"""Main entry point for the Telegram Horoscope Bot."""
import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

from bot.config import TELEGRAM_BOT_TOKEN, LOG_LEVEL
from bot.handlers.start import start_command, help_command, horoscope_command
from bot.handlers.horoscope import horoscope_callback

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, LOG_LEVEL.upper(), logging.INFO)
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    logger.info("Starting Telegram Horoscope Bot...")
    
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("horoscope", horoscope_command))
    
    # Register callback query handler for zodiac sign selection
    application.add_handler(CallbackQueryHandler(horoscope_callback, pattern=r'^zodiac:'))
    
    # Start the bot
    logger.info("Bot is running. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == '__main__':
    main()
