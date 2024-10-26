# Project3-StockDataVisualizer
Scrum Team 15's Stock Data Visualizer Application

## To ensure the application is functional make sure the following python dependencies are installed/included:
- pygal
- lxml
- requests

# masonk-5-patch-1
Branch which establishes the questions the user is prompted with to enter necessary stock data.

# Kymanis-Branch
Error handling in get_stock_data_input():

Encloses the entire input collection in a try block to catch unexpected errors, outputting an error message and returning None values for safety.
API call error handling:

Uses response.raise_for_status() to catch HTTP errors (e.g., 404 or 500 errors).
Checks the response JSON for errors specific to the stock data API, such as an "Error Message" field.
General Exception Handling:

Captures all other unexpected errors in the API call section with except Exception as e.

# feature-APIquery
Branch for creating the unique API url using parameters from the user's input and retrieving JSON data from the Alpha Vantage server.

# cavenm-graph
Branch for reading JSON data from the API url and rendering it via a bar graph or line graph on the user's browser. Note: this branch also employs error handling to ensure there are no unexpected program crashes.
