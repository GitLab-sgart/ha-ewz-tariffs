import requests
import html
from bs4 import BeautifulSoup
from const import TARIFF_URL


def get_tariff_data():
    url = TARIFF_URL
    response = requests.get(url)
    ewz_page_soup = BeautifulSoup(response.text, 'html.parser')

    tariffs = {}

    # Find the table for each tariff type
    ewz_tables = ewz_page_soup.find_all('ewz-table')
    for ewz_table in ewz_tables:
        # Unescape the element to access the table element and it's data
        html_ewz_table = html.unescape(str(ewz_table).replace('<ewz-table content=\'', '').replace('\' hascolheader="true" hasrowheader="true" slot="layout-8-1" tablecaption="&lt;p&gt;Alle Angaben verstehen sich in Rp./kWh&lt;/p&gt;\n&lt;p&gt;Für Kund*innen in Graubünden beträgt die kommunale Abgabe inkl. MwSt. 2,26 Rp./kWh bzw. 2,10 Rp./kWh exkl. MwSt.&lt;/p&gt;">\n</ewz-table>', ''))
        ewz_table_soup = BeautifulSoup(html_ewz_table, 'html.parser')
        table = ewz_table_soup.find('table')
        # Loop through each td and check for numerical value
        found_values = []
        for td in table:
            for data in td.text.split('\n'):
                try:
                    found_values.append(float(data.strip().replace(',', '.')))
                except ValueError as e:
                    # Ignore, as this means there is no numerical value
                    continue
        # Extract the 4th and 3rd last two values as these are the total tariffs including tax
        try:
            hochtarif_rp = found_values[-4]
            niedertarif_rp = found_values[-3]
        except IndexError:
            # Ignore, as this means the current td does not contain any data
            continue

        # Convert data from Rp./kWh to CHF/kWh and add it to tariffs object
        hochtarif = hochtarif_rp / 100
        niedertarif = niedertarif_rp / 100
        if ewz_tables.index(ewz_table) == 3:
            tariffs['ewz.econatur'] = {'hochtarif': hochtarif, 'niedertarif': niedertarif}
        elif ewz_tables.index(ewz_table) == 2:
            tariffs['ewz.natur'] = {'hochtarif': hochtarif, 'niedertarif': niedertarif}
        elif ewz_tables.index(ewz_table) == 1:
            tariffs['ewz.pronatur'] = {'hochtarif': hochtarif, 'niedertarif': niedertarif}

    return tariffs
