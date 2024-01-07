from homeasistant import config_entries
from const import DOMAIN

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step(self):
        return True