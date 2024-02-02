import pyodbc
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

server = "database.sql.azuresynapse.net"
database = "database"

connection_string = (
    f"Driver=ODBC Driver 18 for SQL Server;"
    f"Server={server};"
    f"Database={database};"
    f"Authentication=ActiveDirectoryInteractive;"
    f"UID=;"
    f"PWD=;"
    f"AuthenticationMethod=ActiveDirectoryInteractive"
)

def execute_query(query):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame.from_records(rows, columns=columns)

    cursor.close()
    conn.close()

    return df.to_dict(orient='records')

@app.route('/query', methods=['POST'])
def query_data():
    try:
        data = request.json
        query = data.get('query')
        result = execute_query(query)
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
