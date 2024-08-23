str = str(input("Введіть довільне речення: \n"))
words = str.split()
uniq_words = set()

for word in words: 
    uniq_words.add(word)
print("Унікальні слова у введенному речені:")
for uni_word in uniq_words :
    print(uni_word, end=" ")
