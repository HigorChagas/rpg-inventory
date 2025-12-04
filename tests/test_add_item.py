import pytest

from inventory.inventory import add_item


def test_add_item_basic():
    inventory = []
    categories = set()

    add_item(inventory, categories, "espada", "arma", 10)

    # inventário deve ter 1 item
    assert len(inventory) == 1

    item = inventory[0]

    assert item["name"] == "espada"
    assert item["category"] == "arma"
    assert item["weight"] == 10

    # categoria deve ter sido adicionada
    assert "arma" in categories


def test_add_item_weight():
    inventory = []
    categories = set()

    add_item(inventory, categories, "espada", "arma", 10)

    with pytest.raises(ValueError):
        add_item(inventory, categories, "espada", "arma", 61)


def test_add_item_already_exists():
    inventory = [{"name": "espada", "category": "arma", "weight": 10}]
    categories = set()

    with pytest.raises(ValueError):
        add_item(inventory, categories, "espada", "arma", 10)
