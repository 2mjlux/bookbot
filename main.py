import sys
from stats import count_words, count_characters, sort_on, sort_list_dict

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def main():
    
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_file = sys.argv[1]
	
	# pass data as parameters
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_list_dict(char_count)
    
    print_report(path_to_file, num_words, sorted_char_count)

def print_report(file_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_data in sorted_chars:
        if char_data["char"].isalpha():
            print(f"{char_data['char']}: {char_data['num']}")
    print("============= END ===============")

# path_to_file = "books/frankenstein.txt"

main()
