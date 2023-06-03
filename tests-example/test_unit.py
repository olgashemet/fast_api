from unittest.mock import MagicMock, patch
from devtools import debug
import os

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

