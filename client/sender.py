import requests

def send_message():
    while True:
        link = input()

        if link is None or link == '':
            print("Wrong argument")

        else:
            for url in link.split(";"):
                response_code = str(requests.post('http://localhost:8000', data=url))
                if '200' in response_code:
                    print("Successfully send")
                elif '400' in response_code:
                    print("Bad request")

send_message()