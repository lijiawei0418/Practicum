from pymarc import MARCReader
import csv

def get_field(field_code):
    if record[field_code] is None:
        return None
        # print(field_code, ':', 'None')
    else:
        return record[field_code]['a']
        # print(field_code, ':', record[field_code]['a'])


def get_fields(field_code):
    fields = record.get_fields(field_code)
    if fields == []:
        return None
        # print(field_code, ':', 'None')
    else:
        l_list = []
        for data in fields:
            data_list = str(data).split('$')
            d_list = []
            for d in data_list[1:]:
                d_list.append(d[1:])
            l_list.append((' -- ').join(d_list))
        return ('|').join(l_list)
        # print(field_code, ':', ('|').join(l_list))


fh = open('uiu_ia-uiuc_20171002-unique-with856.mrc', 'rb')

read = MARCReader(fh,force_utf8=True, to_unicode=True, hide_utf8_warnings=True, utf8_handling='ignore')

header = ['ldr6', 'ldr7', 'year', 'language', '20', '35', '50', '82', '100', '110', '111', '245', '260', '264', '300', '505', '650', '651', '655', '700', '710', '856']

csvfile = open('data.csv', 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(header)







for record in read:
    data = []
    # get leader position
    leader_position = str(record.leader)
    # print("!!!",leader_position)
    if leader_position is not None:
        data.append(record.leader[6])
        data.append(record.leader[7])
        # print('LDR[6]:', record.leader[6])
        # print('LDR[7]:', record.leader[7])
    else:
        data.append(None)
        data.append(None)
        # print('LDR[6]:', 'None')
        # print('LDR[7]:', 'None')

    # get 008 position
    eighth_position = str(record['008'])[6:]
    if eighth_position is not None:
        # print(eighth_position)
        data.append(eighth_position[7:11])
        data.append(eighth_position[35:38])
        # print('008[7:10]:', eighth_position[7:11])
        # print('008[35:37]:', eighth_position[35:38])
    else:
        data.append(None)
        data.append(None)
        # print('008[7:10]:', 'None')
        # print('008[35:37]:', 'None')

    data.append(get_field('20'))
    data.append(get_field('35'))
    data.append(get_field('50'))
    data.append(get_field('82'))
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




    # get_field('20')
    # get_field('35')
    # get_field('50')
    # get_field('82')
    # get_fields('100')
    # get_fields('110')
    # get_fields('111')
    # get_field('245')
    # get_fields('260')
    # get_fields('264')
    # get_fields('300')
    # get_fields('505')
    # get_fields('650')
    # get_fields('651')
    # get_fields('655')
    # get_fields('700')
    # get_fields('710')
    if eighth_position is not None:
        if (eighth_position[23] == 'o'):
            data.append(get_fields('856'))
            # get_fields('856')

    csvwriter.writerow(data)

csvfile.close()