def word_count(string : str) -> None:
    split_string  = string.split()
    print(f"Found {len(split_string)} total words")

def count_chars(string : str) -> dict:
    string = string.lower()
    char_dict = {}
    for i in range (0, len(string)):
        if(string[i] in char_dict):
            char_dict[string[i]] +=1
        else:
            char_dict[string[i]] = 1
    return char_dict




def char_dict_to_list(char_dict : dict) -> list:
    char_list = []
    for item in char_dict:
        temp_dict = {"char":item,"num":char_dict[item]}
        char_list.append(temp_dict)
    sorted_list = char_list.sort(reverse=True,key=lambda arr : arr["num"] )
    return char_list