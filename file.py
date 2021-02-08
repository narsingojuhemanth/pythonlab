# open both files
with open('first.txt','r') as firstfile, open('second.txt','w') as secondfile:

 # read content from first file
    for line in firstfile:
    # append content to second file
        secondfile.write(line)
print("Content of second file copied to first file successfully")