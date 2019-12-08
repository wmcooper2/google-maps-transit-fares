from constants import *
from pathlib import Path
from typing import List, Set, Text

def load_stations(stations: Text) -> List[Text]:
    """Load station names. Returns List.

    Example:
    If the lines in "stations" text file look like this...
        Abe
        Abekawa

    The return list looks like this...
        ["Abe", "Abekawa"]
    """

    with open(stations, "r") as f:
        return [line.strip() for line in f.readlines()]


def load_stations_long_name(stations: Text) -> List[Text]:
    """Load station names. Returns List.

    Example: 
    If the lines in "stations" text file look like this...
        Abe Station	安部駅（あべ）
        Abekawa Station	安倍川駅（あべかわ）
    
    The return list looks like this...
        ["Abe", "Abekawa"]
    """

    with open(stations, "r") as f:
        eng_jap_name = [line.strip() for line in f.readlines()]
    stations = [name.split("\t") for name in eng_jap_name]
    return [station[0].split(" ")[0] for station in stations]


def file_counter(_dir: Text) -> int:
    """Count files in _dir. Returns int."""
    return sum([1 for p in Path(_dir).iterdir()])


def fares_already_scraped(_dir: Text) -> Set[Text]:
    """Loads names of stations already looked up. Returns set."""
    return set([str(p.name).split(" ")[0] for p in Path(_dir).iterdir()])


def load_fares_waiting(_file: Text) -> Set[Text]:
    """Loads names of stations waiting to be scraped. Returns Set."""
    all_stations = set(load_stations(_file))
    stations_finished = fares_already_scraped(FARES)
    error_stations = set(load_stations(ISSUE_STATIONS))

    #print simple stats, delete before wrapping up
    #send to log
    print(f"Stations in {STATION_FILE}: {len(all_stations)}")
    print(f"Error stations: {len(error_stations)}")
    return all_stations.difference(stations_finished, error_stations)


