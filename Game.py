from random import randint
from time import sleep

player = {
    'name': '',
    'armor': 0,
    'hp': 100,
    'attack': 5,
    'luck': 0,
    'money': 1000,
    'inventory': []
}

enemies = [
    {
        'name': 'Цветочек',
        'hp': 10,
        'attack': 10,
        'script': 'Зачем ты здесь? Ты не пройдешь через меня, Тебе меня не победить!',
        'win': 'Ты - достойный противник,  Цветок погибает.',
        'loss': 'Цветок съедает вас.'
    },

    {
        'name': ':Жрубсень',
        'hp': 200,
        'attack': 5,
        'script': 'Не ожидал меня встретить? Я проголодался и ты станешь моим ужином!',
        'win': 'Мой животик так и остался вурчащим...',
        'loss': 'Сегодня кто-то поужинает, но точно не ты!'
    },

    {
        'name': 'Неуловимыч',
        'hp': 50,
        'attack': 20,
        'script': 'Щщщих кто вторгся в мои владенья? Зря ты сюда полез, теперь ты будешь гнить в земле!',
        'win': 'Щщщих ты силен, но тебе не победить моих братьев...',
        'loss': 'Прощай...'
    },
    {
        'name': 'Найтсталкер',
        'hp': 90,
        'attack': 40,
        'script': 'Зэночня я прекращю твое существование жалкий кусок плоти!',
        'win': 'Ты не такой как все...',
        'loss': 'Тебе не следовало сюда суваться!'
    },
    {
        'name': 'Лич',
        'hp': 40,
        'attack': 75 ,
        'script': 'Ты очень силен раз пришел сюда, но дальше тебе не пройти!',
        'win': 'Я даже рад что моя душа успокоилась...',
        'loss': 'ТЫ, НЕ, ПРОЙДЕШЬ!'
    },
    {
        'name': 'Вольдемар',
        'hp': 225,
        'attack': 73 ,
        'script': 'Сейчас ты утонешь в моей болоте!',
        'win': 'Утонуть в своемже болоте - худшая смерть...',
        'loss': 'Легчайшая для величайшего!'
    }
]
import Вступление
#Начало игры
name = input('Введи своё имя, путник: ')
import Диалог1
player['name'] = name
current_enemy = 0
round = randint(1, 2)
enemy = enemies[current_enemy]
enemy_hp = enemies[current_enemy]['hp']
print(f'Противник - {enemy["name"]}: {enemy["script"]}')
sleep(1)
print("Я здесь чтобы помочь деревне!")
input('Enter чтобы продолжить')
print()
while player['hp'] > 0 and enemy_hp > 0:
    if round % 2 == 1:
        print(f'{player["name"]} атакует {enemy["name"]}.')
        enemy_hp -= player['attack']
        sleep(1)
        print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
        print()
        sleep(1)
    else:
        print(f'{enemy["name"]} атакует {player["name"]}.')
        player['hp'] -= enemy['attack']
        sleep(1)
        print(f'''{player['name']} - {player['hp']}
{enemy['name']} - {enemy_hp}''')
        print()
        sleep(1)
    round += 1

if player['hp'] > 0:
    print(f'Противник - {enemy["name"]}: {enemy["win"]}')
else:
    print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
if player['hp'] > 0:
    print("Вашь баланс пополнен,Баланс:")
    player["money"] +=50
    print(player["money"])
else:
    print("Вы проиграли")
print("Вы добераетесь до деревне и вас встречает доктор по имени: Стенфорд")
sleep(2)
print("""Стенфорд спрашивает вас нужна ли вам медецинская помощь?
Цена:Бесплатно""")
sleep(1)
answer0 = int(input("""Ваш ответ:1-Нет, спасибо.;2-Да, было бы славно.
Впешите(1или2):"""))
if answer0 == 1:
    print("Вы проходите дальше.")
elif answer0 ==2:
    print("""Стенфонд оказывает вам медецинскую помощь.""")
    player['hp'] = 100
    print(player["hp"])
    sleep(2)
    print("Вы идите дальше.")
