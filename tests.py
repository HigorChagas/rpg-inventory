from inventory import add_item, edit_item, find_by_name, remove_item


def test():
    inventory = [
        {"name": "Espada", "category": "arma", "weight": 19},
        {"name": "Arco", "category": "arma", "weight": 19},
    ]

    categories = set()

    edit_item(inventory, "Espada", {"name": "Poção", "category": "Item", "weight": 0.5})


test()
