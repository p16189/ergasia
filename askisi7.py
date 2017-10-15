words = input('Give words : ')
words2 = words.split(" ")

max_len = 0
max_word = words2[0]
for d in words2:
    if (len(d) >= max_len):
        max_len = len(d)
        max_word = d

print (max_word)
