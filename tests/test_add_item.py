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
