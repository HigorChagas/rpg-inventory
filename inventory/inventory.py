import json


def add_item(inventory, categories, name, category, weight):
    name = name.strip().lower()
    category = category.strip().lower()

    if any(d["name"] == name for d in inventory):
        raise ValueError(f"O item '{name}' já existe no inventário!\n")

    if weight > 60:
        raise ValueError("O peso do item não pode ultrapassar 60kg\n")

    item = {"name": name, "category": category, "weight": weight}

    total_weight = inv_total_weight(inventory) + weight
    if total_weight > 100:
        raise ValueError(
            f"Peso máximo do inventário alcançado (100kg)\nO item {name} não foi adicionado\n"
        )

    inventory.append(item)
    save_inventory(inventory)
    categories.add(category)
    print(f"Item '{name}' adicionado com sucesso!\n")


def remove_item(inventory, item_name):
    item_name = item_name.strip().lower()
    if not item_name:
        raise ValueError("Você deve digitar o nome do item")
    if len(inventory) == 0:
        raise Exception("O inventário não contém nenhum item")

    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            save_inventory(inventory)
            print(f"Item {item_name} removido do inventário")
            return

    raise Exception("Esse item não está no inventário")


def inv_total_weight(inventory):
    total_weight = 0
    for item in inventory:
        total_weight += item["weight"]
    return total_weight


def list_items(inventory):
    total_weight = inv_total_weight(inventory)
    for i, obj in enumerate(inventory, 1):
        print(f"🟦 Slot {i} 🟦")
        print(f"Nome: {obj['name']}")
        print(f"Categoria: {obj['category']}")
        print(f"Peso {obj['weight']}\n")
    print(f"Peso Total: {total_weight}\n")


def find_by_category(inventory, category):
    category = category.strip().lower()
    results = []
    for item in inventory:
        if item["category"] == category:
            results.append(item)

    if len(results) == 0:
        raise ValueError("Nenhum item com essa categoria foi encontrado")
    return results


def find_by_name(inventory, item_name):
    item_name = item_name.strip().lower()
    results = []
    for item in inventory:
        if item_name in item["name"]:
            results.append(item)

    for i, obj in enumerate(results, 1):
        print(f"🟦 Slot {i} 🟦")
        print(f"Nome: {obj['name']}")
        print(f"Categoria: {obj['category']}")
        print(f"Peso {obj['weight']}\n")

    if len(results) == 0:
        raise ValueError("Nenhum item com esse nome foi encontrado")

    if not item_name:
        raise ValueError("Por favor, forneça o nome do item")

    return


def show_categories(categories):
    return categories


def edit_item(inventory, item_name, updates):
    if not updates:
        raise ValueError("Nenhuma informação para atualizar")

    item_name = item_name.strip().lower()
    for item in inventory:
        if item["name"].strip().lower() == item_name:
            for field, value in updates.items():
                if isinstance(value, str):
                    value = value.strip().lower()
                item[field] = value
            save_inventory(inventory)
            print("Item editado com sucesso!")
            return

    raise ValueError("Item não encontrado")


def load_inventory():
    try:
        with open("data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_inventory(inventory):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=4)
