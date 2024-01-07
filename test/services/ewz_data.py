import unittest
from unittest.mock import MagicMock

import services.general
from services.ewz_data import fetch_low_tariff

URL = "https://www.ewz.ch/de/private/strom/tarife/tarifuebersicht.html"
GENERAL_SERVICE_MOCK = services.general
GENERAL_SERVICE_MOCK.fetch_html_content = MagicMock(return_value="")

class EWZDataServiceTest(unittest.IsolatedAsyncioTestCase):
    async def test_data_extraction_call(self):
        await fetch_low_tariff()
        GENERAL_SERVICE_MOCK.fetch_html_content.assert_called_with(URL)
        self.assertIs()


if __name__ == '__main__':
    unittest.main()
