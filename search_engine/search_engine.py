import math
import re


def search(docs: list[dict], words: str):

    def calculate_idf(docs: list[dict], word: str) -> float:
        pattern = rf"\b{word}\b"
        num_docs_with_word = sum(
            1 for doc in docs if re.search(pattern, doc["text"], re.IGNORECASE)
        )
        total_docs = len(docs)
        if total_docs == 1:
            return 1
        return (
            math.log(total_docs / (num_docs_with_word))
            if num_docs_with_word > 0
            else 0.0
        )

    def calculate_tf(text: str, word: str) -> float:
        words = text.split()
        word_count = len(words)
        return words.count(word.lower()) / word_count if word_count > 0 else 0.0

    def prettify(text: str) -> str:
        return re.sub(r"[^\w\s]", "", text).lower()

    result = {}
    words_list = prettify(words).split()

    for doc in docs:
        doc_text = prettify(doc["text"])
        tfidf_score = 0.0
        for word in words_list:
            tf = calculate_tf(doc_text, word)
            idf = calculate_idf(docs, word)
            tfidf_score += tf * idf

        if tfidf_score > 0:
            result[doc["id"]] = tfidf_score

    sorted_results = sorted(result.items(), key=lambda item: item[1], reverse=True)
    return [doc_id for doc_id, _ in sorted_results]
