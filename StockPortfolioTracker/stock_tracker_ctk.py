import customtkinter as ctk
from tkinter import messagebox, filedialog
import yfinance as yf
import plotly.graph_objects as go

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

user_portfolio = {}

popular_stocks = ["AAPL", "TSLA", "GOOG", "AMZN", "INFY.NS", "HDFCBANK.NS", "TCS.NS"]

# --- Fetch real-time stock price using yfinance ---
def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        return stock.history(period='1d')['Close'].iloc[-1]
    except:
        return None

# --- Add stock to portfolio ---
def update_portfolio():
    stock = stock_var.get().upper()
    qty = quantity_entry.get()
    try:
        qty = int(qty)
        if qty <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive quantity.")
        return

    price = get_stock_price(stock)
    if price is None:
        messagebox.showerror("Error", f"Could not fetch price for {stock}.")
        return

    if stock in user_portfolio:
        user_portfolio[stock]['qty'] += qty
    else:
        user_portfolio[stock] = {'qty': qty, 'price': price}

    display_summary()

# --- Display portfolio summary ---
def display_summary():
    summary_text.configure(state='normal')
    summary_text.delete("0.0", "end")
    total = 0
    for stock, data in user_portfolio.items():
        qty = data['qty']
        price = data['price']
        value = qty * price
        total += value
        summary_text.insert("end", f"{stock}: {qty} × ${price:.2f} = ${value:.2f}\n")
    summary_text.insert("end", f"\nTotal Investment: ${total:.2f}")
    summary_text.configure(state='disabled')

# --- Save to file ---
def save_to_file():
    if not user_portfolio:
        messagebox.showinfo("Info", "Portfolio is empty.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv"), ("Text files", "*.txt")])
    if not file_path:
        return
    with open(file_path, 'w') as f:
        f.write("Stock,Quantity,Price,Value\n")
        total = 0
        for stock, data in user_portfolio.items():
            qty = data['qty']
            price = data['price']
            value = qty * price
            total += value
            f.write(f"{stock},{qty},{price:.2f},{value:.2f}\n")
        f.write(f"\nTotal Investment,,,{total:.2f}")
    messagebox.showinfo("Saved", f"Data saved to {file_path}")

# --- Show interactive pie chart using Plotly ---
def show_pie_chart():
    if not user_portfolio:
        messagebox.showinfo("Info", "Portfolio is empty.")
        return

    labels, values = [], []
    for stock, data in user_portfolio.items():
        qty = data['qty']
        price = data['price']
        labels.append(stock)
        values.append(qty * price)

    if values:
        fig = go.Figure(data=[
            go.Pie(labels=labels, values=values, textinfo='label+percent',
                   hoverinfo='label+value', marker=dict(colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A']),
                   insidetextorientation='radial')
        ])
        fig.update_layout(title="Investment Distribution", template="plotly_dark")
        fig.show()
    else:
        messagebox.showerror("Error", "No valid data to plot.")

# --- UI Setup ---
root = ctk.CTk()
root.title("📊 Stock Portfolio Dashboard")
root.geometry("750x650")

header = ctk.CTkLabel(root, text="Stock Portfolio Tracker Dashboard", font=("Segoe UI", 22, "bold"))
header.pack(pady=15)

tabs = ctk.CTkTabview(root, width=720, height=550)
tabs.pack(pady=10)

portfolio_tab = tabs.add("Portfolio")
history_tab = tabs.add("History")  # Placeholder for now
stats_tab = tabs.add("Dashboard")  # Placeholder for future stats

# --- Portfolio Tab Layout ---
input_frame = ctk.CTkFrame(portfolio_tab, corner_radius=10)
input_frame.pack(pady=10)

stock_var = ctk.StringVar(value="AAPL")

stock_label = ctk.CTkLabel(input_frame, text="Stock Symbol:", font=("Segoe UI", 14))
stock_label.grid(row=0, column=0, padx=10, pady=10)
stock_dropdown = ctk.CTkComboBox(input_frame, values=popular_stocks, variable=stock_var, width=200, font=("Segoe UI", 14))
stock_dropdown.grid(row=0, column=1, padx=10, pady=10)

quantity_label = ctk.CTkLabel(input_frame, text="Quantity:", font=("Segoe UI", 14))
quantity_label.grid(row=1, column=0, padx=10, pady=10)
quantity_entry = ctk.CTkEntry(input_frame, width=200, font=("Segoe UI", 14))
quantity_entry.grid(row=1, column=1, padx=10, pady=10)

btn_frame = ctk.CTkFrame(portfolio_tab, corner_radius=10)
btn_frame.pack(pady=10)

add_btn = ctk.CTkButton(btn_frame, text="➕ Add Stock", command=update_portfolio, width=150, corner_radius=16, hover_color="#00cc99")
add_btn.grid(row=0, column=0, padx=10)

save_btn = ctk.CTkButton(btn_frame, text="💾 Save Portfolio", command=save_to_file, width=150, corner_radius=16, hover_color="#3399ff")
save_btn.grid(row=0, column=1, padx=10)

chart_btn = ctk.CTkButton(btn_frame, text="📊 Show Pie Chart", command=show_pie_chart, width=150, corner_radius=16, hover_color="#ffaa00")
chart_btn.grid(row=0, column=2, padx=10)

summary_text = ctk.CTkTextbox(portfolio_tab, height=300, width=670, font=("Consolas", 12))
summary_text.pack(pady=10)
summary_text.configure(state='disabled')

root.mainloop()
