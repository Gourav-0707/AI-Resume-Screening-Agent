def extract_education(text):

    text = text.lower()

    education = [
        "phd",
        "master",
        "m.tech",
        "b.tech",
        "b.e",
        "bachelor",
        "mba",
        "mca",
        "bca"
    ]

    for degree in education:
        if degree in text:
            return degree.upper()

    return "Not Found"