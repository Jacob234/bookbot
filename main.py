def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)
    count_char(file_contents)


    
    
    

def count_words(book):
    words = book.split()
    print(len(words))


def count_char(book):
    my_string = book.lower()

    char_dict = {}

    for char in my_string:
        char_dict[char] =  char_dict.get(char, 0) + 1

    print(str(char_dict))

main()