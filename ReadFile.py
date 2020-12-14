#name = input('enter file: ')

name = "F:\TMP\myFile.txt"
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

# print(counts.__str__())


bigcount = None
bigword = None
for words in counts.items():
   # print(words)
    count = words[1]
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(str(bigword) + " - " + str(bigcount))
