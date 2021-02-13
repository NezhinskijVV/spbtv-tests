import requests


class HttpManager:
    headers = {'Content-Type': 'application/json',
               'Host': 'api.spbtv.com'}
    cookie = ""

    params = {'client_id': '66797942-ff54-46cb-a109-3bae7c855370',
              'locale': 'ru',
              'client_version': '3.1.3-5933',
              'timezone': '10800'}

    @staticmethod
    def get(url):
        result = requests.get(url,
                              headers=HttpManager.headers,
                              cookies=HttpManager.cookie)
        return result

    @staticmethod
    def get_with_param_username(url, username):
        res_params = HttpManager.params.copy()
        res_params.update({'username': username})
        result = requests.get(url,
                              headers=HttpManager.headers,
                              cookies=HttpManager.cookie,
                              params=res_params)
        return result
