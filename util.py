from pathlib import Path
from typing import List, Set, Text

def load_stations(stations: Text) -> List[Text]:
    """Load station names. Returns List."""
    with open(stations, "r") as f:
        return [line.strip() for line in f.readlines()]


def load_stations2(stations: Text) -> List[Text]:
    """Load station names. Returns List."""
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
