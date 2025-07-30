name = "vijay dinanath chouhan"
word_list = name.split()  # ['vijay', 'dinanath', 'chouhan']

for word in word_list:
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    print(reversed_word, end=" ")