else:
    print("Вы незамечая Стенфорда, проходите дальше.")
    sleep(2)
print("Вы доходите до перекрестка всех улиц.")
sleep(2)
print("Монетка говорит: тебе сейчас нужно идти прямо и ты попадешь на рынок, хочу обратить твое внимание на продавца по имени:Виктор оставь деньги для покупки жетона, как я помню минимальный стоит 500")
sleep(2)
print("Вы идите на рынок и встречаете торговца броней по имени: Сидор")
sleep(1)
goods0 ={"Деревянная броня":500,"Кольчуга":1000,"Железная броня":1500}
print(goods0)
sleep(1)
print("Деревянная броня снижает урон на 10 дополнительный шанц заблокировать удар и контр атаковать.;Кольчуга снижает на 20;Железная броня снижает атаку на 30")
sleep(2)
print("Игрок, делайте каждый выбор осмысленно, вернутся назад нельзя!")
buy0 = int(input("""Какую броню вы хочите купить:1-Деревянная броня.;2-Кольчуга.;3-Железная броня.;4-пройти дальше
Впешите(1/2/3/4):"""))
sleep(1)
if buy0 == 4:
    print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
elif buy0==1:
    answer2 = input("Вы хотите купить данную броню?").title()
    if answer2 == "Да":
        if player['money'] >= 500:
            if "Деревянная броня" in goods0:
                del goods0['Деревянная броня']
                player['money'] -=500
                player['inventory'].append('Деревянная броня')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
    if answer2 == "Нет":
        print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
if buy0 ==2:
    answer2 = input("Вы хотите купить данную броню?").title()
    if answer2 == "Да":
        if player['money'] >= 1000:
            if "Кольчуга" in goods0:
                del goods0['Кольчуга']
                player['money'] -=1000
                player['inventory'].append('Кольчуга')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
    if answer2 == "Нет":
        print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
    if buy0==3:
            answer2 = input("Вы хотите купить данную броню?").title()
    if answer2 == "Да":
        if player['money'] >=1500:
            if "Железная броня" in goods0:
                del goods0['Железная броня']
                player['money'] -=1500
                player['inventory'].append('Железная броня')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
    if answer2 == "Нет":
        print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
sleep(1)
goods1 = {"Меч":500,"Копье":1000,"Булава":1500}
print(goods1)
sleep(1)
print("Меч увеличивает вашь урон на 20.;Копье увеличивает урона на 30.;Булава увеличивает вашь урон на 45")
buy1 = int(input("Какое оружие вы хотите купить:1-Меч.;2-Копье.;3-Булава.;4-пройти дальше."))
sleep(1)
if buy1 == 4:
    print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
elif buy1==1:
    answer3 = input("Вы хотите купить данное оружие?").title()
    if answer3 == "Да":
        if player['money'] >= 500:
            if "Меч" in goods1:
                del goods1['Меч']
                player['money'] -=500
                player['inventory'].append('Меч')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
    if answer3 == "Нет":
        print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
if buy1 ==2:
    answer3 = input("Вы хотите купить данное оружие?").title()
    if answer3 == "Да":
        if player['money'] >= 1000:
            if "Кольчуга" in goods1:
                del goods1['Копье']
                player['money'] -=1000
                player['inventory'].append('Копье')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
    if answer3 == "Нет":
        print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
    if buy1==3:
            answer3 = input("Вы хотите купить данное оружие?").title()
    if answer3 == "Да":
        if player['money'] >=1500:
            if "Булава" in goods1:
                del goods1['Булава']
                player['money'] -=1500
                player['inventory'].append('Булава')
                print(player)
                sleep(1)
                print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
    if answer3 == "Нет":
        print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
