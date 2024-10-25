# Project3-StockDataVisualizer
Scrum Team 15's Stock Data Visualizer Application

# Kymanis-Branch
Error handling in get_stock_data_input():

Encloses the entire input collection in a try block to catch unexpected errors, outputting an error message and returning None values for safety.
API call error handling:

Uses response.raise_for_status() to catch HTTP errors (e.g., 404 or 500 errors).
Checks the response JSON for errors specific to the stock data API, such as an "Error Message" field.
General Exception Handling:

Captures all other unexpected errors in the API call section with except Exception as e.
