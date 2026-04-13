# 💳 Credit Card Validator

A simple and elegant credit card validation tool built with Python and Streamlit. Validates credit card numbers using the Luhn algorithm and fetches detailed card information including issuer, scheme, type, and country.

## Features

- ✅ **Luhn Algorithm Validation** - Verify credit card number validity
- 🏦 **Card Details Lookup** - Get issuer, scheme, card type, and country information
- 🎨 **Beautiful UI** - Interactive Streamlit dashboard
- 🔒 **Error Handling** - Graceful handling of API failures
- 📝 **Test Cards** - Built-in test card numbers for easy testing

## Prerequisites

- Python 3.8 or higher
- pip or conda package manager

## Environment Setup

1. **Copy the environment template**
   ```bash
   cp .env.example .env
   ```

2. **Get an API key from HandyAPI**
   - Visit [HandyAPI](https://handyapi.com/)
   - Sign up for a free account
   - Get your API key from the dashboard

3. **Update your `.env` file**
   ```bash
   # Edit .env and replace 'your_api_key_here' with your actual API key
   HANDY_API_KEY=your_actual_api_key_here
   ```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/credit_card_check.git
   cd credit_card_check
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Streamlit Dashboard

```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## API Information

This project uses the **HandyAPI BIN Lookup** service to fetch card details:
- **Endpoint**: `https://data.handyapi.com/bin/{bin_number}`
- **API Key**: Required (stored securely in `.env` file)

## Test Cards

| Card Number | Scheme | Status |
|------------|--------|---------|
| `4242 4242 4242 4242` | Visa | Valid |
| `5555 5555 5555 4444` | Mastercard | Valid |
| `6011 1111 1111 1117` | Discover | Valid |
| `3782 822463 10005` | American Express | Valid |

## Validation Method

The validator uses the **Luhn Algorithm**, also known as the "modulus 10" algorithm:

1. Reverse the card number digits
2. Double every second digit
3. Subtract 9 from any doubled value greater than 9
4. Sum all digits
5. If the total modulo 10 equals 0, the card is valid

## Project Structure

```
credit_card_check/
├── streamlit_app.py      # Main Streamlit dashboard
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
├── .env                  # Environment variables (create from .env.example)
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── README.md            # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Security Note

⚠️ **Important**: Never hardcode API keys in production code. Use environment variables instead:

```python
import os

api_key = os.getenv("HANDY_API_KEY")
```

## Disclaimer

This tool is for educational purposes only. Always validate card information through official payment processing channels for production use.

## Support

For issues and questions, please open an issue on GitHub or contact the maintainers.

---

**Made with ❤️ by Jeet Prosad Mandal**
