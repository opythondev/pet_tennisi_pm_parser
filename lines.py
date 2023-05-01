from line import *
from add_lines import add_line_type_1, add_line_type_2, add_line_type_3, add_line_type_4

sport_periods = {
    'soccer': 'FT',
    'hockey': 'FT',
    'tennis': 'MATCH',
    'volleyball': 'FT',
    'basketball': 'MATCH',
    'baseball': 'FT',
    'handball': 'FT',
    'e-soccer': 'FT',
    'e-hockey': 'FT',
    'e-tennis': 'MATCH',
    'e-volleyball': 'FT',
    'e-basketball': 'MATCH',
    'e-other': 'FT'
}

periods = {
    '1-я карта': '1M',
    '2-я карта': '2M',
    'Первый тайм': '1H',
    'Второй тайм': '2H',
    '1-й сет': '1S',
    '1-я половина': '1H',
    '2-я половина': '2H',
    '1-я четверть': '1Q',
    '2-я четверть': '2Q',
    '3-я четверть': '3Q',
    '4-я четверть': '4Q',
    '1-й период': '1P',
    '2-й период': '2P',
    '3-й период': '3P',
}


def data_cleaner(part):
    c_part = re.sub(r'.*\n.*\n.*\n<TD ALIGN=left.*\n<.TD>', '', str(part))
    c_part = re.sub(r'<TD.*bgcolor.*<.TD>', '', str(c_part))
    c_part = re.sub(r'<TR ALIGN="center".*', '', str(c_part))
    c_part = re.sub(r'<TD ALIGN=left COLSPAN=.*', '', str(c_part))
    return c_part


def data_splitter(part):
    l_part = re.split('<tr valign=top>', str(part))
    l_part.pop(0)

    return l_part


# main lines for tr align=center
def line_center(part, period, sport):
    if sport in ('basketball', 'baseball', 'e-basketball'):
        chunk = line_type_1(part, period, sport)

    elif sport in ('soccer', 'e-soccer', 'hockey', 'handball', 'e-hockey'):
        chunk = line_type_2(part, period, sport)

    elif sport in ('tennis', 'e-tennis'):
        chunk = line_type_3(part, period, sport)

    elif sport in ('volleyball', 'e-volleyball'):
        chunk = line_type_4(part, period, sport)

    elif sport in 'e-other':
        chunk = line_type_5(part, period, sport)

    else:
        chunk = ''
    return chunk


# additional lines for tr align=left
def line_left(part, period, sport, ht_name, at_name):
    market_list = data_splitter(part)
    if sport in ('basketball', 'baseball', 'e-basketball'):
        chunk = add_line_type_1(market_list, period, ht_name, at_name)

    elif sport in ('soccer', 'e-soccer', 'hockey', 'handball', 'e-hockey'):
        chunk = add_line_type_2(market_list, period, ht_name, at_name)

    elif sport in ('tennis', 'e-tennis'):
        chunk = add_line_type_3(market_list, period, ht_name, at_name)

    elif sport in ('volleyball', 'e-volleyball', 'e-other'):
        chunk = add_line_type_4(market_list, period, ht_name, at_name)

    else:
        chunk = ''
    return chunk


def get_lines(format_g, sport, ht_name, at_name):
    lines = []
    part_line = re.split('</TR>\n<TR ALIGN=', format_g)
    curr_period = ''
    for index, part in enumerate(part_line):
        if index == 0:
            line_format = re.findall(r'^<tr align="([a-z]*)', part)
            line_format = line_format[0]
            if line_format == 'center':
                curr_period = sport_periods.get(sport)
                cleaned_part = data_cleaner(part)
                outcomes = line_center(cleaned_part, curr_period, sport)
                lines.extend(outcomes)
            elif line_format == 'left':
                period = curr_period
                outcomes = line_left(part, period, sport, ht_name, at_name)
                lines.extend(outcomes)
            else:
                skip = True
        else:
            line = f'<TR ALIGN={part}'
            line_format = re.findall(r'^<TR ALIGN="([a-z]*)', line)
            line_format = line_format[0]
            if line_format == 'center':
                find_period = re.findall(r'<TD ALIGN=left.*>(.*)<.TD>', line)
                curr_period_raw = re.sub('&nbsp;', '', find_period[0])
                curr_period_raw.strip()
                curr_period = periods.get(curr_period_raw)
                if curr_period is None:
                    skip = True
                else:
                    cleaned_part = data_cleaner(line)
                    outcomes = line_center(cleaned_part, curr_period, sport)
                    lines.extend(outcomes)
            elif line_format == 'left':
                period = curr_period
                outcomes = line_left(part, period, sport, ht_name, at_name)
                lines.extend(outcomes)
            else:
                skip = True
    return lines

