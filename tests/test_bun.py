import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        'name,price',
        [
            ('Black bun', 100),
            ('White bun', 200.5),
            ('Red bun', 0),
        ]
    )
    def test_bun_get_name_and_price_returns_correct_values(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name
        assert bun.get_price() == price