import re


def volley_f_f(fora_list_tmp, period):
    fora = []
    set_f = ''
    if 'по сетам' in fora_list_tmp[0]:
        set_f = 'SET_'
    f_f1_p = re.findall(r'id="p">(.*)<.a>', fora_list_tmp[1])
    f_f1_v = re.findall(r'id="p">(.*)<.a>', fora_list_tmp[2])
    f_f1 = 'F-F1'
    f1_type = set_f+f_f1
    fora.append({'param': float(f_f1_p[0]), 'period': period, 'type': f1_type, 'value': f_f1_v[0]})

    f_f2_p = re.findall(r'id="p">(.*)<.a>', fora_list_tmp[4])
    f_f2_v = re.findall(r'id="p">(.*)<.a>', fora_list_tmp[5])
    f_f2 = 'F-F2'
    f2_type = set_f+f_f2
    fora.append({'param': float(f_f2_p[0]), 'period': period, 'type': f2_type, 'value': f_f2_v[0]})

    return fora


def volley_ou(total_list_tmp, period, ht_name, at_name):
    total = []
    if len(total_list_tmp) != 4:
        print(f'OU, volley_cyber, err')
        pass
    else:
        param = total_list_tmp[2]
        param_val = param
        if param == '':
            param_val = ''
        else:
            param_val = float(param)

        uo_to_base = 'OU-'
        uo_tu_type = 'TU'
        uo_to_type = 'TO'
        if ht_name in total_list_tmp[0]:
            uo_to_base = 'OU1-'
        elif at_name in total_list_tmp[0]:
            uo_to_base = 'OU2-'
        elif 'по сетам' in total_list_tmp[0]:
            uo_to_base = 'SET_OU-'
        elif 'нечет' in total_list_tmp[0]:
            uo_to_base = 'OE-'
            uo_tu_type = 'EVEN'
            uo_to_type = 'ODD'

        uo_tu = re.findall(r'id="p">(.*)<.a>', total_list_tmp[1])
        type_tu = uo_to_base+uo_tu_type
        total.append({'param': param_val, 'period': period, 'type': type_tu, 'value': uo_tu[0]})
        uo_to = re.findall(r'id="p">(.*)<.a>', total_list_tmp[3])
        type_to = uo_to_base + uo_to_type
        total.append({'param': param_val, 'period': period, 'type': type_to, 'value': uo_to[0]})

    return total
