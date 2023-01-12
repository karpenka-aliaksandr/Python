
def damage_armor(play,enem):
    return enem['damage'] / play['armor']
    

def attack(play,enem):
    play['health']-=damage_armor(play,enem)

player={'name':'player','health': 100, 'damage':80,'armor':1.5}
enemy={'name':'enemy','health': 100, 'damage':60,'armor':1.2}
print(player)
print(enemy)

attack(player,enemy)
print(player)
print(enemy)

attack(enemy,player)
print(player)
print(enemy)