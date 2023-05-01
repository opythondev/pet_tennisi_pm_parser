import re
from add_lines_regexp import volley_ou, volley_f_f


def add_line_type_1(market_list, period, sport, ht_name, at_name):
    markets = []
    if len(market_list) == 0:
        pass
    else:
        pass
    return markets


def add_line_type_2(market_list, period, sport, ht_name, at_name):
    markets = []
    if len(market_list) == 0:
        pass
    else:
        pass
    return markets


def add_line_type_3(market_list, period, ht_name, at_name):
    markets = []
    if len(market_list) == 0:
        pass
    else:
        total = re.compile('.*(Т|т)отал.*')
        fora = re.compile('.*форой.*')

        total_list = list(filter(total.match, market_list))
        for t in total_list:
            total_list_tmp = re.split(r'&nbsp;', t)
            if len(total_list_tmp) != 4:
                print(f'F_F, tennis, add_line_type_3, err in {t}')
            else:
                t_t_t = volley_ou(total_list_tmp, period, ht_name, at_name)
                markets.extend(t_t_t)

        fora_list = list(filter(fora.match, market_list))
        for i in fora_list:
            fora_list_tmp = re.split(r'&nbsp;', i)
            if len(fora_list_tmp) != 6:
                print(f'F_F, volley, add_line_type_4, err in {t}')
            else:
                f_f_f = volley_f_f(fora_list_tmp, period)
                markets.extend(f_f_f)
    return markets


# 'volleyball', 'e-volleyball', 'e-other'
def add_line_type_4(market_list, period, ht_name, at_name):
    markets = []
    if len(market_list) == 0:
        pass
    else:
        total = re.compile('.*(Т|т)отал.*')
        fora = re.compile('.*форой.*')

        total_list = list(filter(total.match, market_list))
        for t in total_list:
            total_list_tmp = re.split(r'&nbsp;', t)
            if len(total_list_tmp) != 4:
                print(f'F_F, volley, add_line_type_4, err in {t}')
            else:
                t_t_t = volley_ou(total_list_tmp, period, ht_name, at_name)
                markets.extend(t_t_t)

        fora_list = list(filter(fora.match, market_list))
        for i in fora_list:
            fora_list_tmp = re.split(r'&nbsp;', i)
            if len(fora_list_tmp) != 6:
                print(f'F_F, volley, add_line_type_4, err in {t}')
            else:
                f_f_f = volley_f_f(fora_list_tmp, period)
                markets.extend(f_f_f)

    return markets


