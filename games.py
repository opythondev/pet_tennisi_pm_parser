import re
from datetime import datetime
from lines import get_lines

g_names_exceptions = ('хозяева', 'гости', 'серия', 'итоги', 'на турнире', 'левые', 'правые')

add_data_chars = ('(', ')')

months = {
    'Января': '01',
    'Февряля': '02',
    'Марта': '03',
    'Апреля': '04',
    'Мая': '05',
    'Июня': '06',
    'Июля': '07',
    'Августа': '08',
    'Сенября': '09',
    'Октября': '10',
    'Ноября': '11',
    'Декабря': '12'
}

mods = {
    'Фолы': 'FOUL',
    # 'Эйсы': 'ACE', лютый гемор
    'ЖК': 'YC',
    'Удары в створ': 'SHOT',
    'Офсайды': 'OFS',
    'Угловые': 'CRN',
}

series = ('Счёт серии', 'Счет серии')

sport_dict = {
    'футбол': 'soccer',
    'хоккей': 'hockey',
    'теннис': 'tennis',
    'волейбол': 'volleyball',
    'баскетбол': 'basketball',
    'бейсбол': 'baseball',
    'пляжный волейбол': 'volleyball',
    'кунг-волейбол': 'volleyball',
    'шорт-хоккей': 'hockey',
    'гандбол': 'handball',
    # 'киберфутбол': 'e-soccer',
    # 'киберхоккей': 'e-hockey',
    # 'кибертеннис': 'e-tennis',
    # 'киберволейбол': 'e-volleyball',
    # 'кибербаскетбол': 'e-basketball',
    'e-футбол': 'e-soccer',
    'e-хоккей': 'e-hockey',
    'e-теннис': 'e-tennis',
    'e-волейбол': 'e-volleyball',
    'e-баскетбол': 'e-basketball',
    'киберспорт': 'e-other',
    'e-киберспорт': 'e-other'
}

games = []


def clean_list(games):
    games *= 0


def data_to_file(html, name):
    file = open(name, mode='w', encoding='utf-8')
    writer = file.write(html)
    file.close()


