def count_words(text):
	return len(text.split())
	
def count_characters(text):
	lower_text = text.lower()
	char_count = {}
	for char in lower_text:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1
	return char_count
		
