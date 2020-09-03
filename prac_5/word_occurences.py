words_to_count = {}

user_string = input("Please enter a string: ")
words = user_string.split()
for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

words = list(words_to_count.keys())
words.sort()

longest_word = max((len(word) for word in words))

for word in words:
    print("{:{}}: {}".format(word, longest_word, words_to_count[word]))
