import requests
import json
from datetime import datetime

API_ENDPOINT = "https://your-api.com/upload"  # Replace with real endpoint
API_KEY = "your_api_key_here"  # Optional: Include in headers

def collect_stats():
    print("Enter Aimlabs stats:")
    username = input("Username: ")
    scenario = input("Scenario (e.g., Gridshot): ")
    score = int(input("Score: "))
    accuracy = float(input("Accuracy (%): "))
    kills = int(input("Kills: "))
    shots_fired = int(input("Shots Fired: "))
    headshot_ratio = float(input("Headshot Ratio (0.0 - 1.0): "))

    data = {
        "username": username,
        "scenario": scenario,
        "score": score,
        "accuracy": accuracy,
        "kills": kills,
        "shots_fired": shots_fired,
        "headshot_ratio": headshot_ratio,
        "date_played": datetime.utcnow().isoformat()
    }

    return data

def upload_stats(data):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"  # Optional
    }
    try:
        response = requests.post(API_ENDPOINT, headers=headers, json=data)
        if response.status_code == 200:
            print("✅ Stats uploaded successfully!")
        else:
            print(f"❌ Failed to upload. Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"❌ Upload error: {e}")

if __name__ == "__main__":
    stats = collect_stats()
    upload_stats(stats)
