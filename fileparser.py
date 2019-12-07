from typing import List, Text

def parser(filename: Text) -> List[Text]:
    with open(filename, "r") as myfile:
        return [line.strip() for line in myfile.readlines()]
