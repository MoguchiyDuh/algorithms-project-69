from search_engine.search_engine import search

doc1 = "I can't shoot straight unless I've had a pint!"
doc2 = "Don't shoot shoot shoot that thing at me."
doc3 = "I'm your shooter."
docs = [
    {"id": "doc1", "text": doc1},
    {"id": "doc2", "text": doc2},
    {"id": "doc3", "text": doc3},
]

big_docs = [
    {"id": "doc1", "text": "I love programming"},
    {"id": "doc2", "text": "programming is fun"},
    {"id": "doc3", "text": "I love fun"},
    {"id": "doc4", "text": "Learning programming is exciting"},
    {"id": "doc5", "text": "Fun with programming can lead to creativity"},
    {"id": "doc6", "text": "I enjoy programming in Python"},
    {"id": "doc7", "text": "Programming can be challenging but rewarding"},
    {"id": "doc8", "text": "Fun activities include programming contests"},
    {"id": "doc9", "text": "I love to program games"},
    {"id": "doc10", "text": "Programming is the future of technology"},
    {"id": "doc11", "text": "With programming, you can build amazing things"},
    {
        "id": "doc12",
        "text": "Programming languages make communication with computers possible",
    },
    {"id": "doc13", "text": "I prefer programming over manual tasks"},
    {"id": "doc14", "text": "Learning new programming languages is fun"},
    {"id": "doc15", "text": "I often write programs to solve problems"},
    {"id": "doc16", "text": "Python programming is very popular"},
    {"id": "doc17", "text": "The joy of programming comes from problem-solving"},
    {"id": "doc18", "text": "I attend programming workshops to improve my skills"},
    {"id": "doc19", "text": "Team programming can enhance productivity"},
    {"id": "doc20", "text": "I find programming to be an enjoyable hobby"},
    {"id": "doc21", "text": "Collaborative programming leads to innovative solutions"},
]


def test_1():
    word = "shoot"
    result = search(docs, word)
    assert result == ["doc2", "doc1"]


def test_2():
    docs1 = [{"id": "doc1", "text": doc1}]
    assert search(docs1, "pint") == ["doc1"]
    assert search(docs1, "pint!") == ["doc1"]


def test_3():
    result = search(docs, "shoot at me")
    assert result == ["doc2", "doc1"]


def test_4():
    assert search(big_docs, "python") == ["doc6", "doc16"]
    assert search(big_docs, "program") == ["doc9"]
