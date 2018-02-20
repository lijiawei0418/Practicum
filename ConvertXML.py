from lxml import etree
infile = open('/Users/lijiawei/Desktop/uiu_uiuc-loc_20180124_uiuc_DigitalRareBookCollections_105.xml', 'rb')
xml = infile.read()
infile.close()
tree = etree.fromstring(xml)
ns = {'m': 'http://www.loc.gov/MARC21/slim'}
# get records
records = tree.xpath('//m:record', namespaces=ns)


def xpath_function(path):
    result = record.xpath(path, namespaces=ns)
    if len(result) == 0:
        return None
    else:
        return result[0]


all_info = []
for record in records:
    book_info = []
    # get leader position
    leader = xpath_function('./m:leader/text()')
    if leader != 'na':
        # get type of record
        type_of_record = leader[6]
        # get bibliography level
        bib_level = leader[7]
    else:
        type_of_record = leader
        bib_level = leader
    book_info.append(type_of_record)
    book_info.append(bib_level)

    # get 008 position
    control008 = xpath_function('./m:controlfield[@tag = "008"]/text()')
    if control008 != 'na':
        # get language
        language = control008[35:38]
        # get year
        year = control008[7:11]
        # year有错，cleaning？

        if control008[23] == 'o':
            # get 856 position
            # get electronic_link
            electronic_link = xpath_function('./m:datafield[@tag = "856"]/m:subfield[@code = "u"]/text()')
            book_info.append(electronic_link)
        else:
            electronic_link = 'na'
    else:
        language = control008
        year = control008
        electronic_link = control008
    book_info.append(year)
    book_info.append(language)
    book_info.append(electronic_link)

    # get ISBN
    isbn = xpath_function('./m:datafield[@tag = "020"]/m:subfield[@code = "a"]/text()')
    book_info.append(isbn)

    # get 035 position
    # get system control number
    system_control_nums = xpath_function('./m:datafield[@tag = "035"]/m:subfield[@code = "a"]/text()')
    book_info.append(system_control_nums)
    # 是否删掉OCOLC

    # get 082 position
    # get dewey decimal
    dewey_dec = xpath_function('./m:datafield[@tag = "082"]/m:subfield[@code = "a"]/text()')
    book_info.append(dewey_dec)

    # get 100 position
    # get personal name
    personal_name = xpath_function('./m:datafield[@tag = "100"]/m:subfield[@code = "a"]/text()')
    book_info.append(personal_name)

    # get 110 position
    # get Corporate name
    corporate_name = xpath_function('./m:datafield[@tag = "110"]/m:subfield[@code = "a"]/text()')
    book_info.append(corporate_name)

    # get 111 position
    # get meeting name
    meeting_name = xpath_function('./m:datafield[@tag = "111"]/m:subfield[@code = "a"]/text()')
    book_info.append(meeting_name)

    # get 245 position
    # get title
    title = xpath_function('./m:datafield[@tag = "245"]/m:subfield[@code = "a"]/text()')
    book_info.append(title)

    # get 260 position
    # get publication place
    publication_place = xpath_function('./m:datafield[@tag = "260"]/m:subfield[@code = "a"]/text()')
    book_info.append(publication_place)

    # get 260 position
    # get publisher name
    publisher_name = xpath_function('./m:datafield[@tag = "260"]/m:subfield[@code = "b"]/text()')
    book_info.append(publisher_name)

    # get 260 position
    # get publication date
    publication_date = xpath_function('./m:datafield[@tag = "260"]/m:subfield[@code = "c"]/text()')
    book_info.append(publication_date)

    # get 264 position
    # get production place
    producation_place = xpath_function('./m:datafield[@tag = "264"]/m:subfield[@code = "a"]/text()')
    book_info.append(producation_place)

    # get 264 position
    # get producer name
    producer_name = xpath_function('./m:datafield[@tag = "264"]/m:subfield[@code = "b"]/text()')
    book_info.append(producer_name)

    # get 264 position
    # get producation date
    producation_date = xpath_function('./m:datafield[@tag = "264"]/m:subfield[@code = "c"]/text()')
    book_info.append(producation_date)

    # get 300 position
    # get extent
    extent = xpath_function('./m:datafield[@tag = "300"]/m:subfield[@code = "a"]/text()')
    book_info.append(extent)

    # get 300 position
    # get physical_detail
    physical_detail = xpath_function('./m:datafield[@tag = "300"]/m:subfield[@code = "b"]/text()')
    book_info.append(physical_detail)

    # get 300 position
    # get dimensions
    dimensions = xpath_function('./m:datafield[@tag = "300"]/m:subfield[@code = "c"]/text()')
    book_info.append(dimensions)

    # get 505 position
    # get formatted contents note
    contents_note = xpath_function('./m:datafield[@tag = "505"]/m:subfield[@code = "a"]/text()')
    book_info.append(contents_note)

    # get 650 position
    # get subject_access
    subject_access = xpath_function('./m:datafield[@tag = "650"]/m:subfield[@code = "a"]/text()')
    book_info.append(physical_detail)

    # get 651 position
    # get geographic_name
    geographic_name = xpath_function('./m:datafield[@tag = "651"]/m:subfield[@code = "a"]/text()')
    book_info.append(geographic_name)

    # get 655 position
    # get index_term (need more details)
    index_term = xpath_function('./m:datafield[@tag = "655"]/m:subfield[@code = "a"]/text()')
    book_info.append(index_term)

    # get 700 position
    # get personal name
    personal_name = xpath_function('./m:datafield[@tag = "700"]/m:subfield[@code = "a"]/text()')
    book_info.append(personal_name)

    # get 710 position
    # get corporate name (corporate_name1)
    corporate_name1 = xpath_function('./m:datafield[@tag = "710"]/m:subfield[@code = "a"]/text()')
    book_info.append(corporate_name1)



    all_info.append(book_info)

print(all_info)
