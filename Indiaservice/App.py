from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)

# Define a constant for the expected API key
# EXPECTED_API_KEY = "apikey"  # Replace with your actual key if it's different

@app.route('/', methods=['GET'])
def fetch_data():

    # Check for the apikey and consumer in the query parameters
    apikey = request.args.get("apikey")
    print(apikey)
    consumer = request.args.get("consumer")
    print(consumer)
    
    app.logger.debug(f"Received API key: {apikey}")
    app.logger.debug(f"Received consumer: {consumer}")
    
    # Ensure both apikey and consumer are provided and the apikey matches
    # if apikey != EXPECTED_API_KEY or not consumer:
    #     return jsonify({"error": "Invalid or missing API key or consumer"}), 403

    # Proceed to fetch data from the external URL if the key and consumer are valid
    try:
        # Pass both apikey and consumer as parameters to the external request
        response = requests.get(
            "http://172.19.0.3:8000/hello",
            params={"apikey": apikey, "consumer":consumer}
        )
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the data as JSON
        data = json.loads(response.text)
        country = "India"  # Specify the country for filtering

        # Filter movies by the specified country, ensuring 'country' is a string
        movies = [movie for movie in data if isinstance(movie.get("country"), str) and country in movie["country"]]

    except requests.RequestException as e:
        # In case of an error, return an error message in JSON format
        return jsonify({"error": str(e)}), 500

    # Return the filtered movies as a JSON response
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
