from lxml import etree
import csv

infile = open('uiu_uiuc-loc_20180124_uiuc_DigitalRareBookCollections_105.xml', 'rb')
xml = infile.read()
infile.close()
tree = etree.fromstring(xml)
ns = {'m': 'http://www.loc.gov/MARC21/slim'}
# get records
records = tree.xpath('//m:record', namespaces=ns)


def get_field(field_code):
    index_term = record.xpath('./m:datafield[@tag="{0}"]/m:subfield[@code = "a"]/text()'.format(field_code),namespaces=ns)
    if len(index_term) != 0:
        return index_term[0]
    else:
        return None

def get_fields(field_code):
    index_term = record.xpath('./m:datafield[@tag="{0}"]'.format(field_code), namespaces=ns)
    field_list = []
    for item in index_term:
        item_list = item.xpath('./m:subfield/text()', namespaces=ns)
        item_string = ' -- '.join(item_list)
        field_list.append(item_string)
    field = '|'.join(field_list)
    return field

header = ['ldr6', 'ldr7', 'year', 'language', 'isbn', 'scn', 'cn', 'dcn', 'author', 'corporate', 'mn', 'title', 'publication', 'production', 'pd', 'notes', 'subjects', 'geo', 'genre', 'pername', 'corporname', 'uri']


csvfile = open('dataxml.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header)

for record in records:
    data = []
    leader = record.xpath('./m:leader/text()', namespaces=ns)
    if leader is not None:
        # get type of record
        data.append(leader[0][6])
        # get bibliography level
        data.append(leader[0][7])
    else:
        type_of_record = leader
        bib_level = leader
        data.append(type_of_record)
        data.append(bib_level)

    control008 = record.xpath('./m:controlfield[@tag = "008"]/text()', namespaces=ns)
    if control008 is not None:
        # get language
        data.append(control008[0][35:38])
        # get year
        data.append(control008[0][7:11])
        # year有错，cleaning？
    else:
        data.append(None)
        data.append(None)

    data.append(get_field('020'))
    data.append(get_field('035'))
    data.append(get_field('050'))
    data.append(get_field('082'))
    data.append(get_fields('100'))
    data.append(get_fields('110'))
    data.append(get_fields('111'))
    data.append(get_field('245'))
    data.append(get_fields('260'))
    data.append(get_fields('264'))
    data.append(get_fields('300'))
    data.append(get_fields('505'))
    data.append(get_fields('650'))
    data.append(get_fields('651'))
    data.append(get_fields('655'))
    data.append(get_fields('700'))
    data.append(get_fields('710'))

    electronic_link = record.xpath('./m:datafield[@tag = "856"]/m:subfield[@code = "u"]/text()', namespaces=ns)
    if len(electronic_link) != 0:
        electronic_link = electronic_link[0]
    else:
        electronic_link.append(None)
    if control008[0][23] == 'o':
        # get 856 position
        # get electronic_link
        data.append(electronic_link[0])
    else:
        data.append(None)

    csvwriter.writerow(data)

csvfile.close()
