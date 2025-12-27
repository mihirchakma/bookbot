def get_num_words(text):
    # Split the text into words based on whitespace
    words = text.split()
    return len(words)

def get_chars_dict(text):
    # Create a dictionary to hold character counts
    character_count_dict = {}

    # Iterate through each character in the text
    for char in text.lower():
        # If the character is already in the dictionary, increment its count
        if char in character_count_dict:
            character_count_dict[char] += 1
        else:
            character_count_dict[char] = 1    
    return character_count_dict

def sort_chars_by_count(char_count_dict):
    # Convert the dictionary to a list of dictionaries
    char_count_list = [{"char": char, "num": count} for char, count in char_count_dict.items()]

    # Define a helper function to get the count for sorting
    def get_count(item):
        return item["num"]

    # Sort the list in descending order based on the count
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list
