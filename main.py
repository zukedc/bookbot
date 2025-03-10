import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

from stats import word_count, char_count, chars_to_sorted_list

def main():
    book_text = get_book_text(path)  # Use path here, not filepath
    total_words = word_count(book_text)
    chars = char_count(book_text)
    chars_sorted = chars_to_sorted_list(chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")  # And here too
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in chars_sorted:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()