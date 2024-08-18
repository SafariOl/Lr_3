str = str(input("Введіть довільне речення: \n"))
words = str.split()
uniq_words = set()

for word in words: 
    uniq_words.add(word)

print(uniq_words)
