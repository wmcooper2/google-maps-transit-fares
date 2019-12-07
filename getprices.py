try:
    from PIL import Image
except ImportError:
    import Image

from pathlib import Path
import pytesseract
from typing import Text

def extract_num(num: Text) -> Text:
    """Extracts the number portion of num. Returns string."""
    return num.split("¥")[-1]


def image_to_number(path: Text) -> int:
    """Converts png image of price to a number. Returns int."""
    num = pytesseract.image_to_string(Image.open(path))
    try: 
        return int(num)
    except ValueError:
        return int(extract_num(num))


if __name__ == "__main__":
    for p in Path("fares").iterdir():
        print(image_to_number(str(p)))
