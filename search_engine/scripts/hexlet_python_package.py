import os
import sys

sys.path.append(os.path.abspath("D:\\algorithms-project-69\\"))
from search_engine.search_engine import search
from tests.test_search_engine import docs


def main():
    """Run an example code."""
    word = "shoot at me, nerd"

    result = search(docs, word)
    print(result)


if __name__ == "__main__":
    main()
