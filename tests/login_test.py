from utils.http_manager import HttpManager
from utils.api import Api


class TestLoginForm:

    @staticmethod
    def test_smoke():
        result = HttpManager.get(Api.BASE_URL)
        assert 200 == result.status_code

    @staticmethod
    def test_check_not_register_username():
        result = HttpManager.get_with_param_username(Api.CHECK_LOGIN_URL, 'seekeRRofconfessor@gmail.com')

        response_json = result.json()
        print(response_json)
        Api.check_login_format_response(response_json)

        assert 200 == result.status_code
        assert response_json['data']['available'] == True

    @staticmethod
    def test_check_register_username():
        result = HttpManager.get_with_param_username(Api.CHECK_LOGIN_URL, 'seekerofconfessor@gmail.com')

        response_json = result.json()
        print(response_json)

        Api.check_login_format_response(response_json)

        assert 200 == result.status_code
        assert response_json['data']['available'] == False