sleep(1)
goods2 = {"Жетон радости":500,"Жетон удачи":1000,"Жетон леплекона":1500}
print(goods2)
sleep(1)
print("""Жетон радости дает возможность выпадения более дорогих безделушек и увелечение дропа монет.;Жетон удачи дает шанц на выпадение ценных вещей.;Жетон леплекона даец шанц на выпадение лучших вещей""")
buy2={"Какой жетон вы хотите купить:1-Жетон радости.;2Жетон удачи-.;3Жетон леплекона-.;4-пройти дальше"}
sleep(1)
if buy2 == 4:
    print("Вы проходите дальше, и поподаете в опасную зону ")
elif buy2==1:
    answer4 = input("Вы хотите купить данный жетон?").title()
    if answer4 == "Да":
        if player['money'] >= 500:
            if "Жетон радости" in goods2:
                del goods2['Жетон радости']
                player['money'] -=500
                player['inventory'].append('Жетон радости')
                print(player)
                sleep(1)
                print("Вы идете дальше, и поподаете в опасную зону")
    if answer4 == "Нет":
        print("Вы проходите дальше, и поподаете в опасную зону")
if buy2 ==2:
    answer4 = input("Вы хотите купить данный жетон?").title()
    if answer4 == "Да":
        if player['money'] >= 1000:
            if "Жетон удачи" in goods2:
                del goods2['Жетон удачи']
                player['money'] -=1000
                player['inventory'].append('Жетон удачи')
                print(player)
                sleep(1)
                print("Вы идете дальше, и поподаете в опасную зону")
    if answer4 == "Нет":
        print("Вы проходите дальше, и поподаете в опасную зону")
    if buy2==3:
            answer4 = input("Вы хотите купить данный жетон?").title()
    if answer4 == "Да":
        if player['money'] >=1500:
            if "Жетон леплекона" in goods2:
                del goods2['Жетон леплекона']
                player['money'] -=1500
                player['inventory'].append('Жетон леплекона')
                print(player)
                sleep(1)
                print("Вы идете дальше, и поподаете в опасную зону")
    if answer4 == "Нет":
        print("Вы проходите дальше, и поподаете в опасную зону")
import Диалог2
monsters_lower = {"Жрубсень","Неуловимыч",}
sleep(6)
print("""Примечание: Вы не можете атаковать монстра, к которому вы ещё не открыли путь.
(Не одолели монстра перед ним)""")
def weapons():
            print(player["inventory"])
            sleep(1)
            print("""Примечание: пишите правельно названия точ в точ как в инвентаре и обращайте внимание какой предмет вас спрашивают!
пробелы нужно ставить!""")
            weapons1 = input("Выберете броню которую вы будете использовать:")
            if weapons1 == "Деревянная броня":
                if "Деревянная броня" in player["inventory"]:
                    player["armor"] = 10
            elif weapons1 == "Кольчуга":
                if "Кольчуга" in player["inventory"]:
                    player["armor"] = 20
            elif weapons1 == "Железная броня":
                if "Железная броня" in player["inventory"]:
                    player["armor"] = 30
            elif weapons1 == "Проклятая броня":
                if "Проклятая броня" in player["inventory"]:
                    player["armor"] = 40
            elif weapons1 == "Сумеречная броня":
                if "Сумеречная броня" in player["inventory"]:
                    player["armor"] = 50
            else:
                print("Вы не находите никакой брони.")
            weapons2 = input("Выберите оружие которое вы будете использовать:")
            if weapons2 == "Меч":
                if "Меч" in player["inventory"]:
                    player["attack"] = 25
            elif weapons2 == "Копье":
                if "Копье" in player["inventory"]:
                    player["attack"] = 35
            elif weapons2 == "Булава":
                if "Булава" in player["inventory"]:
                    player["attack"] = 50
            elif weapons2 == "Проклятый кенжал":
                if "Проклятый кенжал" in player["inventory"]:
                    player["attack"] = 75
            elif weapons2 == "Проклятое копье":
                if "Проклятое копье" in player["inventory"]:
                    player["attack"] = 100
            elif weapons2 == "Сумеречный меч":
                if "Сумеречный меч" in player["inventory"]:
                    player["attack"] = 150
            elif weapons2 == "Таинственная Булава":
                if "Таинственная Булава" in player["inventory"]:
                    player["attack"] = 500
            else:
                print("Вы не находите никакого оружия")
                player["attack"] = 5
            weapons3 = input("Выберите жетон который вы будете использовать: ")
            if weapons3 == "Жетон радости":
                if "Жетон радости" in player["inventory"]:
                    player["luck"] = 1
            elif weapons3 == "Жетон удачи":
                if "Жетон удачи" in player["inventory"]:
                    player["luck"] = 2
            elif weapons3 == "Жетон леплекона":
                if "Жетон леплекона" in player["inventory"]:
                    player["luck"] = 3
            else:
                print("Вы не нашли никакого жетона")
                player["luck"] = 0
            return player["armor"], player["attack"], player["luck"]
