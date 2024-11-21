# 7. Write a python function to remove a given word from a words ad strip it at the same time


# ### MY CONFUSING CODE

# def removeWord(w,l):
#     newList = []
#     for word in l:
#         if w == word.lower().strip():
#             continue
#         newList.append(word)
#     print(newList)
            

# words = ["Hey","this","is","vivek","and","I","am","am","fine"]
# print(words)

# w = input("Enter word to remove : ")
# w = w.strip().lower()

# removeWord(w,words)



# ### CORRECTED CODE FOR THIS APPROACH, THIS IS WRONG ONE

# def remove_word(word_to_remove, words_list):
#     new_list = []
#     for word in words_list:
#         # Compare after stripping and converting to lowercase
#         if word_to_remove != word.lower().strip():
#             new_list.append(word)
#     return new_list  # Return the new list

# # Input list
# words_list = ["Hey", "this", "is", "vivek", "and", "I", "am", "am", "fine"]
# print(f"Original list: {words_list}")

# # Input word to remove
# word_to_remove = input("Enter word to remove: ").strip().lower()

# # Get the updated list
# updated_list = remove_word(word_to_remove, words_list)

# print(f"Updated list: {updated_list}")




#CORRECT CODE AND CORRECT APPROACH


def removeWord(word_to_remove, words_list):
    i=0
    while i < len(words_list):
        if words_list[i] == word_to_remove:
            print(f"Removed word : {words_list.pop(i)}")
        else:
            i+=1
    return words_list



words_list = ["Hey", "this", "is", "vivek", "and", "I", "am", "am", "fine"]
print(f"Original list: {words_list}")

# Input word to remove
word_to_remove = input("Enter word to remove: ").strip().lower()

updated_list=removeWord(word_to_remove, words_list)

print(f"Updated list: {updated_list}")