def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    #count_char(file_contents)
    report(file_contents)

    
    
    

def count_words(book):
    words = book.split()
    print(len(words))
    return(len(words))


def count_char(book):
    my_string = book.lower()
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    print(alphabet)

    char_dict = {}
    for char in alphabet:
        char_dict[char] = 0


    for char in my_string:
        try:
            char_dict[char] += 1
        except Exception:
            pass
        

    print(str(char_dict))
    return(char_dict)

def report(book):
    
    word_count = count_words(book)

    char_dict = count_char(book)

    dict_list = []

    for char in char_dict:
        dict_list.append({"character": char, "number": char_dict[char]})
    
    def sort_on(dict):
        return dict["number"]

    dict_list.sort(reverse=True, key=sort_on)

    print(
        f"""--- Begin report of books/frankenstein.txt ---
{word_count} words found in the document
        """
    )

    for entry in dict_list:
        print(f"The {entry["character"]} character was found {entry["number"]} times" )

main()