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


def reverse_index(docs: dict) -> dict:
    doc_ids_dict = {}

    for doc in docs:
        text: str = doc["text"]
        words: list[str] = text.split(" ")
        print(words)
        for word in words:
            if word in doc_ids_dict:
                if doc["id"] not in doc_ids_dict[word]:
                    doc_ids_dict[word] += [doc["id"]]
            else:
                doc_ids_dict[word] = [doc["id"]]

    return doc_ids_dict
