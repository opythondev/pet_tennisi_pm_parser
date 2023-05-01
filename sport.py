import requests
from leagues import get_dates
from games import games, clean_list
import time
import re
import cProfile


sportId = {
    "soccer": '137',
    'tennis': '139',
    'basket': '140',
    'hockey': '138',
    'volleyball': '9027116',
    'handball': '5662396',
    'baseball': '326835',
    'cybersport': '439908280'
}


URL = f'https://tennisi.bet/rt/cgi/!book2_free.BetsLines?gameid=5&lang=rus&categoryid=439908280&eventid=&parentid=&showold' \
      f'=&rt=210615112403&pidstmpid=0&betgroupid=-3&age=0'


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


headers = {
    # заголовки запроса
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-language": "ru,en-US;q=0.9,en;q=0.8,ru-RU;q=0.7",
    "cache-control": "max-age=0",
    "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "frame",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1"
}


def extract_sport_page2(url):
    print(f'Парсиниг страницы {url}')
    start8 = time.perf_counter()
    result = requests.get(url, headers=headers)
    print(f'Page response sec: {time.perf_counter() - start8}')
    tables = re.split(r'<TABLE   style="border-collapse: collapse;', str(result.text))
    tables.pop(0)
    for i in tables:
        leagues_table = re.split('<TH ALIGN="left" ', i)
        leagues_table.pop(0)
        for ii in leagues_table:
            format_ii = f'<TH {ii}'
            sport_tmp = re.findall('.*TARGET="main"><b><font color=white>(.*)<.b><.font><.A><.font>', format_ii)
            sub_sport_tmp = sport_tmp[0]
            sub_sport_1 = re.sub('::.*', '', sub_sport_tmp)
            sub_sport_2 = re.findall('.*Кибер.*', sub_sport_tmp)
            if sub_sport_2:
                sub_sport_2 = 'e-'
            else:
                sub_sport_2 = ''
            league_name = re.sub('^.*:: ', '', sub_sport_tmp)
            league_name = re.sub('Кибер[а-я]*\. ', '', league_name).strip()
            if any(l_names_exception in league_name for l_names_exception in l_names_exceptions):
                skip = True
            else:
                get_dates(format_ii, league_name, sub_sport_1, sub_sport_2)
    return 'Done'


def data_to_file(html, name):
    file = open(name, mode='w', encoding='utf-8')
    writer = file.write(html)
    file.close()


if __name__ == "__main__":
    while True:
        start3 = time.perf_counter()
        #cProfile.run('extract_sport_page2(URL)')
        print(extract_sport_page2(URL))
        print(games)
        print(f'цикл {time.perf_counter() - start3}')
        time.sleep(3)
        clean_list(games)