stats_after_weapons = weapons()
sleep(1)
victims = int(input("Выберите кого вы хотите побороть:1-Жрубсень.;2-Неуловимыч."))
while True:
    if victims == 1:
        player['name'] = name
        current_enemy = 1
        round = randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']
        enemy["attack"] -= player["armor"]
        if enemy['attack'] <0:
            enemy["attack"] = 0
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()
        while player['hp'] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                enemy_hp -= player['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}.')
                player['hp'] -= enemy['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            win = 0
            monsters_lower.remove("Жрубсень")
            player["money"] += 150
            break
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
    if victims == 2:
        player['name'] = name
        current_enemy = 2
        round = randint(1, 2)
        enemy = enemies[current_enemy]
        enemy_hp = enemies[current_enemy]['hp']
        enemy["attack"] -= player["armor"]
        if enemy['attack'] <0:
            enemy["attack"] = 0
        print(f'Противник - {enemy["name"]}: {enemy["script"]}')
        input('Enter чтобы продолжить')
        print()
        while player['hp'] > 0 and enemy_hp > 0:
            if round % 2 == 1:
                print(f'{player["name"]} атакует {enemy["name"]}.')
                enemy_hp -= player['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            else:
                print(f'{enemy["name"]} атакует {player["name"]}.')
                player['hp'] -= enemy['attack']
                sleep(1)
                print(f'''{player['name']} - {player['hp']}
        {enemy['name']} - {enemy_hp}''')
                print()
                sleep(1)
            round += 1

        if player['hp'] > 0:
            print(f'Противник - {enemy["name"]}: {enemy["win"]}')
            win = 0
            monsters_lower.remove("Неуловимыч")
            player["money"] += 150
            break
        else:
            print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
def drop():
    if player["luck"] ==  0:
        drop_item="Безделушка"
    if player["luck"] == 1:
        drop_item="Дорогая безделушка"
    if player["luck"] == 2:
        drop_item="Дорогая безделушка"
    if player["luck"] == 3:
        drop_item="Дорогая безделушка"
    return drop_item
drop_item = drop()
def specialized_drop_weapon():
    if player["luck"] == 0 or player["luck"] == 1:
        drop_specialized_item_weapon = ""
    if player["luck"] == 2:
        if win == 1:
            choose = randint(1,2)
            if choose == 1:
                drop_specialized_item_weapon = "Проклятый кенжал"
            if choose == 2:
                drop_specialized_item_weapon = "Проклятое копье"
        else:
            drop_specialized_item_weapon = ""
    if player["luck"] == 3:
        if win ==3:
            drop_specialized_item_weapon = "Сумеречный меч"
        else:
            drop_specialized_item_weapon = ""
    return drop_specialized_item_weapon
def specialized_drop_armor():
    if player["luck"] == 0 or player["luck"] == 1:
        drop_specialized_item_armor = ""
    if player["luck"] == 2:
        if win ==2:
            drop_specialized_item_armor = "Проклятая броня"
        else:
            drop_specialized_item_armor = ""
    if player["luck"] == 3:
        if win ==4:
            drop_specialized_item_armor = "Сумеречная броня"
        else:
            drop_specialized_item_armor = ""
    return drop_specialized_item_armor
drop_specialized_item_weapon = specialized_drop_weapon()
drop_specialized_item_armor = specialized_drop_armor()
if drop_specialized_item_weapon != "" and drop_specialized_item_armor != "" and drop_item != "":
    sleep(1)
    print("Инвентарь пополнен:")
    player["inventory"].append(drop_specialized_item_weapon)
    player["inventory"].append(drop_specialized_item_armor)
    player["inventory"].append(drop_item)
    print(player["inventory"])
def after_win():
    print("Вы идете в больницу, встречаете там Стенфорда")
    sleep(2)
    print("Он вас лечит")
    player["hp"] =100
    sleep(1)
    print(player["hp"])
    sleep(1)
    print("Вы идите в обход рынок")
    sleep(1)
    choise = int(input("Вы можете пойти 1-:Комната отдыха.;2-Пойти сразу на рынок."))
    if choise == 1:
        print("Вы идите в комнату отдыха")
        sleep(2)
        print("Вы присаживаетесь за стойку продажи")
        sleep(2)
        print("Вы расслабляетесь")
        sleep(2)
        print("Показатели персонажа:")
        sleep(1)
        print(player)
        sleep(2)
        purchase_prise = {"Безделушка":250,"Дорогая безделушка":500, "Меч":250,"Копье":500,"Булава":750,"Проклятый кенжал":1250,"Проклятое копье":1500,"Сумеречный меч":2000,"Деревянная броня":250,"Кольчуга":500,"Железная броня":750,"Проклятая броня":1500,"Сумеречная броня":2000,"Жетон радости":250,"Жетон удачи":500,"Жетон леплекона":1000}
        print(purchase_prise)
        sleep(1)
        print(player["inventory"])
        tipes_of_sale = int(input("""Сколько Товаров вы хочите продать всего товаров:16
Товары это (Копье, Проклятый кенжал, Безделушка, Кольчуга и тд.)"""))
        for i in range(tipes_of_sale):

            print("Вашь инвентарь",player["inventory"])
            sale = input("""Введите название товара на продажу (с учетом пробелов):""")
            if sale == "Безделушка":
                if "Безделушка" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Безделушка")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Безделушка")
                        player["money"] += 250
            if sale == "Дорогая безделушка":
                if "Дорогая безделушка" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Дорогая безделушка")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Дорогая безделушка")
                        player["money"] += 500
            if sale == "Меч":
                if "Меч" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Меч")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Меч")
                        player["money"] += 250
            if sale == "Копье":
                if "Копье" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Копье")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Копье")
                        player["money"] += 500
            if sale == "Булава":
                if "Булава" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Булава")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Булава")
                        player["money"] += 750
            if sale == "Проклятый кенжал":
                if "Проклятый кенжал" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Проклятый кенжал")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Проклятый кенжал")
                        player["money"] += 1250
            if sale == "Проклятое копье":
                if "Проклятое копье" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Проклятое копье")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Проклятое копье")
                        player["money"] += 1500
            if sale == "Сумеречный меч":
                if "Сумеречный меч" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Сумеречный меч")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Сумеречный меч")
                        player["money"] += 2000
            if sale == "Деревянная броня":
                if "Деревянная броня" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Деревянная броня")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Деревянная броня")
                        player["money"] += 250
            if sale == "Кольчуга":
                if "Кольчуга" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Кольчуга")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Кольчуга")
                        player["money"] += 500
            if sale == "Железная броня":
                if "Железная броня" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Железная броня")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Железная броня")
                        player["money"] += 750
            if sale == "Жетон радости":
                if "Жетон радости" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Жетон радости")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Жетон радости")
                        player["money"] += 250
            if sale == "Жетон удачи":
                if "Жетон удачи" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Жетон удачи")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Жетон удачи")
                        player["money"] += 500
            if sale == "Жетон леплекона":
                if "Жетон леплекона" in player["inventory"]:
                    number_of_sale = player["inventory"].count("Жетон леплекона")
                    for a in range(number_of_sale):
                        player["inventory"].remove("Жетон леплекона")
                        player["money"] += 500
    if choise == 2:
        print("Вы проходите мимо комнаты отдыха.")
    sleep(1)
    buy0 = int(input("""Какую броню вы хочите купить:1-Деревянная броня.;2-Кольчуга.;3-Железная броня.;4-пройти дальше
Впешите(1/2/3/4):"""))
    sleep(1)
    if buy0 == 4:
        print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
    elif buy0==1:
        answer2 = input("Вы хотите купить данную броню?").title()
        if answer2 == "Да":
            if player['money'] >= 500:
                if "Деревянная броня" in goods0:
                    del goods0['Деревянная броня']
                    player['money'] -=500
                    player['inventory'].append('Деревянная броня')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
        if answer2 == "Нет":
            print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
    if buy0 ==2:
        answer2 = input("Вы хотите купить данную броню?").title()
        if answer2 == "Да":
            if player['money'] >= 1000:
                if "Кольчуга" in goods0:
                    del goods0['Кольчуга']
                    player['money'] -=1000
                    player['inventory'].append('Кольчуга')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
        if answer2 == "Нет":
            print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
        if buy0==3:
                answer2 = input("Вы хотите купить данную броню?").title()
        if answer2 == "Да":
            if player['money'] >=1500:
                if "Железная броня" in goods0:
                    del goods0['Железная броня']
                    player['money'] -=1500
                    player['inventory'].append('Железная броня')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца оружием по имени Хард")
        if answer2 == "Нет":
            print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
    sleep(1)
    goods1 = {"Меч":500,"Копье":1000,"Булава":1500}
    print(goods1)
    sleep(1)
    print("Меч увеличивает вашь урон на 20.;Копье увеличивает урона на 30.;Булава увеличивает вашь урон на 45")
    buy1 = int(input("Какое оружие вы хотите купить:1-Меч.;2-Копье.;3-Булава.;4-пройти дальше."))
    sleep(1)
    if buy1 == 4:
        print("Вы проходите дальше, встречаете торговца оружием по имени Хард")
    elif buy1==1:
        answer3 = input("Вы хотите купить данное оружие?").title()
        if answer3 == "Да":
            if player['money'] >= 500:
                if "Меч" in goods1:
                    del goods1['Меч']
                    player['money'] -=500
                    player['inventory'].append('Меч')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
        if answer3 == "Нет":
            print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
    if buy1 ==2:
        answer3 = input("Вы хотите купить данное оружие?").title()
        if answer3 == "Да":
            if player['money'] >= 1000:
                if "Кольчуга" in goods1:
                    del goods1['Копье']
                    player['money'] -=1000
                    player['inventory'].append('Копье')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
        if answer3 == "Нет":
            print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
        if buy1==3:
                answer3 = input("Вы хотите купить данное оружие?").title()
        if answer3 == "Да":
            if player['money'] >=1500:
                if "Булава" in goods1:
                    del goods1['Булава']
                    player['money'] -=1500
                    player['inventory'].append('Булава')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше дальше, встречаете торговца жетонов по имени Виктор")
        if answer3 == "Нет":
            print("Вы проходите дальше, встречаете торговца жетонов по имени Виктор")
    sleep(1)
    goods2 = {"Жетон радости":500,"Жетон удачи":1000,"Жетон леплекона":1500}
    print(goods2)
    sleep(1)
    print("""Жетон радости дает возможность выпадения более дорогих безделушек и увелечение дропа монет.;Жетон удачи дает шанц на выпадение ценных вещей.;Жетон леплекона даец шанц на выпадение лучших вещей""")
    buy2={"Какой жетон вы хотите купить:1-Жетон радости.;2Жетон удачи-.;3Жетон леплекона-.;4-пройти дальше"}
    sleep(1)
    if buy2 == 4:
        print("Вы проходите дальше, и поподаете в опасную зону ")
    elif buy2==1:
        answer4 = input("Вы хотите купить данный жетон?").title()
        if answer4 == "Да":
            if player['money'] >= 500:
                if "Жетон радости" in goods2:
                    del goods2['Жетон радости']
                    player['money'] -=500
                    player['inventory'].append('Жетон радости')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше, и поподаете в опасную зону")
        if answer4 == "Нет":
            print("Вы проходите дальше, и поподаете в опасную зону")
    if buy2 ==2:
        answer4 = input("Вы хотите купить данный жетон?").title()
        if answer4 == "Да":
            if player['money'] >= 1000:
                if "Жетон удачи" in goods2:
                    del goods2['Жетон удачи']
                    player['money'] -=1000
                    player['inventory'].append('Жетон удачи')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше, и поподаете в опасную зону")
        if answer4 == "Нет":
            print("Вы проходите дальше, и поподаете в опасную зону")
        if buy2==3:
                answer4 = input("Вы хотите купить данный жетон?").title()
        if answer4 == "Да":
            if player['money'] >=1500:
                if "Жетон леплекона" in goods2:
                    del goods2['Жетон леплекона']
                    player['money'] -=1500
                    player['inventory'].append('Жетон леплекона')
                    print(player)
                    sleep(1)
                    print("Вы идете дальше, и поподаете в опасную зону")
        if answer4 == "Нет":
            print("Вы проходите дальше, и поподаете в опасную зону")
        return player
