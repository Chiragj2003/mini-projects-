# Expense Tracker 💰

Track your daily expenses with detailed reports and beautiful visualizations.

## Features
- 📝 **Add Expenses** - Record expenses with description, category, amount, and date
- 👀 **View All Expenses** - Display all recorded expenses in a table format
- 🔍 **Filter by Category** - View expenses filtered by specific categories
- 📊 **Monthly Summary** - Get detailed monthly expense breakdowns
- 📈 **Visualizations** - Create charts (pie, line, bar) to analyze spending patterns
- 💾 **Export to CSV** - Export your expense data for external analysis
- 🗑️ **Delete Expenses** - Remove incorrect entries
- 🎯 **9 Categories** - Pre-defined categories for easy organization

## Categories
1. Food & Dining
2. Transportation
3. Shopping
4. Entertainment
5. Bills & Utilities
6. Healthcare
7. Education
8. Travel
9. Other

## Requirements
```bash
pip install matplotlib
```

## Usage
```bash
python expense_tracker.py
```

## Features in Detail

### Add Expense
Record new expenses with:
- Description (e.g., "Grocery shopping")
- Category (from predefined list)
- Amount in dollars
- Date (default: today)

### Monthly Summary
- View total spending per category
- See percentage breakdown
- Identify top spending categories

### Visualizations
1. **Pie Chart** - Shows spending distribution by category
2. **Line Chart** - Tracks daily spending over time
3. **Bar Chart** - Compares monthly spending

### Export to CSV
Export all expenses to CSV format with:
- Date, Description, Category, Amount
- Timestamped filename
- Compatible with Excel/Google Sheets

## Example Usage
```
=== ADD NEW EXPENSE ===
Description: Lunch at restaurant
Category: 1 (Food & Dining)
Amount ($): 25.50
Date: 2025-10-15

✓ Expense added successfully! ($25.50 for Food & Dining)
```

## Files Created
- `expenses.json` - Stores all expense data
- `expenses_export_*.csv` - Exported CSV files

## Tips
- 💡 Add expenses daily for accurate tracking
- 📊 Review monthly summaries to identify spending patterns
- 🎯 Use categories consistently for better analysis
- 📈 Check visualizations monthly to spot trends
