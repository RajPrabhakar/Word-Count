import docx, re
from docx import Document

file = 'pap.docx'
target = [['method', 'program', 'feasibility', 'engineering', 'rahul', 'lax'],
          ['network', 'security', 'cryptography', 'encryption', 'decryption'],
          ['machine learning', 'nlp', 'neural', 'deep learning', 'robotics', 'automation'],
          ['database', 'query', 'records', 'tables', 'sql', 'oracle']]
domain_total = [[0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
domain = ['Mathematics', 'Communication', 'A.I', 'Database']
word_count = 0
fopen = open(file, "rb")
docu = Document(fopen)
pattern = re.compile('[\W_]+')
for para in docu.paragraphs:
    content = para.text
    for word in content.split():
        word = word.lower()
        word = pattern.sub('', word)
        dom_count = 0
        for out_list in target:
            key_count = 0
            for in_list in out_list:
                if in_list == word:
                    domain_total[dom_count][key_count]+=1
                key_count+=1
            dom_count+=1
        word_count+=1
print(word_count)
for i in range(4):
    for j in range(len(target[i])):
        print(domain[i], " : ", target[i][j], " : ", domain_total[i][j])
    

