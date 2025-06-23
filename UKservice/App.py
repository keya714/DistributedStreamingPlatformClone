from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetch_data():
    # Fetch data from the external URL
    try:
        response = requests.get("http://172.19.0.3:8000/hello")
        # print(response)
        response.raise_for_status()  # Check for HTTP request errors
        
        data = json.loads(response.text)  # Parse the data as JSON
        # print(data)
        country = "UK"  # Specify the country for filtering

        # Filter movies by the specified country, ensuring 'country' is a string
        movies = [movie for movie in data if isinstance(movie.get("country"), str) and country in movie["country"]]

    except requests.RequestException as e:
        # In case of an error, return an error message in JSON format
        return jsonify({"error": str(e)}), 500

    # Return the filtered movies as a JSON response
    return jsonify(movies)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8051)


# from flask import Flask, jsonify
# import requests

# app = Flask(__name__)

# @app.route('/getmovies')
# def fetch_json_data():
#     url = "http://172.19.0.3:8000/hello"  # Replace with the actual URL
#     try:
#         response = requests.get(url)
#         print(response)
#         response.raise_for_status()  # Check for HTTP request errors
#         json_data = response.json()  
#         print(json_data)
#     except requests.RequestException as e:
#         return jsonify({"error": str(e)}), 500

#     return jsonify(json_data)

# @app.route('/')
# def fetch_data():
#     print("keya")
#     return "Hello!!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8050)
