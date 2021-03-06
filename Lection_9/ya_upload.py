import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        file_name = file_path.split('/')[-1]
        token = self.token
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={'path': file_name},
                                headers={'Authorization': f'OAuth {token}'})
        href = response.json()['href']
        with open(file_path, 'rb') as f:
            requests.put(href, files={'file': f})
        if response.status_code == 200:
            print('Успешная выгрузка файла')
        return
if __name__ == '__main__':
    uploader = YaUploader('TOKEN')
    uploader.upload('dZein0z.gif')
