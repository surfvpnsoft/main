"""Horoscope callback query handler."""
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

from bot.services.horoscope_api import HoroscopeService
from bot.utils.zodiac import get_zodiac_info
from bot.keyboards.zodiac_keyboard import get_zodiac_keyboard

logger = logging.getLogger(__name__)

# Initialize horoscope service
horoscope_service = HoroscopeService()


async def horoscope_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle zodiac sign selection callback.
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    query = update.callback_query
    await query.answer()
    
    # Extract zodiac sign from callback data
    callback_data = query.data
    if not callback_data.startswith('zodiac:'):
        logger.warning(f"Invalid callback data: {callback_data}")
        return
    
    sign = callback_data.split(':', 1)[1]
    logger.info(f"User {query.from_user.id} requested horoscope for {sign}")
    
    # Get zodiac info
    zodiac_info = get_zodiac_info(sign)
    if not zodiac_info:
        await query.edit_message_text("Ошибка: неизвестный знак зодиака")
        return
    
    # Show loading message
    loading_message = f"Получаю гороскоп для {zodiac_info['emoji']} {zodiac_info['ru']}..."
    await query.edit_message_text(loading_message)
    
    # Fetch horoscope
    horoscope_text = await horoscope_service.get_horoscope(sign)
    
    if horoscope_text:
        # Format the horoscope message
        today = datetime.now().strftime("%d.%m.%Y")
        message = (
            f"{zodiac_info['emoji']} {zodiac_info['ru']} {zodiac_info['emoji']}\n"
            f"📅 {today}\n\n"
            f"{horoscope_text}\n\n"
            f"━━━━━━━━━━━━━━━\n"
            f"🔮 Узнать гороскоп другого знака: /horoscope"
        )
        
        await query.edit_message_text(message)
    else:
        # Show error message
        error_message = (
            "😔 Извините, не удалось получить гороскоп.\n"
            "Пожалуйста, попробуйте позже."
        )
        await query.edit_message_text(
            error_message,
            reply_markup=get_zodiac_keyboard()
        )
