from search_engine.search_engine import search
from tests.test_search_engine import docs


def main():
    """Run an example code."""
    word = "shoot"

    result = search(docs, word)
    print(result)


if __name__ == "__main__":
    main()
