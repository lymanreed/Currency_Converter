phrase = input()
first = phrase.find("old")
last = phrase.rfind("old")
print(first if first > last else last)
