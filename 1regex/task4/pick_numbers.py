"""import re

def pick_numbers(text: str) -> list[str]:
    return re.split(r"", text)"""

import re

def pick_numbers(text):
    numbers = re.findall(r'\b\d+\b', text)
    return [int(num) for num in numbers]