from character import Enemy

lyle = Enemy("Lyle","An evil person")
lyle.describe()


lyle.set_conversation("Hello my name is lyle")

lyle.talk()

lyle.set_weakness("explosives")

lyle.get_weakness()

print("What will you fight with")
fight_with = input()
lyle.fight(fight_with)
