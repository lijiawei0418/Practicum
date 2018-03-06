from pymarc import MARCReader

def get_field(field_code):
    if record[field_code] is None:
        print(field_code, ':', 'None')
    else:
        print(field_code, ':', record[field_code]['a'])


def get_fields(field_code):
    fields = record.get_fields(field_code)
    if fields == []:
        print(field_code, ':', 'None')
    else:
        l_list = []
        for data in fields:
            data_list = str(data).split('$')
            d_list = []
            for d in data_list[1:]:
                d_list.append(d[1:])
            l_list.append((' -- ').join(d_list))
        print(field_code, ':', ('|').join(l_list))


fh = open('/Users/lijiawei/Desktop/full_vufind3_export_for_UIU_20171016170000.mrc', 'rb')
read = MARCReader(fh)
i = 0
for record in read:
    # get leader position
    leader_position = record.leader
    if leader_position is not None:
        print('LDR[6]:', record.leader[6])
        print('LDR[7]:', record.leader[7])
    else:
        print('LDR[6]:', 'None')
        print('LDR[7]:', 'None')

    # get 008 position
    eighth_position = str(record['008'])[6:]
    if eighth_position is not None:
        print('008[7:10]:', eighth_position[7:11])
        print('008[35:37]:', eighth_position[35:38])
    else:
        print('008[7:10]:', 'None')
        print('008[35:37]:', 'None')

    get_field('20')
    get_field('35')
    get_field('50')
    get_field('82')
#     print(record['100'])
    get_fields('100')
    get_fields('110')
    get_fields('111')
    get_field('245')
    get_fields('260')
    get_fields('264')
    get_fields('300')
    get_fields('505')
    get_fields('650')
    # print(record['650'])
    get_fields('651')
#     print(record['651']['a'],'--',record['651']['v'])
    get_fields('655')
    get_fields('700')
    get_fields('710')
    if eighth_position is not None:
        if (eighth_position[23] == 'o'):
            get_fields('856')

