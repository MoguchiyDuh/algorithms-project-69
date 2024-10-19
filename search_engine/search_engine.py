import re


def search(texts: dict, str_to_find: str) -> list:
    result = []
    for text in texts:
        pattern = rf"\b{str_to_find}\b"
        if re.findall(pattern, text["text"]):
            result.append(text["id"])
    return result
