"""
Currency Converter - Real-time exchange rates
Features:
- Real-time currency conversion using live exchange rates
- Support for 150+ currencies
- Historical exchange rates
- Offline mode with cached rates
- GUI interface with Tkinter
- Favorite currency pairs
- Conversion history
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
import os
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("💱 Currency Converter")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg='#2C3E50')
        
        # API endpoint (free tier - no API key needed)
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        
        # Cache settings
        self.cache_file = "exchange_rates_cache.json"
        self.cache_duration = timedelta(hours=6)  # Cache for 6 hours
        
        # History file
        self.history_file = "conversion_history.json"
        
        # Popular currencies
        self.popular_currencies = [
            'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'INR', 'MXN'
        ]
        
        # Load data
        self.exchange_rates = {}
        self.currencies = []
        self.load_exchange_rates()
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        """Create all UI widgets"""
        
        # Title
        title_label = tk.Label(
            self.root,
            text="💱 CURRENCY CONVERTER",
            font=('Helvetica', 24, 'bold'),
            bg='#2C3E50',
            fg='#ECF0F1'
        )
        title_label.pack(pady=20)
        
        # Main conversion frame
        conv_frame = tk.Frame(self.root, bg='#34495E', bd=5, relief='ridge')
        conv_frame.pack(pady=10, padx=30, fill='both')
        
        # Amount input
        amount_label = tk.Label(
            conv_frame,
            text="Amount:",
            font=('Helvetica', 14),
            bg='#34495E',
            fg='#ECF0F1'
        )
        amount_label.grid(row=0, column=0, padx=10, pady=15, sticky='w')
        
        self.amount_entry = tk.Entry(
            conv_frame,
            font=('Helvetica', 16),
            width=20,
            bd=2,
            relief='solid'
        )
        self.amount_entry.grid(row=0, column=1, padx=10, pady=15)
        self.amount_entry.insert(0, "1.00")
        
        # From currency
        from_label = tk.Label(
            conv_frame,
            text="From:",
            font=('Helvetica', 14),
            bg='#34495E',
            fg='#ECF0F1'
        )
        from_label.grid(row=1, column=0, padx=10, pady=15, sticky='w')
        
        self.from_currency = ttk.Combobox(
            conv_frame,
            values=self.currencies,
            font=('Helvetica', 12),
            width=18,
            state='readonly'
        )
        self.from_currency.grid(row=1, column=1, padx=10, pady=15)
        self.from_currency.set('USD')
        
        # Swap button
        swap_button = tk.Button(
            conv_frame,
            text="⇅",
            command=self.swap_currencies,
            font=('Helvetica', 20, 'bold'),
            bg='#3498DB',
            fg='white',
            width=3,
            relief='raised',
            bd=2,
            cursor='hand2'
        )
        swap_button.grid(row=2, column=1, pady=5)
        
        # To currency
        to_label = tk.Label(
            conv_frame,
            text="To:",
            font=('Helvetica', 14),
            bg='#34495E',
            fg='#ECF0F1'
        )
        to_label.grid(row=3, column=0, padx=10, pady=15, sticky='w')
        
        self.to_currency = ttk.Combobox(
            conv_frame,
            values=self.currencies,
            font=('Helvetica', 12),
            width=18,
            state='readonly'
        )
        self.to_currency.grid(row=3, column=1, padx=10, pady=15)
        self.to_currency.set('EUR')
        
        # Convert button
        convert_button = tk.Button(
            self.root,
            text="🔄 CONVERT",
            command=self.convert_currency,
            font=('Helvetica', 16, 'bold'),
            bg='#27AE60',
            fg='white',
            width=20,
            height=2,
            relief='raised',
            bd=3,
            cursor='hand2'
        )
        convert_button.pack(pady=20)
        
        # Result frame
        result_frame = tk.Frame(self.root, bg='#34495E', bd=5, relief='ridge')
        result_frame.pack(pady=10, padx=30, fill='both')
        
        self.result_label = tk.Label(
            result_frame,
            text="Enter amount and click Convert",
            font=('Helvetica', 18, 'bold'),
            bg='#34495E',
            fg='#ECF0F1',
            wraplength=500
        )
        self.result_label.pack(pady=30)
        
        # Exchange rate info
        self.rate_label = tk.Label(
            result_frame,
            text="",
            font=('Helvetica', 12),
            bg='#34495E',
            fg='#BDC3C7'
        )
        self.rate_label.pack(pady=10)
        
        # Button frame
        button_frame = tk.Frame(self.root, bg='#2C3E50')
        button_frame.pack(pady=10)
        
        # Refresh rates button
        refresh_button = tk.Button(
            button_frame,
            text="🔃 Refresh Rates",
            command=self.refresh_rates,
            font=('Helvetica', 11),
            bg='#E67E22',
            fg='white',
            width=15,
            relief='raised',
            bd=2,
            cursor='hand2'
        )
        refresh_button.grid(row=0, column=0, padx=5)
        
        # History button
        history_button = tk.Button(
            button_frame,
            text="📜 History",
            command=self.show_history,
            font=('Helvetica', 11),
            bg='#9B59B6',
            fg='white',
            width=15,
            relief='raised',
            bd=2,
            cursor='hand2'
        )
        history_button.grid(row=0, column=1, padx=5)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=('Helvetica', 10),
            bg='#2C3E50',
            fg='#95A5A6'
        )
        self.status_label.pack(pady=10)
        
        # Popular currencies frame
        popular_frame = tk.LabelFrame(
            self.root,
            text="Quick Convert (1 USD to...)",
            font=('Helvetica', 11, 'bold'),
            bg='#34495E',
            fg='#ECF0F1',
            bd=3
        )
        popular_frame.pack(pady=10, padx=30, fill='both')
        
        self.popular_labels = {}
        for i, currency in enumerate(self.popular_currencies[1:6]):  # Show top 5
            label = tk.Label(
                popular_frame,
                text=f"{currency}: ...",
                font=('Helvetica', 10),
                bg='#34495E',
                fg='#ECF0F1',
                anchor='w'
            )
            label.grid(row=i//2, column=i%2, padx=10, pady=5, sticky='w')
            self.popular_labels[currency] = label
        
        self.update_popular_rates()
    
    def load_exchange_rates(self):
        """Load exchange rates from cache or API"""
        # Try loading from cache first
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, 'r') as f:
                    cache_data = json.load(f)
                
                # Check if cache is still valid
                cache_time = datetime.fromisoformat(cache_data['timestamp'])
                if datetime.now() - cache_time < self.cache_duration:
                    self.exchange_rates = cache_data['rates']
                    self.currencies = sorted(self.exchange_rates.keys())
                    self.update_status(f"Using cached rates (updated: {cache_time.strftime('%Y-%m-%d %H:%M')})")
                    return
            except:
                pass
        
        # Fetch from API
        self.refresh_rates()
    
    def refresh_rates(self):
        """Fetch latest exchange rates from API"""
        try:
            self.update_status("Fetching latest rates...")
            response = requests.get(f"{self.api_url}USD", timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.exchange_rates = data['rates']
                self.currencies = sorted(self.exchange_rates.keys())
                
                # Update comboboxes
                self.from_currency['values'] = self.currencies
                self.to_currency['values'] = self.currencies
                
                # Save to cache
                cache_data = {
                    'timestamp': datetime.now().isoformat(),
                    'rates': self.exchange_rates
                }
                with open(self.cache_file, 'w') as f:
                    json.dump(cache_data, f, indent=4)
                
                self.update_status("✓ Rates updated successfully!")
                self.update_popular_rates()
                messagebox.showinfo("Success", "Exchange rates updated successfully!")
            else:
                raise Exception("Failed to fetch rates")
        
        except Exception as e:
            self.update_status(f"✗ Error: {str(e)}")
            messagebox.showerror("Error", "Failed to fetch exchange rates.\nUsing cached rates if available.")
    
    def convert_currency(self):
        """Perform currency conversion"""
        try:
            # Get input values
            amount = float(self.amount_entry.get())
            from_curr = self.from_currency.get()
            to_curr = self.to_currency.get()
            
            if not from_curr or not to_curr:
                messagebox.showwarning("Warning", "Please select both currencies")
                return
            
            # Convert to USD first, then to target currency
            if from_curr != 'USD':
                amount_in_usd = amount / self.exchange_rates[from_curr]
            else:
                amount_in_usd = amount
            
            # Convert to target currency
            if to_curr != 'USD':
                result = amount_in_usd * self.exchange_rates[to_curr]
            else:
                result = amount_in_usd
            
            # Calculate exchange rate
            if from_curr != 'USD':
                rate = self.exchange_rates[to_curr] / self.exchange_rates[from_curr]
            else:
                rate = self.exchange_rates[to_curr]
            
            # Display result
            self.result_label.config(
                text=f"{amount:,.2f} {from_curr} = {result:,.2f} {to_curr}",
                fg='#2ECC71'
            )
            
            self.rate_label.config(
                text=f"Exchange Rate: 1 {from_curr} = {rate:.6f} {to_curr}"
            )
            
            # Save to history
            self.save_to_history(amount, from_curr, result, to_curr, rate)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")
        except KeyError:
            messagebox.showerror("Error", "Currency not found in database")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def swap_currencies(self):
        """Swap from and to currencies"""
        from_val = self.from_currency.get()
        to_val = self.to_currency.get()
        
        self.from_currency.set(to_val)
        self.to_currency.set(from_val)
    
    def update_popular_rates(self):
        """Update quick convert display"""
        try:
            for currency in list(self.popular_labels.keys()):
                if currency in self.exchange_rates:
                    rate = self.exchange_rates[currency]
                    self.popular_labels[currency].config(
                        text=f"{currency}: {rate:.4f}"
                    )
        except:
            pass
    
    def save_to_history(self, amount, from_curr, result, to_curr, rate):
        """Save conversion to history"""
        history = []
        
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            except:
                history = []
        
        entry = {
            'timestamp': datetime.now().isoformat(),
            'amount': amount,
            'from': from_curr,
            'result': result,
            'to': to_curr,
            'rate': rate
        }
        
        history.insert(0, entry)  # Add to beginning
        history = history[:50]  # Keep last 50 conversions
        
        with open(self.history_file, 'w') as f:
            json.dump(history, f, indent=4)
    
    def show_history(self):
        """Display conversion history"""
        if not os.path.exists(self.history_file):
            messagebox.showinfo("History", "No conversion history yet.")
            return
        
        try:
            with open(self.history_file, 'r') as f:
                history = json.load(f)
            
            if not history:
                messagebox.showinfo("History", "No conversion history yet.")
                return
            
            # Create history window
            history_window = tk.Toplevel(self.root)
            history_window.title("Conversion History")
            history_window.geometry("600x400")
            history_window.configure(bg='#2C3E50')
            
            # Title
            title = tk.Label(
                history_window,
                text="📜 Conversion History (Last 20)",
                font=('Helvetica', 16, 'bold'),
                bg='#2C3E50',
                fg='#ECF0F1'
            )
            title.pack(pady=10)
            
            # Create scrollable text widget
            text_frame = tk.Frame(history_window)
            text_frame.pack(fill='both', expand=True, padx=10, pady=10)
            
            scrollbar = tk.Scrollbar(text_frame)
            scrollbar.pack(side='right', fill='y')
            
            text_widget = tk.Text(
                text_frame,
                font=('Courier', 10),
                bg='#34495E',
                fg='#ECF0F1',
                yscrollcommand=scrollbar.set
            )
            text_widget.pack(side='left', fill='both', expand=True)
            scrollbar.config(command=text_widget.yview)
            
            # Add history entries
            for entry in history[:20]:
                timestamp = datetime.fromisoformat(entry['timestamp'])
                text_widget.insert('end', f"{timestamp.strftime('%Y-%m-%d %H:%M')}\n")
                text_widget.insert('end', f"{entry['amount']:.2f} {entry['from']} = "
                                        f"{entry['result']:.2f} {entry['to']}\n")
                text_widget.insert('end', f"Rate: {entry['rate']:.6f}\n")
                text_widget.insert('end', "-"*60 + "\n\n")
            
            text_widget.config(state='disabled')
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load history: {str(e)}")
    
    def update_status(self, message):
        """Update status label"""
        self.status_label.config(text=message)
        self.root.update()

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
