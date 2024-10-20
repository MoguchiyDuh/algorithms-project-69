from search_engine.search_engine import search, reverse_index

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."
docs = [
    {"id": "doc1", "text": doc1},
    {"id": "doc2", "text": doc2},
    {"id": "doc3", "text": doc3},
]


def test_1():
    word = "shoot"
    result = search(docs, word)
    assert result == ["doc2", "doc1"]


def test_2():
    docs2 = [{"id": "doc1", "text": doc1}]
    assert search(docs2, "pint") == ["doc1"]
    assert search(docs2, "pint!") == ["doc1"]


def test_3():
    result = search(docs, "shoot at me")
    assert result == ["doc2", "doc1"]


def test_4():
    doc1 = {"id": "doc1", "text": "some text"}
    doc2 = {"id": "doc2", "text": "some text too"}
    docs = [doc1, doc2]
    index = {"some": ["doc1", "doc2"], "text": ["doc1", "doc2"], "too": ["doc2"]}
    assert reverse_index(docs) == index
