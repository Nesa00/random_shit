# def get_characters_in_range():
#   """
#   This function generates a list of characters from a specified Unicode code block.
#   """
#   characters = []
#   for char_code in range(0x4E00, 0x9FFF):
#     characters.append(chr(char_code))
#   return characters

# chinese_chars = get_characters_in_range()

# # Print the first 10 characters for reference
# print(f"Sample characters: {chinese_chars}")
# print(f"Number of characters: {len(chinese_chars)}")

# # You can access all characters in the list:
# # print(chinese_chars)  # This might output a large number of characters


# https://www.khngai.com/chinese/charmap/tbluni.php?page=0

characters = [chr(i) for i in range(0x4E00, 0x9FFF)]
# print(characters)
# print(len(characters))
