from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

# Get the API key from environment variable
RIOT_API_KEY = os.environ.get('RIOT_API_KEY', '')
if not RIOT_API_KEY:
    print("WARNING: No Riot API key found in environment variables")

# Base URLs for Riot API
RIOT_API_BASE_URL = "https://na1.api.riotgames.com/lol"

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/summoner/<name>', methods=['GET'])
def get_summoner(name):
    url = f"{RIOT_API_BASE_URL}/summoner/v4/summoners/by-name/{name}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"Failed to fetch summoner data: {response.status_code}"}), response.status_code

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
