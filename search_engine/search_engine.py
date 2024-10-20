import re


def search(docs: dict, str_to_find: str) -> list:
    result = []
    query = re.escape(str_to_find.rstrip(".,!?"))
    for doc in docs:
        pattern = rf"\b{query}\b"
        if re.findall(pattern, doc["text"], re.IGNORECASE):
            result.append(doc["id"])
    return result
