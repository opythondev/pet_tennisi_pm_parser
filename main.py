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
    'киберспорт': 'e-other'
}

val = 'a'
d = a_dict.get(val)
if d:
    print(a_dict.get(val))
