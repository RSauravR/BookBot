def get_total_word_count(text):
    return len(text.split())

def character_appearing_calculator(text):
    lowered_text = text.lower()
    char_dict = {}
    for char in lowered_text:
        char_dict[char] = char_dict.get(char,0) + 1
    return  char_dict

def sort_on(items):
    return items["count"]

def sorted_character_appearing_calculator(char_dict):
    char_list = [{'char': k, 'count': v} for k, v in char_dict.items()]
    char_list1 = sorted(char_list,reverse=True, key=sort_on)
    return char_list1