sleep(1)
stats_after_firts_win = after_win()
print("Ваши показатели:",player)
sleep(2)
print("Доступные враги:",monsters_lower)
sleep(2)
weapons()
stats_after1_weapons = weapons()
if "Неуловимыч" in monsters_lower:
    while True:
            player['name'] = name
            current_enemy = 2
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                round += 1

            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 0
                monsters_lower.remove("Неуловимыч")
                player["money"] += 150
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
if "Жрубсень" in monsters_lower:
    while True:
            player['name'] = name
            current_enemy = 1
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                round += 1

            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 0
                monsters_lower.remove("Жрубсень")
                player["money"] += 150
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
drop_item()
drop_item1 = drop_item()
drop_specialized_item_weapon()
drop_specialized_item_weapon1 = drop_specialized_item_weapon()
drop_specialized_item_armor()
drop_specialized_item_armor1 = drop_specialized_item_armor()
if drop_specialized_item_weapon != "" and drop_specialized_item_armor != "" and drop_item1 != "":
    sleep(1)
    print("Инвентарь пополнен:")
    player["inventory"].append(drop_specialized_item_weapon1)
    player["inventory"].append(drop_specialized_item_armor1)
    player["inventory"].append(drop_item1)
    print(player["inventory"])
#Спросить: так будет работать?
after_win()
stats_after_second_win = after_win()
print("Ваши показатели:",player)
sleep(2)
monsters_midle = ["Найтсталкер","Лич"]
print("Доступные враги:",monsters_midle)
sleep(2)
weapons()
stats_after2_weapons = weapons()
fight = int(input("Введите порядковый номер врага:1-Найтсталкер.;2-Лич."))
if fight == 1:
    while True:
            player['name'] = name
            current_enemy = 3
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                round += 1

            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 2
                monsters_midle.remove("Найтсталкер")
                player["money"] += 500
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
if fight == 2:
    while True:
            player['name'] = name
            current_enemy = 4
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                round += 1

            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 1
                monsters_midle.remove("Лич")
                player["money"] += 500
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
drop_item()
drop_item2 = drop_item()
drop_specialized_item_weapon()
drop_specialized_item_weapon2 = drop_specialized_item_weapon()
drop_specialized_item_armor()
drop_specialized_item_armor2 = drop_specialized_item_armor()
if drop_specialized_item_weapon2 != "" and drop_specialized_item_armor2 != "" and drop_item2 != "":
    sleep(1)
    print("Инвентарь пополнен:")
    player["inventory"].append(drop_specialized_item_weapon2)
    player["inventory"].append(drop_specialized_item_armor2)
    player["inventory"].append(drop_item2)
    print(player["inventory"])
