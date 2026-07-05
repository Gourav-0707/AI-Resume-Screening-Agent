import re

def extract_experience(text):
    pattern = r'(\d+)\+?\s*(?:years|year)'
    match = re.search(pattern, text.lower())

    if match:
        return int(match.group(1))

    return 0