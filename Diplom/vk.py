import requests
from datetime import datetime
from pprint import pprint

with open('Diplom/token.txt') as file_object:
    token = file_object.read().strip()
with open('Diplom/yatoken.txt') as f:
    yatoken = f.read().strip()

class VkUser:
    url = 'https://api.vk.com/method/'

    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version,
        }
        self.owner_id = requests.get(self.url+'users.get', self.params).json()['response'][0]['id']

    def get_photos_links(self, user_id=None):
        if user_id is None:
            user_id = self.owner_id
        followers_url = self.url + 'photos.get'
        followers_params = {
            'album_id': 'profile',
            'count': 10,
            'user_id': user_id,
            'extended': 1
        }
        res = requests.get(followers_url, params={**self.params, **followers_params}).json()['response']['items']
        dict_url = {}
        list_url = []
        res_list = []
        for line in res:
            dict_url.update(line)
            list_url.append(dict_url['sizes'][-1]['url'])
            res_list.append({str(line['likes']['count']): dict_url['sizes'][-1]['url']})
        return res_list

vk_client = VkUser(token, '5.130')
vk_client.get_photos_links()
dict_keys = {}
for line in vk_client.get_photos_links():

    dict_keys.update(line)

# pprint(dict_keys)
for x,y in dict_keys.items():
    if list(dict_keys.keys()).count(x) > 1:
        print(x,y)
    print(dict_keys.keys())
        # for like, link in line.items():
    #     if like.count(like)>1:
    #         print(like)

        # response = requests.post('https://cloud-api.yandex.net/v1/disk/resources/upload',
        #                         params={'path': f'{like}.jpg',
        #                                 'url': link},
        #                         headers={'Authorization': f'OAuth {yatoken}'})



# for link in vk_client.get_photos_links():
#     with open(link, 'rb') as f:
#         requests.post(href, files={'file': f})


# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         """Метод загружает файл file_path на яндекс диск"""
#         file_name = vk_client.get_photos_links()#file_path.split('/')[-1]
#         token = self.token
#         response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
#                                 params={'path': file_name},
#                                 headers={'Authorization': f'OAuth {token}'})
#         href = response.json()['href']
#         with open(file_path, 'rb') as f:
#             requests.put(href, files={'file': f})
#         if response.status_code == 200:
#             print('Успешная выгрузка файла')
#         return
#
# # if __name__ == '__main__':
# uploader = YaUploader(yatoken)
# uploader.upload(vk_client.get_photos_links())