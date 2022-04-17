stop_words_file = re.findall(r'\b\w+\b',open('stop-words.txt').read().lower())
len(stop_words_file)
# 444
# list currently includes the commented out lines


import re
name = 'propane'
a = []
Alkane = list(map(lambda m: tuple(filter(bool, m)), re.findall('(\d+\W+)*(methyl|ethyl|propyl|butyl)*(meth|eth|prop|but|pent|hex)(ane)', name)))
if Alkane != a:
    print(Alkane)


        rexp = re.compile(r'\b\w+\b')
stop_words_file = []

with open('stop-words.txt', 'r') as text_file:
    string_to_parse = ''
    for line in text_file.readlines(5069):
        string_to_parse = string_to_parse + line
        for string_to_parse:
            stop_words_file.append(string_to_parse)

print(string_to_parse)

for target in file_name_list:
    string_to_parse = ''
    with open(target,'r',encoding='utf-8', errors='ignore') as text_file:
        for i in text_file.readlines(5096):
            string_to_parse = string_to_parse + i
            mp3_filename = target.replace('.txt','.mp3')
            fullPath = os.path.join(os.getcwd(), mp3_filename)
            engine.save_to_file(string_to_parse, fullPath)
            engine.runAndWait()
