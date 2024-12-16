import random
from utils import quit_game
from inventory import use_item

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def combat(player, monster):
    print(f"\n{'='*40}")
    print(f"⚔️  {CYAN}Un {monster.name} de niveau {monster.level} est devant vous ! ⚔️{RESET}")
    print(f"{'='*40}\n")

    while monster.hp > 0 and player.hp > 0:
        print(f"{GREEN}Vos HP : {player.hp}{RESET} | {RED}HP du {monster.name} : {monster.hp}{RESET}")
        print("\nQue voulez-vous faire ?")
        print("1. Attaquer")
        print("2. Utiliser un objet")
        print("3. Fuir\n")
        
        action = input("Votre choix : ")

        if action == "1":
            damage_to_monster = 0
            
            if random.random() < 0.1:
                print("\n❌ Vous avez raté votre attaque !")
            elif random.random() < 0.2:
                damage_to_monster = max(player.attack * 2 - monster.defense, 0)
                print(f"\n💥 {YELLOW}Coup critique !{RESET}")
            else:
                damage_to_monster = max(player.attack - monster.defense, 0)
            
            monster.hp -= damage_to_monster
            print(f"\n{YELLOW}Vous infligez {damage_to_monster} dégâts au {monster.name}.{RESET}")

            if monster.hp > 0:
                print(f"{RED}Il reste {monster.hp} HP au {monster.name}.{RESET}")
                damage_to_player = max(monster.attack - player.defense, 0)
                player.hp -= damage_to_player
                print(f"Le {monster.name} vous attaque et vous inflige {damage_to_player} dégâts.")
                print(f"{GREEN}Il vous reste {player.hp} HP.{RESET}")
                
                if player.hp <= 0:
                    print("\n💀 Vous avez été vaincu... 😢")
                    print(f"{'='*40}\n")
                    return 'defeated'
            else:
                print(f"\n🎉 {GREEN}Vous avez vaincu le {monster.name}!{RESET}")
                player.gain_xp(50 * monster.level)
                if monster.name == "Dragon":
                    print(f"{YELLOW}🏆 Félicitations, vous avez vaincu le boss final ! Le jeu est terminé.{RESET}")
                    print(f"{'='*40}\n")
                    return 'boss_defeated'

        elif action == "2":
            use_item(player)

        elif action == "3":
            print("\n🏃 Vous prenez la fuite...")
            break

        else:
            print("\n❗ Action invalide. Essayez encore.")

    print(f"{'='*40}\n")
