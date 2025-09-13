def get_num_words(string):
    words_count = len(string.split()) 

    return words_count 

def get_chars_count(string): 
    character_dict = {}

    for word in string.split():
        for char in word.lower():
            if char in character_dict:
                character_dict[char] += 1
            else:
                character_dict[char] = 1
    
    return character_dict

def get_sorted_dict(char_dict):
    dict_list = []

    def sort_on(items):
        return items["num"]

    for key, val in char_dict.items():
        item = { "name": key, "num": val }
        dict_list.append(item)
    
    dict_list.sort(key=sort_on, reverse=True) 

    return dict_list