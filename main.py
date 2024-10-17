with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def count(text):
    words = text.split()
    return len(words)

word_count = count(file_contents)

def count_char(text):
    chars = {}

    low = text.lower()

    for char in low:
            
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    return chars
    

def sort_on(dict):
    return dict["count"]



def report(dict):

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    list_of_dict = [
        {"character": char, "count": count} 
        for char, count in dict.items() if char.isalpha()
    ]

    list_of_dict.sort(reverse=True, key=sort_on)

    for char in list_of_dict:
        print(f"The '{char['character']}' character was found {char['count']} times")
        


report(count_char(file_contents))
