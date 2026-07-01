from flask import Flask, render_template, request, jsonify
import requests
from config import API_KEY

app = Flask(__name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():

    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Please enter a city name."})

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        data = response.json()

        if response.status_code != 200:
            return jsonify({"error": data.get("message", "City not found")})

        temp_c = data["main"]["temp"]
        temp_f = round((temp_c * 9 / 5) + 32, 2)

        result = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature_c": temp_c,
            "temperature_f": temp_f,
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }

        return jsonify(result)

    except requests.exceptions.Timeout:
        return jsonify({"error": "Request Timed Out"})

    except:
        return jsonify({"error": "Network Error"})


if __name__ == "__main__":
    app.run(debug=True)