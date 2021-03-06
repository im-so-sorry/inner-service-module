from datetime import datetime, timedelta
from typing import Optional, Dict, List
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

    def get_user(self, username: str, token: str = None):
        path = "user/social_user/get_user/"
        params = {}
        if token:
            params["token"] = token
        return self._make_call(path, params=params, username=username)

    def switch_streaming(self, username: str, state: bool = True, token: str = None):
        path = "user/social_user/switch_streaming/"
        params = {}
        if token:
            params["token"] = token
        body = {
            "state": state
        }
        return self._make_call(path, method="POST", body=body, params=params, username=username)

    def get_rules(self, username: str, social: str = None):
        path = "stream/rule/"

        params = {
            "social": social or self.service
        }

        return self._make_call(path, params=params, username=username)

    def add_rule(self, username: str, tag: str, value: str, social: str = None):
        path = "stream/rule/"

        body = {
            "key": tag,
            "value": value,
            "service": social or self.service
        }

        return self._make_call(path, method="POST", body=body, username=username)

    def remove_rule(self, username: str, tag: str, social: str = None):
        path = "stream/rule/remove_rule/"

        body = {
            "key": tag,
            "social": social or self.service
        }

        return self._make_call(path, method="DELETE", body=body, username=username)

    def get_stats(self, username: str, tags: List[str] = None, service: str = None, from_date: "datetime" = None,
                  to_date: "datetime" = None):
        path = "stream/event/stats/"

        body = {}

        if from_date:
            body["from_date"] = from_date.isoformat()

        if to_date:
            body["to_date"] = to_date.isoformat()

        if tags:
            body["tags"] = tags

        if service:
            body["services"] = [service]

        return self._make_call(path, method="POST", body=body, username=username)


if __name__ == '__main__':
    bs = BaraddurService("http://localhost:8000/", "1", "vk")

    # r = bs.get_user("arck1", "1")
    # print(r.json())

    # r = bs.get_rules("98449858", "vk")
    # print(r.text)

    r = bs.get_user("98449858")
    print(r.text)
