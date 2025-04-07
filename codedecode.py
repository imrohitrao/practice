paragraph = input("Enter a paragraph: ")
#Split the paragraph into words and store in a list
words_list = paragraph.split()
print("List of words:")

for words in words_list:
    for characters in words:
        firstchar=characters[0]
        print(firstchar)



