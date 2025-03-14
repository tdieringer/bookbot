def count_words (file_contents):
    wordcount = len(file_contents.split())
    return wordcount

def character_count (file_contents):
    characters = {}
    for char in file_contents:
        lowerchar = char.lower()
        if lowerchar in characters:
            characters[lowerchar] += 1
        else:
            characters[lowerchar] = 1
    return characters

def sort_on(characters):
    key_pairs = [{key: value} for key, value in characters.items()]
    key_pairs.sort(key=lambda d: list(d.values())[0], reverse=True)
    return key_pairs

