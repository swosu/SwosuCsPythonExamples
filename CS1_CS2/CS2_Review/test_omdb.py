import requests

API_KEY = "7ad6b576"
BASE_URL = "http://www.omdbapi.com/"

print("API_KEY repr:", repr(API_KEY))

def get_movie_by_title(title: str):
    params = {
        "apikey": API_KEY.strip(),   # <-- strip just in case
        "t": title,
        "plot": "short"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data.get("Response") == "False":
        print(f"Error: {data.get('Error')}")
        return None

    return data

if __name__ == "__main__":
    movie = get_movie_by_title("Inception")
    print(movie)
