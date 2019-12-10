import requests
import time

from time import sleep
from pprint import pprint
from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': 7236311,
    #'redirect_uri': '',
    'display': 'page',
    'response_type': 'token',
    'scope': 'offline, friends, groups',

}

print('?'.join(
    (OAUTH_URL, urlencode(OAUTH_PARAMS))
))

TOKEN = '3973af83b992c181f8a15f95d4da5667565be5754326f5188193d3f9965c381e03d39ed08dd21277f9ba6'
user_id = input('Введите id пользователя: ')

params_1 = {
    'access_token': TOKEN,
    'v': '5.103',
    'user_id': user_id,
    'extended': 1,
    'fields': 'members_count'
}
response_1 = requests.get(
    'https://api.vk.com/method/groups.get',
    params_1
)
# pprint(response_1.json())
rezult_groups = response_1.json()
# pprint(rezult_groups)

groups_list = []
for number_id in rezult_groups['response']['items']:
    id_1 = number_id['id']
    groups_list.append(id_1)
    # print(id_1)


for id_groups in groups_list:
    params_3 = {
        'access_token': TOKEN,
        'v': '5.103',
        'group_id': id_groups,
        'filter': 'friends'
    }
    response_3 = requests.get(
        'https://api.vk.com/method/groups.getMembers',
        params_3
        )

    rezult_groups_frends = response_3.json()

    groups_frends_dict = {}
    for key, value in rezult_groups_frends['response'].items():
        if value == 0:
            rez_dict = dict({'id_group': id_groups})
            groups_frends_dict.update(rez_dict)
            # print(groups_frends_dict)


    for group_id in groups_frends_dict.values():
        params_4 = {
            'access_token': TOKEN,
            'v': '5.103',
            'group_id': group_id,
            'fields': 'members_count'
            }
        response_4 = requests.get(
        'https://api.vk.com/method/groups.getById',
        params_4
            )
        all_rezult = response_4.json()
        # pprint(all_rezult)

        groups_frends_list = []
        for block in all_rezult['response']:
            id_block = block['id']
            name_block = block['name']
            members_count_block = block['members_count']
            dict_block = dict({'name': name_block, 'gid': id_block, 'members_count': members_count_block})
            groups_frends_list.append(dict_block)
            pprint(groups_frends_list)


