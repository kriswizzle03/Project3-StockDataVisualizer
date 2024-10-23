from datetime import datetime

def get_stock_data_input():
    stock_symbol = input("Stock Data Visualizer Group 15 \n------------------------------------- \n\nEnter the stock symbol for the company you want data for: ").strip()

    while True:
        chart_type = input("\nEnter the graph type: \n----------------- \n1. Bar Graph \n2. Line Graph \nEnter the graph type you want (1 or 2):  ").strip()
        if chart_type in ["1", "2"]:
            break
        print("Invalid option. Please enter 1 for Bar Graph or 2 for Line Graph.")

    while True:
        time_series_function = input("\nSelect the Time Series of the chart you want to generate \n-------------------------------------------------------------- \n1. Intraday \n2. Daily \n3. Weekly \n4. Monthly \n\nEnter time series option (1, 2, 3, 4): ").strip()
        if time_series_function in ["1", "2", "3", "4"]:
            break
        print("Invalid option. Please enter 1, 2, 3, or 4.")

    while True:
        begin_date = input("\nEnter the beginning date (YYYY-MM-DD): ").strip()
        try:
            begin_date_dt = datetime.strptime(begin_date, "%Y-%m-%d")
            break
        except ValueError:
            print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.")
    while True:
        end_date = input("\nEnter the end date (YYYY-MM-DD): ").strip()
        try:
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
            if end_date_dt < begin_date_dt:
                print("\nEnd date cannot be before the beginning date. Please enter a valid end date.")
            else:
                break
        except ValueError:
            print("\nInvalid date format. Please enter the date in YYYY-MM-DD format.")

    return stock_symbol, chart_type, time_series_function, begin_date, end_date

stock_data = get_stock_data_input()
print(stock_data)
