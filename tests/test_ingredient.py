import pytest

from praktikum.ingredient import Ingredient


class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type,name,price',
        [
            ('SAUCE', 'Hot sauce', 50),
            ('FILLING', 'Cutlet', 100),
            ('SAUCE', 'Cheese sauce', 75.5),
        ]
    )
    def test_ingredient_getters_return_correct_values(
        self,
        ingredient_type,
        name,
        price
    ):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price