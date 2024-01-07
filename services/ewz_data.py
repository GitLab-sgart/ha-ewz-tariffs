from services.general import fetch_html_content

URL = "https://www.ewz.ch/de/private/strom/tarife/tarifuebersicht.html"

async def fetch_low_tariff():
    content = fetch_html_content(URL)



