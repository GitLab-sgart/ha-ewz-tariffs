import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from const import DOMAIN, TARIFF_OPTIONS, DEFAULT_TARIFF


class EWZTariffConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for EWZ Tariff."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step where the user selects the tariff."""

        if user_input is not None:
            # When the user submits their input, create the entry.
            return self.async_create_entry(title="EWZ Tariff Type", data=user_input)

        # Show the configuration form with the tariff selection dropdown.
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("tariff_type", default=DEFAULT_TARIFF): vol.In(TARIFF_OPTIONS)
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Handle options flow, which allows users to change settings later."""
        return EWZTariffOptionsFlowHandler(config_entry)


class EWZTariffOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow to modify settings after setup."""

    def __init__(self, config_entry):
        """Initialize the options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options menu, allowing changes to settings."""
        if user_input is not None:
            # Update the configuration entry with new data
            return self.async_create_entry(title="", data=user_input)

        # Display the form again with the current settings pre-filled
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required("tariff_type", default=self.config_entry.data.get("tariff_type", "ewz.econatur")): vol.In(TARIFF_OPTIONS)
            })
        )
