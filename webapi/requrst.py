import requests


def main():
    respone = requests.get('https://www.google.com/fucker-come-fucking/')
    print("status code :",respone.status_code)

if __name__ == '__main__':
    main()
