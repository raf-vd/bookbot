def main():

    # Read book & create statistics
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_chars_in_string(text)
    list_of_char_dicts = convert_char_dict_to_list_of_char_dict(char_dict)
    list_of_char_dicts.sort(reverse=True, key=sort_on)
    
    # Output statistics
    print("\n--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    print_letter_count(list_of_char_dicts)
    print("---End of report ---\n")


def print_letter_count(dict_list):
    for entry in dict_list:
        if entry["character"].isalpha():
            print(f"The '{entry["character"]}' character was found {entry["aantal"]} times")

def sort_on(dict):
    return dict["aantal"]
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_chars_in_string(text):
    dict_out = {}
    for c in text:
        lcase_c = c.lower()
        if lcase_c in dict_out:
            dict_out[lcase_c] += 1
        else:
            dict_out[lcase_c] = 1
    return dict_out

def convert_char_dict_to_list_of_char_dict(char_dict):
    dict_list = []
    for c in char_dict:
        dict_list.append({"character" : c, "aantal" : char_dict[c]})
    return dict_list


main()