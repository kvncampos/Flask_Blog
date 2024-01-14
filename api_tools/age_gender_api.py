import requests

AGIFY_URL = 'https://api.agify.io'  # example: https://api.agify.io?name=michael
GENDERIZE_URL = 'https://api.genderize.io'  # example: https://api.genderize.io?name=peter


def agify_api(name: str):
    params = {
        'name': name
    }
    response = requests.get(url=AGIFY_URL, params=params)

    print(response.text)
    return response.json()['age']


def gender_api(name: str):
    params = {
        'name': name
    }
    response = requests.get(url=GENDERIZE_URL, params=params)

    print(response.text)
    return response.json()['gender']


def main():
    print("Running Locally...")
    agify_api('michael')
    gender_api('michael')


if __name__ == '__main__':
    main()
