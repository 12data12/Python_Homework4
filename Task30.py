#Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

keys = open('users.txt','r')
keys_content = keys.read().split('\n')
values = open('hobbies.txt','r')
values_content = values.read().split('\n')
dictionary = dict(zip(keys_content, values_content))

import json
result = open('users_hobbies.txt','w')
result_content = result.write(json.dumps(dictionary, indent =4, separators=(" ", ',')))

keys.close()
values.close()
result.close()