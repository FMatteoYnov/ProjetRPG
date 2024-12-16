from player import Player
from map import move_player
from utils import quit_game

YELLOW = "\033[93m"
RESET = "\033[0m"

def main_menu():
    print(f"\n{'='*40}")
    print(f"{YELLOW}🏰 Bienvenue dans le RPG de Bob ! 🏰{RESET}")
    print(f"{'='*40}")
    print("1. Nouvelle partie")
    print("2. Quitter\n")
    
    choice = input("Choisissez une option : ")
    
    if choice == "1":
        start_game()
    elif choice == "2":
        quit_game()
    else:
        print("\n❗ Choix invalide. Réessayez.")
        main_menu()

def start_game():
    player_name = input("\nEntrez votre nom : ")
    player = Player(player_name)
    print(f"\n✨ {YELLOW}Bienvenue {player_name} ! Votre aventure commence.{RESET}\n")
    
    result = move_player(player)
    if result in ["boss_defeated", "defeated"]:
        main_menu()

if __name__ == "__main__":
    main_menu()
