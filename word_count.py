import docx, re
from docx import Document

file = input("Enter file name:")
target = input("Enter word:")
fopen = open(file, "rb")
docu = Document(fopen)
count = 0
pattern = re.compile('[\W_]+')
for para in docu.paragraphs:
    content = para.text
    for word in content.split():
        word = word.lower()
        word = pattern.sub('', word)
        if target == word:
            count+=1
print(count)

