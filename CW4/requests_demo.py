# Demonstrates requests
import sys
import requests


def itunes():
    if len(sys.argv) != 2:
        sys.exit()
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1]
    )
    obj = response.json()
    for result in obj["results"]:
        print(result["trackName"])


itunes()


def artist_chicago():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "limit": 3}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


artist_chicago()
