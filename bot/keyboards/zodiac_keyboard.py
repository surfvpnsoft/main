"""Inline keyboard for zodiac sign selection."""
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.utils.zodiac import ZODIAC_SIGNS


def get_zodiac_keyboard() -> InlineKeyboardMarkup:
    """Create inline keyboard with all zodiac signs.
    
    Returns:
        InlineKeyboardMarkup with zodiac sign buttons
    """
    keyboard = []
    
    # Create buttons in rows of 3
    row = []
    for sign, info in ZODIAC_SIGNS.items():
        button_text = f"{info['emoji']} {info['ru']}"
        callback_data = f"zodiac:{sign}"
        
        row.append(InlineKeyboardButton(button_text, callback_data=callback_data))
        
        # Add row to keyboard when we have 3 buttons
        if len(row) == 3:
            keyboard.append(row)
            row = []
    
    # Add remaining buttons if any
    if row:
        keyboard.append(row)
    
    return InlineKeyboardMarkup(keyboard)
