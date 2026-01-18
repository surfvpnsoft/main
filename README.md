# Telegram Horoscope Bot 🌟

A Python-based Telegram bot that provides daily horoscope readings for all 12 zodiac signs in Russian language.

## Features

- 🔮 Daily horoscope for all 12 zodiac signs
- 🇷🇺 Russian language interface
- ⚡ Fast response with intelligent caching
- 🎨 User-friendly inline keyboard interface
- 🌐 Automatic translation from English to Russian

## Architecture

The bot uses:
- **python-telegram-bot** for Telegram Bot API integration
- **horoscope-app-api** for horoscope data
- **googletrans** for automatic translation to Russian
- **httpx** for async HTTP requests
- **In-memory caching** to reduce API calls

## Project Structure

```
telegram-horoscope-bot/
├── bot/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── config.py            # Configuration
│   ├── handlers/
│   │   ├── __init__.py
│   │   ├── start.py         # /start and /help handlers
│   │   └── horoscope.py     # Horoscope handlers
│   ├── services/
│   │   ├── __init__.py
│   │   ├── horoscope_api.py # API integration
│   │   └── translator.py    # Translation service
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── cache.py         # Caching utilities
│   │   └── zodiac.py        # Zodiac sign data
│   └── keyboards/
│       ├── __init__.py
│       └── zodiac_keyboard.py # Inline keyboards
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── Dockerfile
```

## Installation

### Prerequisites

- Python 3.10 or higher
- A Telegram Bot Token (get one from [@BotFather](https://t.me/BotFather))

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/surfvpnsoft/main.git
   cd main
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Telegram Bot Token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   LOG_LEVEL=INFO
   CACHE_TTL=86400
   ```

5. **Run the bot**
   ```bash
   python -m bot.main
   ```

## Docker Deployment

### Build and run with Docker

```bash
# Build the image
docker build -t telegram-horoscope-bot .

# Run the container
docker run -d --name horoscope-bot \
  -e TELEGRAM_BOT_TOKEN=your_bot_token_here \
  telegram-horoscope-bot
```

### Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
version: '3.8'
services:
  bot:
    build: .
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - LOG_LEVEL=INFO
      - CACHE_TTL=86400
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

## Usage

1. Start a chat with your bot on Telegram
2. Send `/start` to begin
3. Select your zodiac sign from the inline keyboard
4. Receive your daily horoscope in Russian

### Available Commands

- `/start` - Start the bot and show zodiac sign selection
- `/help` - Show help information
- `/horoscope` - Show zodiac sign selection menu

## Zodiac Signs

The bot supports all 12 zodiac signs:

| Sign | Russian | Emoji | Dates |
|------|---------|-------|-------|
| Aries | Овен | ♈ | 21 марта - 19 апреля |
| Taurus | Телец | ♉ | 20 апреля - 20 мая |
| Gemini | Близнецы | ♊ | 21 мая - 20 июня |
| Cancer | Рак | ♋ | 21 июня - 22 июля |
| Leo | Лев | ♌ | 23 июля - 22 августа |
| Virgo | Дева | ♍ | 23 августа - 22 сентября |
| Libra | Весы | ♎ | 23 сентября - 22 октября |
| Scorpio | Скорпион | ♏ | 23 октября - 21 ноября |
| Sagittarius | Стрелец | ♐ | 22 ноября - 21 декабря |
| Capricorn | Козерог | ♑ | 22 декабря - 19 января |
| Aquarius | Водолей | ♒ | 20 января - 18 февраля |
| Pisces | Рыбы | ♓ | 19 февраля - 20 марта |

## Configuration

Environment variables:

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Bot token from @BotFather | Yes | - |
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | No | INFO |
| `CACHE_TTL` | Cache time-to-live in seconds | No | 86400 |

## Development

### Running Tests

```bash
# Install dev dependencies
pip install pytest pytest-asyncio

# Run tests
pytest
```

### Code Style

The project follows PEP 8 style guidelines. Use `black` and `flake8` for code formatting:

```bash
pip install black flake8
black bot/
flake8 bot/
```

## Troubleshooting

### Bot doesn't respond
- Check that your bot token is correct in `.env`
- Ensure the bot is running (`python -m bot.main`)
- Check the logs for error messages

### Translation issues
- The bot uses Google Translate which may have rate limits
- If translation fails, the original English text will be shown with a note

### API errors
- The horoscope API may occasionally be unavailable
- The bot will show a friendly error message to users
- Cached horoscopes will still be available

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Telegram Bot API wrapper
- [horoscope-app-api](https://horoscope-app-api.vercel.app/) - Horoscope data provider
- [googletrans](https://github.com/ssut/py-googletrans) - Translation library

## Support

For issues and questions, please open an issue on GitHub.

---

Made with ❤️ for astrology enthusiasts
