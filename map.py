from inventory import show_inventory
from player import Player
from monster import create_goblin, create_dragon
from combat import combat
from utils import quit_game
import random

GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

BOSS_LOCATION = {"x": 2, "y": 2}
player_position = {"x": 0, "y": 0}

def move_player(player):
    global player_position

    while True:
        command = input("Que voulez-vous faire ? (East/West/North/South/Inventory/Stats/Quitter): ").lower()
        
        if command in ["east", "west", "north", "south"]:
            if command == "east":
                player_position["x"] += 1
            elif command == "west":
                player_position["x"] -= 1
            elif command == "north":
                player_position["y"] += 1
            elif command == "south":
                player_position["y"] -= 1
            
            print(f"{player.name} marche vers le {command.capitalize()}.")
            result = encounter_event(player)
            
            if result in ["boss_defeated", "defeated"]:
                return result

        elif command == "inventory":
            show_inventory(player)
        elif command == "stats":
            player.show_stats()
        elif command == "quitter":
            quit_game()
        else:
            print("Commande invalide. Essayez encore.")

def encounter_event(player):
    global player_position

    if player_position == BOSS_LOCATION:
        print(f"\n🔥 {CYAN}Vous avez trouvé le Dragon ! Préparez-vous à combattre le boss final !{RESET}")
        dragon = create_dragon()
        return combat(player, dragon)
    
    else:
        event = random.choice(["monstre", "objet", "rien"])

        if event == "monstre":
            monster_level = max(1, player.level - 1)
            goblin = create_goblin(level=monster_level)
            print(f"\n👹 Un gobelin de niveau {monster_level} apparaît !")
            return combat(player, goblin)
        elif event == "objet":
            found_item = random.choice(["Potion", "Attack Boost", "Defense Boost"])
            print(f"\n🎁 {GREEN}{player.name} trouve un {found_item}!{RESET}")
            player.inventory.append(found_item)
        else:
            print("\n🌲 Rien d'intéressant ici...")
