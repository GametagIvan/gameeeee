import json

with open('Загрузки/game_j.json', 'r', encoding='utf-8') as f:
    game = json.load(f)

inventory = []
cur = game['start_node']
hp = 3

while True:
    node = game['nodes'][cur]
    print("\n" + "="*60)
    print(node['desc'].replace('{hp}', str(hp)))
    print(f"{hp}/3")

    if node.get('is_end'):
        print("\nИгра завершена! ")
        break

    if hp <= 0:
        print("\nТы погиб... Игра завершена! ")
        break

    opti = []
    for opt in node.get('opti', []):
        if 'condition' in opt:
            if opt['condition'].get('has_item') not in inventory:
                continue
        opti.append(opt)

    if not opti and cur == 'room6' and 'fallback_room6' in node:
        cur = node['fallback_room6']
        continue

    if not opti:
        print("\n[Тупик] Игра завершена!")
        break

    for i, opt in enumerate(opti, 1):
        print(f"{i}. {opt['text']}")

    choice = int(input("\nВыбор: ")) - 1
    selected = opti[choice]

    if selected.get('action') == 'add_item':
        inventory.append(selected['item'])
        print(f"\n[Взял: {selected['item']}]")

    if selected.get('action') == 'damage':
        hp -= selected.get('damage', 1)
        print(f"\nУрон! -{selected.get('damage',1)} HP")

    if selected.get('action') == 'heal':
        hp = min(3, hp + selected.get('heal', 1))
        print(f"\nЛечение! +{selected.get('heal',1)} HP")

    cur = selected['next']
import json

with open('Загрузки/game_j.json', 'r', encoding='utf-8') as f:
    game = json.load(f)

inventory = []
cur = game['start_node']
hp = 3

while True:
    node = game['nodes'][cur]
    print("\n" + "="*60)
    print(node['desc'].replace('{hp}', str(hp)))
    print(f"{hp}/3")

    if node.get('is_end'):
        print("\nИгра завершена! ")
        break

    if hp <= 0:
        print("\nТы погиб... Игра завершена! ")
        break

    opti = []
    for opt in node.get('opti', []):
        if 'condition' in opt:
            if opt['condition'].get('has_item') not in inventory:
                continue
        opti.append(opt)

    if not opti and cur == 'room6' and 'fallback_room6' in node:
        cur = node['fallback_room6']
        continue

    if not opti:
        print("\n[Тупик] Игра завершена!")
        break

    for i, opt in enumerate(opti, 1):
        print(f"{i}. {opt['text']}")

    choice = int(input("\nВыбор: ")) - 1
    selected = opti[choice]

    if selected.get('action') == 'add_item':
        inventory.append(selected['item'])
        print(f"\n[Взял: {selected['item']}]")

    if selected.get('action') == 'damage':
        hp -= selected.get('damage', 1)
        print(f"\nУрон! -{selected.get('damage',1)} HP")

    if selected.get('action') == 'heal':
        hp = min(3, hp + selected.get('heal', 1))
        print(f"\nЛечение! +{selected.get('heal',1)} HP")

    cur = selected['next']
