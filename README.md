# Stock Portfolio Tracker

This is a real-time stock portfolio tracking desktop application built using **Python**, **customtkinter**, and **yfinance**, developed as part of my internship project at **CodeAlpha**.

The tool allows users to manage a personal stock portfolio by adding stock symbols and quantities, tracking real-time market prices, and visualizing investment distribution using an interactive pie chart.

---

## Features

- Real-time price fetching for global and Indian stock symbols
- Intuitive and modern user interface using `customtkinter`
- Dashboard layout with tabbed views
- Pre-filled suggestions for popular stocks
- Portfolio summary including total investment
- Export data to `.csv` or `.txt` file
- Interactive pie chart visualization with Plotly

---


## Technologies Used

- Python 3.x
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) – for modern, themed UI components
- [yfinance](https://pypi.org/project/yfinance/) – for live stock data
- [Plotly](https://plotly.com/python/) – for interactive charts

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/rishiii026/CodeAlpha_StockPortfolioTracker.git
cd CodeAlpha_StockPortfolioTracker

###2. Install dependencies
pip install customtkinter yfinance plotly

###3. Run the application
python stock_tracker_ctk.py

## Project Structure
├── stock_tracker_ctk.py      # Main application file
├── README.md                 # Project documentation



##Future Enhancements

-Price history chart under the History tab

-Total gains/losses summary

-Sector-wise investment analysis

-Web-based deployment using Flask or Streamlit

## About the Project

$$$ This project was developed during my internship at CodeAlpha as a demonstration of full-stack Python application development with real-time data integration and modern UI design.

For any feedback or collaboration opportunities, feel free to get in touch.