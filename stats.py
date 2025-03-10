def word_count(book_text):
    all_words = book_text.split()
    word_count = len(all_words)
    return word_count

def char_count(text):
    char_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else:
            char_dict[lowered_char] = 1
    return char_dict

def chars_to_sorted_list(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        char_info = {"char": char, "count": count}
        chars_list.append(char_info)

    def sort_on (dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)

    return chars_list