after_win()
stats_after_third_win = after_win()
print("Ваши показатели:",player)
sleep(2)
print("Доступные враги:",monsters_midle)
sleep(2)
weapons()
stats_after3_weapons = weapons()
if "Найтсталкер" in monsters_midle:
    while True:
            player['name'] = name
            current_enemy = 3
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                    if player["hp"] <= enemy['attack']:
                        print("Вы уворачиваетесь от атаки и наносите критический урон!")
                        enemy_hp = 0
                round += 1


            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 2
                monsters_midle.remove("Найтсталкер")
                player["money"] += 500
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
if "Лич" in monsters_midle:
    while True:
            player['name'] = name
            current_enemy = 4
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                    if player["hp"] <= enemy['attack']:
                        print("Вы уворачиваетесь от атаки и наносите критический урон!")
                        enemy_hp = 0
                round += 1
                
            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 1
                monsters_midle.remove("Лич")
                player["money"] += 500
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
drop_item()
drop_item3 = drop_item()
drop_specialized_item_weapon()
drop_specialized_item_weapon3 = drop_specialized_item_weapon()
drop_specialized_item_armor()
drop_specialized_item_armor3 = drop_specialized_item_armor()
if drop_specialized_item_weapon3 != "" and drop_specialized_item_armor3 != "" and drop_item3 != "":
    sleep(1)
    print("Инвентарь пополнен:")
    player["inventory"].append(drop_specialized_item_weapon3)
    player["inventory"].append(drop_specialized_item_armor3)
    player["inventory"].append(drop_item3)
    print(player["inventory"])
