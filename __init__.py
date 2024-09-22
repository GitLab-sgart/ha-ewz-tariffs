from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from const import DOMAIN

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the EWZ Tariff integration."""
    # This function is called when Home Assistant starts up.

    # Set up the integration, but don't need to do anything else for now
    return True

async def async_setup_entry(hass: HomeAssistant, entry) -> bool:
    """Set up the EWZ Tariff from a config entry."""

    # This is called when the user adds the integration through the UI (using config_flow).

    # Register the sensor platform
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )

    return True

async def async_unload_entry(hass: HomeAssistant, entry) -> bool:
    """Handle removal of an entry."""

    # This is called when the user removes the integration.
    # We need to clean up the sensor platform when the integration is removed.
    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")

    return unload_ok
