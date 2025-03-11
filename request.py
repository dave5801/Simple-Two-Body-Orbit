import requests

response = requests.get("http://127.0.0.1:5000/predict?time=120")
print(response.json())  # Output: {'time': 120, 'predicted_position': 0.5}