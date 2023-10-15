from unittest.mock import patch

import requests
from devtools import debug
from unit import Data


class TestUnit:
    @patch.object(Data, "get_dimension")
    def test_get_data(self, get_dimension):
        def side_effect(dim, n):
            return dim * n

        get_dimension.side_effect = side_effect

        x = Data().get_data(4)

        assert x["a"] == "aaaa"
        assert x["b"] == "bbbb"

        debug(x)


class TestIntegration:
    def test_api_v1_data(self):
        r = requests.get("http://localhost:8000/api/v1/data/4")

        assert r.status_code == 200
        assert r.headers["Content-Type"] == "application/json"
        payload = r.json()

        assert isinstance(payload, dict)

        assert payload["a"] == "aaaa"
        assert payload["b"] == "bbbb"

        debug(payload)
