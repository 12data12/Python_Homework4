#Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

keys = open('users.txt').read().split('\n')
values = open('hobbies.txt').read().split('\n')
dictionary = dict(zip(keys, values))

import json
open('users_hobbies.txt', 'w').write(json.dumps(dictionary, indent =4, separators=(" ", ',')))