def get_games(d, day, league_name, sub_sport_1, sub_sport_2):
    games_list = str(d).split('<TR ALIGN="center" id=')
    games_list.pop(0)
    # n = 0
    for i in games_list:
        format_g = f'<tr align="center" bgcolor="#FFDECF" id {i}'
        # data_to_file(format_g, f'game{n}.txt')
        # n +=1
        # Event name (team names) from a tag
        # event_raw = game_data.find('a', {'id': re.compile('.*')}).text
        event_name_raw = re.findall(
            r'(<A HREF=".*" TARGET="main" id=".*">(.*)<img.*><.A>|<A HREF=".*" TARGET="main" id=".*">(.*)<.A>)',
            format_g)
        event_raw = event_name_raw[0]
        event_raw = event_raw[1] + event_raw[2]
        event_raw = re.sub('&nbsp;', '', event_raw)

        # link + id
        href_data = event_name_raw[0]
        href_data = href_data[0]
        href_data = re.findall(r'<A HREF="(.*)" TARGET.*', href_data)

        # EventId from link
        raw_id = re.sub('.*eventid=', '', href_data[0])
        raw_id = re.sub('&more.*', '', raw_id)

        # Make name str 2 list
        event_name_list = event_raw.split(' - ')

        event_exception_list = event_raw.split()

        # Make names list lowercase
        event_exception_list = [i.lower() for i in event_exception_list]

        # Check if ht at name contains exception
        if any(g_names_exception in event_exception_list for g_names_exception in g_names_exceptions):
            # print('exception:', event_exception_list)
            skip = True
        else:
            # print('no exception:', event_name_list)
            # AT name clear
            at_name = re.sub(' \(.*', '', event_name_list[1].strip())
            # name_data name replace left '(.*'
            name_data_left = re.sub('.*\(', '', event_name_list[1].strip())
            # name_data name replace right ')'
            name_data = re.sub('\)', '', name_data_left)

            if sub_sport_2 == '':
                # Check if event is Main\Mod for cyber without (к)
                event_type = ''
                mod_type = ''
                e_sport_2 = sub_sport_2
                if name_data == at_name:
                    event_type = 'Main'
                    mod_type = ''
                elif name_data == 'к':
                    at_name = at_name + ' (к)'
                    event_type = 'Main'
                    mod_type = ''
                    e_sport_2 = 'e-'
                elif 'Матч в' in name_data:
                    event_type = 'Main'
                    mod_type = ''
                elif any(serya in name_data for serya in series):
                    event_type = 'Main'
                    mod_type = ''
                elif any(mod in name_data for mod in mods):
                    event_type = 'Mod'
                    mod_type = mods.get(name_data)
                elif any(mod not in name_data for mod in mods):
                    return
                    # event_type = 'Main'
                    # mod_type = f'undefined {name_data}'
            elif sub_sport_2 == 'e-':
                # Check if event is Main\Mod for cyber with "Киберспорт" in league name
                event_type = ''
                mod_type = ''
                e_sport_2 = sub_sport_2
                if name_data == at_name:
                    event_type = 'Main'
                    mod_type = ''
                elif name_data == 'к':
                    at_name = at_name + ' (к)'
                    event_type = 'Main'
                    mod_type = ''
                    e_sport_2 = 'e-'
                elif any(serya in name_data for serya in series):
                    event_type = 'Main'
                    mod_type = ''
                elif any(mod in name_data for mod in mods):
                    event_type = 'Mod'
                    mod_type = mods.get(name_data)
                elif any(mod not in name_data for mod in mods):
                    # return
                    event_type = 'Main'
                    mod_type = ''

            ht_name = event_name_list[0].strip()

            # Sport name convertion
            sport = ''
            sport_tmp = str(e_sport_2 + sub_sport_1.strip()).lower()
            sport_val = sport_dict.get(sport_tmp)
            if sport_val:
                sport = sport_val
            else:
                sport = 'Err'

            # Event link
            link_a = 'https://tennisi.bet/rt/cgi/'
            # link_b = game_data.find('a', {'id': re.compile('.*')})['href']
            link_b = href_data[0]
            link = link_a + link_b

            # EventId from link
            # raw_id = re.sub('.*eventid=', '', link_b)
            # raw_id = re.sub('&more.*', '', raw_id)

            # Event start time
            # start_time = game_data.find('a', {'target': 'main'}).text

            start_time_raw = re.findall('<A HREF=".*" TARGET="main">(.*)<.A>', format_g)
            start_time = start_time_raw[0]

            # Event start date
            date = day.strip()
            arr_d = 'Сегодня'
            event_date_time = ''
            today = datetime.today()

            # Event date_time formated
            if date == arr_d:
                format_today = today.strftime("%Y-%m-%d")
                # output format 2021-06-17 10:33:52.20697301:00
                event_date_time = format_today + " " + str(start_time)
                tmp_time = datetime.strptime(event_date_time, "%Y-%m-%d %H:%M")
                timestamp = int(datetime.timestamp(tmp_time))
                # Проверить таймзону для работы со словарем
                # dt_object = datetime.fromtimestamp(timestamp)
            elif date != arr_d:
                tmp_date = date.split()
                year_is = today.strftime("%Y")
                date_is = tmp_date[0]
                month_is = months.get(tmp_date[1])
                event_date_time = str(year_is) + "-" + str(month_is) + "-" + str(date_is) + " " + str(start_time)
                tmp_time = datetime.strptime(event_date_time, "%Y-%m-%d %H:%M")
                timestamp = int(datetime.timestamp(tmp_time))
                # Проверить таймзону для работы со словарем
                # dt_object = datetime.fromtimestamp(timestamp)

            # Event league
            league = league_name
            outcomes = get_lines(format_g, sport, ht_name, at_name)

            games.append({'sport': sport, 'type': event_type, 'mod_type': mod_type, 'eventid': raw_id,
                          'league': league, 'link': link, 'timestamp': timestamp, 'datetime': event_date_time,
                          'start_date': date, 'start time': start_time, 'event_raw': event_raw, 'ht_name': ht_name,
                          'at_name': at_name, 'name_data': name_data, 'outcomes': outcomes})
    return
