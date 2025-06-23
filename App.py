from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'port':'3306',
    'user': 'root',
    'password': 'keya123',
    'database': 'imdb'
}

# Route to fetch data and return it as JSON
@app.route('/fetchdata', methods=['GET'])
def fetch_data():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Execute a query to fetch data
        cursor.execute("SELECT title,country FROM movie")
        data = cursor.fetchall()

        # Close database connection
        cursor.close()
        conn.close()

        # Return the fetched data as JSON
        return jsonify(data)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Route to render HTML page
@app.route('/')
def index():
    return render_template('App.html')

if __name__ == '__main__':
    app.run(debug=True)
