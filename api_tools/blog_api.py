import requests
from pprint import pp

def get_blogs(blog_url: str):
    response = requests.get(blog_url)
    return response


def main():
    # Using: https://www.npoint.io
    # API Example:  https://api.npoint.io/c790b4d5cab58020d391
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    return response


if __name__ == '__main__':
    print("Running Local...")
    test = main().json()
    pp(test)
