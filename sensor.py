from homeassistant.helpers.entity import Entity
from datetime import datetime, time

from const import HOCHTARIF_START, HOCHTARIF_END
from scraper import get_tariff_data

class EWZTariffSensor(Entity):
    def __init__(self, tariff_type):
        self._state = None
        self._tariff_type = tariff_type
        self._tariffs = get_tariff_data()

    @property
    def name(self):
        return f"EWZ {self._tariff_type} Tariff"

    @property
    def state(self):
        # Update the state depending on the time of day (Hochtarif/Niedertarif)
        current_time = datetime.now().time()
        hochtarif_start = time(HOCHTARIF_START, 0)
        hochtarif_end = time(HOCHTARIF_END, 0)

        if hochtarif_start <= current_time < hochtarif_end:
            # Hochtarif (day tariff)
            return self._tariffs[self._tariff_type]['hochtarif']
        else:
            # Niedertarif (night tariff)
            return self._tariffs[self._tariff_type]['niedertarif']

    @property
    def unit_of_measurement(self):
        return "CHF/kWh"

    def update(self):
        # Optionally refresh tariff data on every update
        self._tariffs = get_tariff_data()