after_win()
stats_after_fourth_win = after_win()
print("Ваши показатели:",player)
sleep(2)
monsters_hight_firts = ["Вольдемар"]
print("Доступные враги:",monsters_hight_firts)
sleep(2)
weapons()
stats_after4_weapons = weapons()
while True:
            player['name'] = name
            current_enemy = 5
            round = randint(1, 2)
            enemy = enemies[current_enemy]
            enemy_hp = enemies[current_enemy]['hp']
            enemy["attack"] -= player["armor"]
            if enemy['attack'] <0:
                enemy["attack"] = 0
            print(f'Противник - {enemy["name"]}: {enemy["script"]}')
            input('Enter чтобы продолжить')
            print()
            while player['hp'] > 0 and enemy_hp > 0:
                if round % 2 == 1:
                    print(f'{player["name"]} атакует {enemy["name"]}.')
                    enemy_hp -= player['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                else:
                    print(f'{enemy["name"]} атакует {player["name"]}.')
                    player['hp'] -= enemy['attack']
                    sleep(1)
                    print(f'''{player['name']} - {player['hp']}
            {enemy['name']} - {enemy_hp}''')
                    print()
                    sleep(1)
                    if player["hp"] <= enemy['attack']:
                        print("Вы уворачиваетесь от атаки и наносите критический урон!")
                        enemy_hp = 0
                round += 1

            if player['hp'] > 0:
                print(f'Противник - {enemy["name"]}: {enemy["win"]}')
                win = 3
                monsters_hight_firts.remove("Вольдемар")
                player["money"] += 1000
                break
            else:
                print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
drop_item()
drop_item4 = drop_item()
drop_specialized_item_weapon()
drop_specialized_item_weapon4 = drop_specialized_item_weapon()
drop_specialized_item_armor()
drop_specialized_item_armor4 = drop_specialized_item_armor()
if drop_specialized_item_weapon4 != "" and drop_specialized_item_armor4 != "" and drop_item4 != "":
    sleep(1)
    print("Инвентарь пополнен:")
    player["inventory"].append(drop_specialized_item_weapon4)
    player["inventory"].append(drop_specialized_item_armor4)
    player["inventory"].append(drop_item4)
    print(player["inventory"])
import Диалог3
