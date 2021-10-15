line = input().lower().split()
word_counts = {}

for word in line:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for key, value in word_counts.items():
    print(key, value)
