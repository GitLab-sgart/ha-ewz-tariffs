import requests

def fetch_html_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return ""