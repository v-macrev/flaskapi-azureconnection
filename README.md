# Flask Web App API for Azure Synapse SQL Database

This script is a Flask web application that acts as a simple API for executing SQL queries on an Azure Synapse SQL database. It exposes a single API endpoint (/query) that accepts POST requests with a JSON payload containing a 'query' key, and it returns the results of the executed SQL query in JSON format. The application uses the pyodbc library to connect to the Azure Synapse SQL database and the pandas library to convert query results into a JSON-friendly format. It's a basic example and should be extended with security measures and additional features for a production environment.

## Getting Started

### Prerequisites

- Python 3.10 installed
- [Virtual Environment](https://docs.python.org/3/library/venv.html) (recommended)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/v-macrev/flaskapi-azureconnection.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flaskapi-azureconnection
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv apienv
   source apienv/bin/activate   # For Unix/Linux
   # or
   .\apienv\Scripts\activate    # For Windows
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the Flask web application:

   ```bash
   flask run
   ```
or

   ```bash
   python main.py
   ```

2. Open your favorite API testing tool, such as [Postman](https://www.postman.com/) or use the provided `test.http` file.

3. Send sample requests to the API to execute SQL queries on the Azure Synapse SQL database.

### Testing with `test.http`

For your convenience, I've included a `test.http` file that contains sample HTTP requests to test various endpoints of the API. You can use this file with an extension like [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) in Visual Studio Code or other similar tools.

## Contributing

If you encounter any issues or have suggestions for improvement, feel free to [open an issue](https://github.com/v-macrev/flaskapi-azureconnection/issues) or submit a pull request.

Happy coding!
