from inventory.inventory import (
    add_item,
    edit_item,
    find_by_category,
    find_by_name,
    list_items,
    load_inventory,
    remove_item,
    show_categories,
)


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def main():
    inventory = load_inventory()
    categories = set(item["category"] for item in inventory)

    while True:
        print(f"{bcolors.OKCYAN}Inventário, selecione a opção desejada: {bcolors.ENDC}")
        print(f"{bcolors.WARNING}1{bcolors.ENDC} - Adicionar item")
        print(f"{bcolors.WARNING}2{bcolors.ENDC} - Remover item")
        print(f"{bcolors.WARNING}3{bcolors.ENDC} - Mostrar itens")
        print(f"{bcolors.WARNING}4{bcolors.ENDC} - Buscar item pela categoria")
        print(f"{bcolors.WARNING}5{bcolors.ENDC} - Mostrar categorias")
        print(f"{bcolors.WARNING}6{bcolors.ENDC} - Buscar item pelo nome")
        print(f"{bcolors.WARNING}7{bcolors.ENDC} - Editar Item")
        print(f"{bcolors.WARNING}8{bcolors.ENDC} - Sair\n")

        try:
            option = int(input("Digite o número do menu: "))
        except ValueError:
            print("Opção inválida. Digite um número.\n")
            continue

        match option:
            case 1:
                try:
                    name = input("Nome do item: ").strip().lower()
                    if not name:
                        raise ValueError("O nome do item não pode ser em branco\n")

                    category = input("Categoria do item: ").strip().lower()
                    if not category:
                        raise ValueError("A categoria do item não pode ser em branco\n")

                    weight = input("Peso do item: ").strip()
                    if not weight:
                        raise ValueError("O peso do item é obrigatório\n")
                    weight = float(weight)

                    add_item(inventory, categories, name, category, weight)
                except ValueError as e:
                    print(f"{bcolors.FAIL}{e}")
            case 2:
                item_name = input("Qual o nome do item: ").strip().lower()
                try:
                    remove_item(inventory, item_name)
                except Exception as e:
                    print(e)
            case 3:
                list_items(inventory)
            case 4:
                category = input("Qual a categoria dos itens: ").strip().lower()
                try:
                    print(find_by_category(inventory, category))
                except Exception as e:
                    print(e)
            case 5:
                print(show_categories(categories))
            case 6:
                item_name = input("Qual o nome do item: ").strip().lower()
                try:
                    find_by_name(inventory, item_name)
                except Exception as e:
                    print(e)
            case 7:
                try:
                    item_name = input("Qual o nome do item: ").strip().lower()
                    print(
                        f"{bcolors.OKGREEN}Altere somente os campos necessários{bcolors.ENDC}\n"
                    )
                    new_name = input("Digite o novo nome do item: ").strip().lower()
                    new_category = (
                        input("Digite a nova categoria do item: ").strip().lower()
                    )
                    new_weight = input("Digite o novo peso do item: ").strip()
                    updates = {}

                    if new_name:
                        updates["name"] = new_name
                    if new_category:
                        updates["category"] = new_category
                    if new_weight:
                        updates["weight"] = float(new_weight)

                    if not updates:
                        raise ValueError("Nenhum valor digitado\n")

                    edit_item(inventory, item_name, updates)
                except ValueError as e:
                    print(e)
            case 8:
                print("Saindo...")
                break
            case _:
                print("Opção inválida, escolha novamente\n")


if __name__ == "__main__":
    main()
