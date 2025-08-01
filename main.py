from stats import count_words, count_characters

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def main():
	num_words = count_words(get_book_text(path_to_file))
	print(f"{num_words} words found in the document")
	print(count_characters(get_book_text(path_to_file)))

path_to_file = "books/frankenstein.txt"

main()
