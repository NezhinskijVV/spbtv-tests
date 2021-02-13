import configparser


class Api:
    parser = configparser.ConfigParser()
    parser.read('../config.ini')

    BASE_URL = parser.get('spbtv', 'url')
    API_URL = parser.get('spbtv', 'api_url')
    CHECK_LOGIN_URL = API_URL + '/v1/users/username_availability.json'

    @staticmethod
    def check_login_format_response(resp_json):
        if 'data' not in resp_json:
            raise ValueError("No field 'data' in given json")

        if 'available' not in resp_json['data']:
            raise ValueError("No field 'available' for 'data'")

        if 'type' not in resp_json['data']:
            raise ValueError("No field 'type' for 'data'")

        if 'object' not in resp_json['data']:
            raise ValueError("No field 'object' for 'data'")
