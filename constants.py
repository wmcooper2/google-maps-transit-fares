import logging

# logging setup
RESULTS = logging.getLogger("results")
RESULTS.setLevel(logging.INFO)
RESULTS.info("test of results log")
LOG = logging.getLogger("googlemaps")
LOG.setLevel(logging.DEBUG)
LOG.info("test of debug log")

# DEST = "Shinjuku" # change for different target venues
DESTINATIONS = "data/destinations.txt"
FARES = "fares/"
ICONS = "icons/"
ISSUE_STATIONS = "data/stations/issuestations.txt"
STATION_FILE = "data/stations/C.txt"
TARGET_STATIONS = "data/trains/TokyoMetro.txt"

# icons
ARROW1 = ICONS+"arrow1.png"
ARROW2 = ICONS+"arrow2.png"
CHROME = ICONS+"chrome.png"
CLOSE = ICONS+"closedirections.png"
FULLSCREENDOT = ICONS+"fullscreendot.png"
MAPS = ICONS+"maps.png"
SEARCH_INPUT = ICONS+"searchinput.png"
TRANSIT = ICONS+"transit.png"
TRAINRESULT = ICONS+"trainresult.png"
YEN = ICONS+"yen.png"

# settings
ERR_LIM = 20


# example settings
EXAMPLES = "examples/"
EXAMPLE_DESTINATIONS = EXAMPLES+"to_stations.txt"
EXAMPLE_TARGET_STATIONS = EXAMPLES+"from_stations.txt"
EXAMPLE_ISSUE_STATIONS = EXAMPLES+"error_stations.txt"
