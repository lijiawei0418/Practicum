import re
file = open('uiu_ia-uiuc_20171002-unique-with856.mrk', 'r', encoding='utf8')
lines = file.read()
records = lines.split('\n\n')
records = records[:-1]

def get_info(anystr):
    p = re.compile(anystr)
    i_list = p.findall(record)
    if len(i_list) == 0:
        return [None]
    else:
        return i_list

str_list = ['=035.*\$a(.*?)\s','=050.*\$a(.*?)\s','=082.*\$a(.*?)\s','=100.*\$a(.*?)\$','=110.*\$a(.*?)\s',
            '=111.*\$a(.*?)\s','=245.*\$a(.*?)\$',
            '=260.*\$a(.*?)\s','=260.*\$b(.*?)\s','=260.*\$c(.*?)\s',
            '=264.*\$a(.*?)\s','=264.*\$b(.*?)\s','=264.*\$c(.*?)\s','=300.*\$a(.*?)\s','=300.*\$b(.*?)\s',
            '=300.*\$c(.*?)\s','=260.*\$c(.*?)\s','=505.*\$a(.*?)\s','=650.*\$a(.*?)\.','=651.*\$a(.*?)\s',
            '=655.*\$a(.*?)\s','=700.*\$a(.*?)\s','=710.*\$c(.*?)\s']

books_info = []
for record in records:
    book_info = []
    p = re.compile('=LDR\s\s(.*)')
    book_info += [p.findall(record)[0][6]]
    book_info += [p.findall(record)[0][7]]
    p = re.compile('=008\s\s(.*)')
    book_info += [p.findall(record)[0][7:11]]
    if p.findall(record)[0][23] == 'o':
        info = get_info('=856.*\$u(.*?)$')
        book_info += info
    else:
        book_info += [None]
    for string in str_list:
        info = get_info(string)
        book_info += info
#     print(book_info)
    books_info.append(book_info)

print(books_info)



