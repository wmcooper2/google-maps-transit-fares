from pathlib import Path
from typing import Generator
import pytesseract

for p in Path("fares").iterdir():
    print(p.name.strip(".png").split("_"))

