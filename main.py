def get_book_text (filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_words
from stats import character_count
from stats import sort_on

def main():
    import sys
    inputs = sys.argv
    if len(inputs) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        file_contents = get_book_text(filepath)
        wordcount = count_words(file_contents)
        characters = character_count(file_contents)
        sorted_list = sort_on(characters)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {wordcount} total words")
        print("--------- Character Count -------")
        for d in sorted_list:
            for key in d:
                if key.isalpha() == True:
                    print(f"{key}: {d[key]}")
        print("============= END ===============")

main()