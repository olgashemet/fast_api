from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
import requests
from devtools import debug
from unit import Data


class TestUnit:
    @patch.object(Data, "get_dimension")
    def test_get_data(self, get_dimension: MagicMock) -> None:
        def side_effect(dim: str, num: int) -> str:
            return dim * num

        get_dimension.side_effect = side_effect

        data = Data().get_data(4)

        assert data["a"] == "aaaa"
        assert data["b"] == "bbbb"

        debug(data)


class TestIntegration:
    @pytest.mark.skip(reason="localhost:800 is not available, unknown")
    def test_api_v1_data(self) -> None:
        response = requests.get(
            "http://localhost:8000/api/v1/data/4",
            timeout=4,
        )

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        payload = response.json()

        assert isinstance(payload, dict)

        assert payload["a"] == "aaaa"
        assert payload["b"] == "bbbb"

        debug(payload)
