from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from io import TextIOWrapper


def displaywords() -> None:
    file: TextIOWrapper = open("story.txt", "r")
    for line in file:
        for word in line.split():
            if len(word) < 4:
                if not word.isalpha():
                    continue
                print(word, end=" ")


displaywords()
