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
	
def sort_on(items):
    return items["num"]	
		
def sort_list_dict(char_dict):
	list_char_dict = []
	for char, num in char_dict.items():
		list_char_dict.append({"char": char, "num": num})
	list_char_dict.sort(reverse=True, key=sort_on)
	return list_char_dict

