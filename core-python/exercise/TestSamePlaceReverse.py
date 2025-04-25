name = "vijay dinanath chouhan"
words = name.split()  # ['vijay', 'dinanath', 'chouhan']

for word in words:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")