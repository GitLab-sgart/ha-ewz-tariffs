from homeassistant.components.number import NumberEntity


class HighTariff(NumberEntity):
    def set_native_value(self, value: float) -> None:
        # Update

    async def async_set_native_value(self, value: float) -> None:
        # Update


class LowTariff(NumberEntity):
    def set_native_value(self, value: float) -> None:
        # Update

    async def async_set_native_value(self, value: float) -> None:
        # Update