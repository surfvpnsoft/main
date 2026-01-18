"""Start and help command handlers."""
import logging
from telegram import Update
from telegram.ext import ContextTypes

from bot.keyboards.zodiac_keyboard import get_zodiac_keyboard

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user = update.effective_user
    logger.info(f"User {user.id} ({user.username}) started the bot")
    
    welcome_message = (
        "🌟 Добро пожаловать в Бот Гороскопов! 🌟\n\n"
        "Я помогу узнать ваш ежедневный гороскоп.\n\n"
        "Выберите ваш знак зодиака ниже:"
    )
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=get_zodiac_keyboard()
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    help_message = (
        "🔮 Бот Гороскопов - Справка\n\n"
        "Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/horoscope - Выбрать знак зодиака\n"
        "/help - Показать эту справку\n\n"
        "Просто выберите свой знак зодиака, и я расскажу вам ваш гороскоп на сегодня! ✨"
    )
    
    await update.message.reply_text(help_message)


async def horoscope_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /horoscope command.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    message = "Выберите ваш знак зодиака:"
    
    await update.message.reply_text(
        message,
        reply_markup=get_zodiac_keyboard()
    )
