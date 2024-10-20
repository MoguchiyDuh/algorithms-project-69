from search_engine.search_engine import search


def test_1():
    doc1 = "I can't shoot straight unless I've had a pint!"
    doc2 = "Don't shoot shoot shoot that thing at me."
    doc3 = "I'm your shooter."

    docs = [
        {"id": "doc1", "text": doc1},
        {"id": "doc2", "text": doc2},
        {"id": "doc3", "text": doc3},
    ]
    word = "shoot"

    result = search(docs, word)
    assert result == ["doc1", "doc2"]


def test_2():
    doc1 = {"id": "doc1", "text": "I can't shoot straight unless I've had a pint!"}
    docs = [doc1]

    assert search(docs, "pint") == ["doc1"]
    assert search(docs, "pint!") == ["doc1"]
