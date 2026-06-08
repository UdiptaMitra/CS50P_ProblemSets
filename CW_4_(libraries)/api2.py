import sys
import requests


def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
