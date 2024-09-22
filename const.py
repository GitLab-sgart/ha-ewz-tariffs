# Unique identifier for the integration
DOMAIN = "ewz_tariff"

# URL displaying the tariffs
TARIFF_URL = "https://www.ewz.ch/de/private/strom/tarife/tarifuebersicht.html"

# Default tariff, in case none is specified
DEFAULT_TARIFF = "ewz.natur"

# Available tariff options
TARIFF_OPTIONS = {
    "ewz.econatur": "EWZ Econatur",
    "ewz.natur": "EWZ Natur",
    "ewz.pronatur": "EWZ Pronatur"
}

# Time constants for high (Hochtarif) and low tariff (Niedertarif) periods (24h required!)
HOCHTARIF_START = 6  # -> 06:00
HOCHTARIF_END = 22   # -> 22:00