from flask import Flask, render_template, request, send_file
from datetime import datetime
import csv
import requests
from api_service import *  
from graph_generator import generate_graph 

app = Flask(__name__)


BASE_URL = "https://www.alphavantage.co/query?"
INTERVAL = "5min"
API_KEY = "YOUR_API_KEY_HERE"  


def load_stock_symbols():
    symbols = []
    with open('stocks.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)   
        symbols = [row[0] for row in reader]  
    return symbols

@app.route("/", methods=["GET", "POST"])
def home():
    chart_path = None  
    symbols = load_stock_symbols()  

    if request.method == "POST":

        # Retrieve form data
        stock_symbol = request.form.get("stock_symbol")
        chart_type = request.form.get("chart_type")
        time_series_function = request.form.get("time_series_function")
        begin_date = request.form.get("begin_date")
        end_date = request.form.get("end_date")

        time_series_name = convert_time_series(time_series_function)

        url = construct_url(BASE_URL, time_series_name, stock_symbol, INTERVAL, API_KEY)
        response = requests.get(url)
        response.raise_for_status()
        stock_data = response.json()

        if "Error Message" in stock_data:
            return "Error fetching stock data. Please check the stock symbol and try again."

        chart_path = "static/stock_prices_graph.svg"
        generate_graph(stock_symbol, stock_data, chart_type, begin_date, end_date)

    return render_template("index.html", chart_path=chart_path, symbols=symbols)

@app.route("/download-chart")
def download_chart():
    return send_file("static/stock_prices_graph.svg", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)