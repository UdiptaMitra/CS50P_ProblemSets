import requests


def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    print(content)


main()
