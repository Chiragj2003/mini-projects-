"""
Expense Tracker - Track daily expenses with charts
Features:
- Add expenses with category and amount
- View all expenses
- Filter by date range or category
- Calculate total spending
- Visualize expenses with charts (pie chart by category, line chart over time)
- Export data to CSV
- Monthly/yearly summaries
"""

import json
import os
from datetime import datetime, timedelta
import csv

try:
    import matplotlib.pyplot as plt
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False
    print("Note: matplotlib not installed. Charts will not be available.")
    print("Install with: pip install matplotlib")

class ExpenseTracker:
    def __init__(self):
        self.data_file = "expenses.json"
        self.categories = [
            "Food & Dining",
            "Transportation",
            "Shopping",
            "Entertainment",
            "Bills & Utilities",
            "Healthcare",
            "Education",
            "Travel",
            "Other"
        ]
    
    def load_expenses(self):
        """Load expenses from file"""
        if not os.path.exists(self.data_file):
            return []
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    
    def save_expenses(self, expenses):
        """Save expenses to file"""
        with open(self.data_file, 'w') as f:
            json.dump(expenses, f, indent=4)
    
    def add_expense(self):
        """Add a new expense"""
        print("\n" + "="*50)
        print("ADD NEW EXPENSE".center(50))
        print("="*50)
        
        # Get expense details
        description = input("Description: ").strip()
        
        # Select category
        print("\nCategories:")
        for idx, cat in enumerate(self.categories, 1):
            print(f"{idx}. {cat}")
        
        while True:
            try:
                cat_choice = int(input("\nSelect category (1-9): "))
                if 1 <= cat_choice <= len(self.categories):
                    category = self.categories[cat_choice - 1]
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")
        
        # Get amount
        while True:
            try:
                amount = float(input("Amount ($): "))
                if amount > 0:
                    break
                else:
                    print("Amount must be positive.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Get date
        date_input = input("Date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            try:
                date_obj = datetime.strptime(date_input, "%Y-%m-%d")
                date = date_obj.strftime("%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.now().strftime("%Y-%m-%d")
        else:
            date = datetime.now().strftime("%Y-%m-%d")
        
        # Create expense entry
        expense = {
            'id': datetime.now().timestamp(),
            'date': date,
            'description': description,
            'category': category,
            'amount': amount
        }
        
        # Save expense
        expenses = self.load_expenses()
        expenses.append(expense)
        self.save_expenses(expenses)
        
        print(f"\n✓ Expense added successfully! (${amount:.2f} for {category})")
    
    def view_expenses(self):
        """View all expenses"""
        expenses = self.load_expenses()
        
        if not expenses:
            print("\n✗ No expenses recorded yet.")
            return
        
        print("\n" + "="*90)
        print("ALL EXPENSES".center(90))
        print("="*90)
        print(f"{'Date':<12} {'Description':<25} {'Category':<20} {'Amount':>10}")
        print("-"*90)
        
        total = 0
        for expense in sorted(expenses, key=lambda x: x['date'], reverse=True):
            print(f"{expense['date']:<12} {expense['description'][:24]:<25} "
                  f"{expense['category']:<20} ${expense['amount']:>9.2f}")
            total += expense['amount']
        
        print("-"*90)
        print(f"{'TOTAL':<57} ${total:>9.2f}")
        print("="*90)
    
    def filter_by_category(self):
        """Filter expenses by category"""
        print("\n=== Filter by Category ===")
        print("\nCategories:")
        for idx, cat in enumerate(self.categories, 1):
            print(f"{idx}. {cat}")
        
        try:
            cat_choice = int(input("\nSelect category (1-9): "))
            if 1 <= cat_choice <= len(self.categories):
                category = self.categories[cat_choice - 1]
            else:
                print("Invalid choice.")
                return
        except ValueError:
            print("Invalid input.")
            return
        
        expenses = self.load_expenses()
        filtered = [e for e in expenses if e['category'] == category]
        
        if not filtered:
            print(f"\n✗ No expenses found for category: {category}")
            return
        
        print("\n" + "="*90)
        print(f"EXPENSES - {category.upper()}".center(90))
        print("="*90)
        print(f"{'Date':<12} {'Description':<40} {'Amount':>10}")
        print("-"*90)
        
        total = 0
        for expense in sorted(filtered, key=lambda x: x['date'], reverse=True):
            print(f"{expense['date']:<12} {expense['description'][:39]:<40} ${expense['amount']:>9.2f}")
            total += expense['amount']
        
        print("-"*90)
        print(f"{'TOTAL':<52} ${total:>9.2f}")
        print("="*90)
    
    def monthly_summary(self):
        """Show monthly summary"""
        print("\n=== Monthly Summary ===")
        month_input = input("Enter month (YYYY-MM) or press Enter for current month: ").strip()
        
        if month_input:
            try:
                datetime.strptime(month_input, "%Y-%m")
                target_month = month_input
            except ValueError:
                print("Invalid format. Using current month.")
                target_month = datetime.now().strftime("%Y-%m")
        else:
            target_month = datetime.now().strftime("%Y-%m")
        
        expenses = self.load_expenses()
        monthly_expenses = [e for e in expenses if e['date'].startswith(target_month)]
        
        if not monthly_expenses:
            print(f"\n✗ No expenses found for {target_month}")
            return
        
        # Calculate category totals
        category_totals = {}
        for expense in monthly_expenses:
            cat = expense['category']
            category_totals[cat] = category_totals.get(cat, 0) + expense['amount']
        
        total = sum(category_totals.values())
        
        print("\n" + "="*60)
        print(f"SUMMARY FOR {target_month}".center(60))
        print("="*60)
        print(f"{'Category':<30} {'Amount':>15} {'Percentage':>10}")
        print("-"*60)
        
        for cat in sorted(category_totals.keys(), key=lambda x: category_totals[x], reverse=True):
            amount = category_totals[cat]
            percentage = (amount / total) * 100
            print(f"{cat:<30} ${amount:>14.2f} {percentage:>9.1f}%")
        
        print("-"*60)
        print(f"{'TOTAL':<30} ${total:>14.2f}")
        print("="*60)
    
    def visualize_expenses(self):
        """Create charts for expenses"""
        if not MATPLOTLIB_AVAILABLE:
            print("\n✗ matplotlib not installed. Cannot create charts.")
            print("Install with: pip install matplotlib")
            return
        
        expenses = self.load_expenses()
        
        if not expenses:
            print("\n✗ No expenses to visualize.")
            return
        
        print("\n=== Visualize Expenses ===")
        print("1. Pie Chart (by Category)")
        print("2. Line Chart (Over Time)")
        print("3. Bar Chart (Monthly Comparison)")
        
        choice = input("\nSelect chart type (1-3): ").strip()
        
        if choice == '1':
            self._pie_chart(expenses)
        elif choice == '2':
            self._line_chart(expenses)
        elif choice == '3':
            self._bar_chart(expenses)
        else:
            print("Invalid choice.")
    
    def _pie_chart(self, expenses):
        """Create pie chart by category"""
        category_totals = {}
        for expense in expenses:
            cat = expense['category']
            category_totals[cat] = category_totals.get(cat, 0) + expense['amount']
        
        categories = list(category_totals.keys())
        amounts = list(category_totals.values())
        
        plt.figure(figsize=(10, 8))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
        plt.title('Expenses by Category', fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
        print("✓ Chart displayed!")
    
    def _line_chart(self, expenses):
        """Create line chart over time"""
        # Sort by date
        sorted_expenses = sorted(expenses, key=lambda x: x['date'])
        
        # Group by date
        date_totals = {}
        for expense in sorted_expenses:
            date = expense['date']
            date_totals[date] = date_totals.get(date, 0) + expense['amount']
        
        dates = list(date_totals.keys())
        amounts = list(date_totals.values())
        
        plt.figure(figsize=(12, 6))
        plt.plot(dates, amounts, marker='o', linewidth=2, markersize=6)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Amount ($)', fontsize=12)
        plt.title('Expenses Over Time', fontsize=16, fontweight='bold')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        print("✓ Chart displayed!")
    
    def _bar_chart(self, expenses):
        """Create bar chart for monthly comparison"""
        # Group by month
        monthly_totals = {}
        for expense in expenses:
            month = expense['date'][:7]  # YYYY-MM
            monthly_totals[month] = monthly_totals.get(month, 0) + expense['amount']
        
        months = sorted(monthly_totals.keys())
        amounts = [monthly_totals[m] for m in months]
        
        plt.figure(figsize=(12, 6))
        plt.bar(months, amounts, color='skyblue', edgecolor='navy')
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Total Amount ($)', fontsize=12)
        plt.title('Monthly Expenses Comparison', fontsize=16, fontweight='bold')
        plt.xticks(rotation=45)
        plt.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
        print("✓ Chart displayed!")
    
    def export_to_csv(self):
        """Export expenses to CSV"""
        expenses = self.load_expenses()
        
        if not expenses:
            print("\n✗ No expenses to export.")
            return
        
        filename = f"expenses_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['date', 'description', 'category', 'amount']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for expense in sorted(expenses, key=lambda x: x['date']):
                writer.writerow({
                    'date': expense['date'],
                    'description': expense['description'],
                    'category': expense['category'],
                    'amount': expense['amount']
                })
        
        print(f"\n✓ Expenses exported to: {filename}")
    
    def delete_expense(self):
        """Delete an expense"""
        expenses = self.load_expenses()
        
        if not expenses:
            print("\n✗ No expenses to delete.")
            return
        
        print("\n=== Recent Expenses ===")
        recent = sorted(expenses, key=lambda x: x['date'], reverse=True)[:10]
        
        for idx, expense in enumerate(recent, 1):
            print(f"{idx}. {expense['date']} - {expense['description']} "
                  f"({expense['category']}) - ${expense['amount']:.2f}")
        
        try:
            choice = int(input("\nEnter expense number to delete (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(recent):
                expense_to_delete = recent[choice - 1]
                expenses = [e for e in expenses if e['id'] != expense_to_delete['id']]
                self.save_expenses(expenses)
                print(f"✓ Expense deleted successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input.")
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "="*50)
        print("💰 EXPENSE TRACKER 💰".center(50))
        print("="*50)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Monthly Summary")
        print("5. Visualize Expenses (Charts)")
        print("6. Export to CSV")
        print("7. Delete Expense")
        print("8. Exit")
        print("="*50)
    
    def run(self):
        """Main program loop"""
        print("="*50)
        print("💰 EXPENSE TRACKER 💰".center(50))
        print("="*50)
        print("Track your daily expenses and visualize spending!")
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expenses()
            elif choice == '3':
                self.filter_by_category()
            elif choice == '4':
                self.monthly_summary()
            elif choice == '5':
                self.visualize_expenses()
            elif choice == '6':
                self.export_to_csv()
            elif choice == '7':
                self.delete_expense()
            elif choice == '8':
                print("\n👋 Goodbye! Keep tracking your expenses!")
                break
            else:
                print("✗ Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
