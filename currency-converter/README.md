# Currency Converter 💱

Real-time currency converter with beautiful GUI supporting 150+ currencies.

## Features
- 💱 **Real-Time Rates** - Live exchange rates from API
- 🌍 **150+ Currencies** - Support for major world currencies
- 💾 **Smart Caching** - Offline mode with 6-hour cache
- 🔄 **Quick Swap** - Easily swap between currencies
- 📜 **Conversion History** - Track past conversions
- ⚡ **Quick Convert** - See popular currency rates at a glance
- 🎨 **Beautiful GUI** - Modern, user-friendly interface
- 📊 **Exchange Rate Display** - Shows current rate for transparency

## Requirements
```bash
pip install requests
```

## Usage
```bash
python currency_converter.py
```

## How to Use

1. **Enter Amount** - Type the amount you want to convert
2. **Select From Currency** - Choose source currency from dropdown
3. **Select To Currency** - Choose target currency
4. **Click Convert** - See the result instantly!

### Quick Swap
Click the **⇅** button to quickly swap between currencies.

### Refresh Rates
Click **🔃 Refresh Rates** to fetch the latest exchange rates.

### View History
Click **📜 History** to see your last 50 conversions.

## Supported Currency Examples
- 🇺🇸 USD - US Dollar
- 🇪🇺 EUR - Euro
- 🇬🇧 GBP - British Pound
- 🇯🇵 JPY - Japanese Yen
- 🇮🇳 INR - Indian Rupee
- 🇨🇦 CAD - Canadian Dollar
- 🇦🇺 AUD - Australian Dollar
- 🇨🇭 CHF - Swiss Franc
- 🇨🇳 CNY - Chinese Yuan
- 🇲🇽 MXN - Mexican Peso
- ...and 140+ more!

## Features in Detail

### Real-Time Exchange Rates
- Fetches live rates from ExchangeRate-API
- No API key required
- Updates automatically

### Smart Caching
- Caches rates for 6 hours
- Works offline with cached data
- Shows last update time
- Reduces API calls

### Quick Convert Panel
Shows live conversion rates for 1 USD to popular currencies:
- EUR, GBP, JPY, AUD, INR

### Conversion History
- Stores last 50 conversions
- Shows timestamp for each conversion
- Displays amount, currencies, and exchange rate
- Persistent across sessions

## Example Conversion
```
Amount: 100.00
From: USD 🇺🇸
To: EUR 🇪🇺

Result: 100.00 USD = 92.15 EUR
Exchange Rate: 1 USD = 0.9215 EUR
```

## API Information
This app uses the free ExchangeRate-API (https://exchangerate-api.com/)
- No API key required for basic usage
- 1,500 requests per month (free tier)
- Rates updated daily

## Files Created
- `exchange_rates_cache.json` - Cached exchange rates
- `conversion_history.json` - Your conversion history

## Offline Mode
The app works offline using cached exchange rates if:
- You've used it before (cache exists)
- Cache is less than 6 hours old
- Internet connection is unavailable

## Tips
- 💡 Use swap button for quick currency reversal
- 🔄 Refresh rates daily for accuracy
- 📊 Check history to track exchange rate trends
- 💾 App works offline with cached rates
- 🎯 Use quick convert panel for common currencies

## Error Handling
- ✅ Validates numeric input
- ✅ Handles API failures gracefully
- ✅ Falls back to cached rates
- ✅ Clear error messages
- ✅ Prevents invalid conversions

## Use Cases
- 💼 Business currency conversions
- ✈️ Travel planning
- 🛒 International shopping
- 💰 Investment tracking
- 📈 Exchange rate monitoring
