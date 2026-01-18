"""Zodiac sign data and utilities."""

ZODIAC_SIGNS = {
    'aries': {'emoji': '♈', 'ru': 'Овен', 'dates': '21 марта - 19 апреля'},
    'taurus': {'emoji': '♉', 'ru': 'Телец', 'dates': '20 апреля - 20 мая'},
    'gemini': {'emoji': '♊', 'ru': 'Близнецы', 'dates': '21 мая - 20 июня'},
    'cancer': {'emoji': '♋', 'ru': 'Рак', 'dates': '21 июня - 22 июля'},
    'leo': {'emoji': '♌', 'ru': 'Лев', 'dates': '23 июля - 22 августа'},
    'virgo': {'emoji': '♍', 'ru': 'Дева', 'dates': '23 августа - 22 сентября'},
    'libra': {'emoji': '♎', 'ru': 'Весы', 'dates': '23 сентября - 22 октября'},
    'scorpio': {'emoji': '♏', 'ru': 'Скорпион', 'dates': '23 октября - 21 ноября'},
    'sagittarius': {'emoji': '♐', 'ru': 'Стрелец', 'dates': '22 ноября - 21 декабря'},
    'capricorn': {'emoji': '♑', 'ru': 'Козерог', 'dates': '22 декабря - 19 января'},
    'aquarius': {'emoji': '♒', 'ru': 'Водолей', 'dates': '20 января - 18 февраля'},
    'pisces': {'emoji': '♓', 'ru': 'Рыбы', 'dates': '19 февраля - 20 марта'},
}


def get_zodiac_info(sign: str) -> dict:
    """Get information about a zodiac sign.
    
    Args:
        sign: Zodiac sign name in English (lowercase)
        
    Returns:
        Dictionary with zodiac sign information
    """
    return ZODIAC_SIGNS.get(sign.lower(), {})


def get_all_signs() -> list:
    """Get list of all zodiac sign names.
    
    Returns:
        List of zodiac sign names in English
    """
    return list(ZODIAC_SIGNS.keys())
