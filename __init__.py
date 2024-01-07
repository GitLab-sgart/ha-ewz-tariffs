async def setup(hass, config):

    # Service for reloading data
    def handle_reload(call):
        # Handle call
        return
    hass.services.register('reload', 'reload', handle_reload)

    return True
