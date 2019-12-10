import logging

# logging setup
RESULTS = logging.getLogger("results")
RESULTS.setLevel(logging.INFO)
RESULTS.info("test of results log")

LOG = logging.getLogger("googlemaps")
LOG.setLevel(logging.DEBUG)
LOG.info("test of debug log")

# create logger
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
# 
# create console handler and set level to debug
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to ch
# ch.setFormatter(formatter)
# add ch to logger
# logger.addHandler(ch)
# 'application' code
# logger.debug('debug message')


DEST = "Shinjuku Station" # change for different target venues
FARES = "fares/"
ICONS = "icons/"
ISSUE_STATIONS = "data/stations/issuestations.txt"
STATION_FILE = "data/stations/C.txt"
TARGET_STATIONS = "data/trains/TokyoMetro.txt"

#icons
ARROW1 = ICONS+"directionarrow1.png"
ARROW2 = ICONS+"directionarrow2.png"
CHROME = ICONS+"googlechrome.png"
FULLSCREENDOT = ICONS+"fullscreendot.png"
MAPS = ICONS+"googlemaps.png"
SEARCH_INPUT = ICONS+"searchinput.png"
TRANSIT = ICONS+"transit.png"
YEN = ICONS+"yen.png"
