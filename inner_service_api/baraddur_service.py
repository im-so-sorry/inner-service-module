from typing import Optional, Dict
from urllib.parse import urljoin

import requests
from requests import Response

from inner_service_api.base_service import BaseService


class BaraddurService(BaseService):
    def __init__(self, base_url: str, token: str, service: str) -> None:
        self.base_url = base_url
        self.token = token
        self.service = service

    def _make_call(self, path: str, method: str = "GET", params: Optional[Dict] = None, body: Dict = None, *,
                   username: str) -> Response:
        url = urljoin(self.base_url, path)

        headers = {
            "X-USERNAME": str(username),
            "X-SERVICE": str(self.service),
            "X-INTERNAL-TOKEN": str(self.token)
        }

        response = requests.request(method, url=url, params=params, json=body, headers=headers)

        return response

    def get_user(self, username: str, token: str):
        path = "user/social_user/get_user"
        params = {
            "token": token
        }
        return self._make_call(path, params=params, username=username)

    def get_rules(self, username: str, social: str = None):
        path = "stream/rule"

        params = {
            "social": social or self.service
        }

        return self._make_call(path, params=params, username=username)

    def add_rule(self, username: str, tag: str, value: str, social: str = None):
        path = "stream/rule"

        params = {
            "social": social or self.service
        }

        return self._make_call(path, params=params, username=username)


if __name__ == '__main__':
    bs = BaraddurService("http://localhost:8000/", "1", "vk")

    # r = bs.get_user("arck1", "1")
    # print(r.json())

    r = bs.get_rules("arck1", "1")
    print(r.json())
