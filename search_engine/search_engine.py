import re
import string


def search(docs: dict, words: str) -> list:
    result = {}

    def sort_by_values_desc(dict_to_sort: dict) -> list:
        return [
            key
            for key, value in sorted(
                dict_to_sort.items(), key=lambda item: item[1], reverse=True
            )
        ]

    translator = str.maketrans("", "", string.punctuation)
    words_list = words.translate(translator).split(" ")
    for doc in docs:
        print(doc)
        number_of_entries = 0
        for word in words_list:
            print(word)
            pattern = rf"\b{word}\b"
            entries = re.findall(pattern, doc["text"], re.IGNORECASE)
            if entries:
                number_of_entries += len(entries)
        if number_of_entries != 0:
            result[doc["id"]] = number_of_entries
            print(number_of_entries)

    return sort_by_values_desc(result)
