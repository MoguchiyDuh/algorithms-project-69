import math
import re
import string


def return_tf(text: str, word: str) -> float:
    words = text.split()
    word_count = len(words)
    return words.count(word) / word_count if word_count != 0 else 0


def return_idf(docs: list[dict], word: str) -> float:
    num_docs_with_word = 0
    for doc in docs:
        if re.search(rf"\b{word}\b", doc["text"], re.IGNORECASE):
            num_docs_with_word += 1
    result = len(docs) / (1 + num_docs_with_word)
    return math.log(result)


def search(docs: list[dict], words: str) -> list:
    translator = str.maketrans("", "", string.punctuation)
    words_list = words.translate(translator).lower().split()

    result = {}

    for doc in docs:
        text_cleaned: str = doc["text"].translate(translator).lower()
        tfidf_score = 0.0

        for word in words_list:
            tf = return_tf(text_cleaned, word)
            idf = return_idf(docs, word)
            tfidf_score += tf * idf

        if tfidf_score > 0:
            result[doc["id"]] = tfidf_score

    return [
        doc_id
        for doc_id, _ in sorted(result.items(), key=lambda item: item[1], reverse=True)
    ]


# def reverse_index(docs: list[dict]) -> dict:
#     docs_pre_word_list = {}

#     translator = str.maketrans("", "", string.punctuation)

#     for doc in docs:
#         words_list = doc["text"].translate(translator).lower().split()

#         for word in words_list:
#             if word not in docs_pre_word_list:
#                 docs_pre_word_list[word] = []

#             if doc["id"] not in docs_pre_word_list[word]:
#                 docs_pre_word_list[word].append(doc["id"])

#     return docs_pre_word_list
