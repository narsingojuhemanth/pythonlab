text_file = open('data.txt', 'r')
text = text_file.read()
print(text)
#cleaning
text = text.lower()
print(text)

words = text.split()
print(words)

words = [word.strip('.,!;()[]') for word in words]
print(words)

words = [word.replace("'s", '') for word in words]
print(words)

#finding unique
unique = []
for word in words:
 if word not in unique:
    unique.append(word)
#sort
unique.sort()
#print
print(unique)