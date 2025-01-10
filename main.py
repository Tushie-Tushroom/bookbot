def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    total_words = word_count(file_contents)
    char_dict = character_count(file_contents)

    char_list = []
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    char_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")

    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['num']} times")

    print("--- End Report ---")
    
main()




'''
This is the solution to the bookbot so far in the course.
Study the differences.

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

'''