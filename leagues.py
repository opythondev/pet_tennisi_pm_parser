import re
from games import get_games
import time

l_names_exceptions = (
    'Статистика игроков',
    'Первый',
    'Ответный',
    'по голам в своих матчах',
    'Обладатель',
    'Победитель',
    'Гибкий экспресс',
    'Итоги',
    'Статистические показатели групп',
    'Специальные ставки',
    'Кто забьёт больше голов на турнире',
    'Статистика выступления на турнире',
    'Лучший',
    'Кто выше по итогам чемпионата',
    'Победитель и обладатель Золотой бутсы'
    'забьет больше голов',
    'Забьет больше',
    'Сравнения',
    'Какая сборная',
    'Пара финалистов',
    'Специальные ставки на турнир. Тотал',
    'Специальные ставки на турнир',
    'Итоги группового турнира',
    'Синтетические матчи',
    'Отборочные матчи',
    'Итоги выступления сборной'
)


def get_dates(format_ii, league_name, sub_sport_1, sub_sport_2):
    # разбиваем таблицу по дням и получаем дату
    games_by_date = re.split(r'<TD COLSPAN.* CLASS="WO" NOWRAP>&nbsp;<b>', str(format_ii))
    games_by_date.pop(0)
    for d in games_by_date:
        format_d = f'<b>{d}'
        day_find = re.findall(r'^<b>(.*)</b>', format_d)
        day = str(day_find[0])
        #day = BeautifulSoup(format_d, 'html.parser').find('b').text
        # разбираем игры за 1 день
        get_games(d, day, league_name, sub_sport_1, sub_sport_2)


def get_leagues(table):
    league_name = table.find_all('th')
    if len(league_name) == 0:
        print("Error! Нет лиг!")
        print(len(league_name))
    elif len(league_name) > 0:
        # leagues_table = re.split('<th align="left', str(table))
        leagues_table = str(table).split('<th align="left')
        leagues_table.pop(0)
        for ii in leagues_table:
            format_g = f'<th {ii}'
            league_name = BeautifulSoup(format_g, 'html.parser').find('th').text.strip()
            sub_sport_1 = re.sub('::.*', '', league_name)
            league_name = re.sub('^.*:: ', '', league_name)
            league_name = re.sub('Кибер[а-я]*\. ', '', league_name)
            if any(l_names_exception in league_name for l_names_exception in l_names_exceptions):
                skip = True
            else:
                get_dates(ii, league_name, sub_sport_1)
                # add_data(games)
    return len(league_name)
