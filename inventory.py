GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def use_item(player):
    if not player.inventory:
        print("🔒 Votre inventaire est vide.")
    else:
        print("\n📦 Votre inventaire : ")
        for item in player.inventory:
            print(f" - {YELLOW}{item}{RESET}")
        
        item = input("\nQuel objet voulez-vous utiliser ? ")

        if item == "Potion":
            player.hp += 20
            print(f"\n{GREEN}🍀 Vous utilisez une Potion et regagnez 20 HP.{RESET}")
            player.inventory.remove(item)
        
        elif item == "Attack Boost":
            player.attack += 5
            print(f"\n🗡️  {YELLOW}Vous utilisez un Boost d'Attaque. Attaque augmentée de 5 pour ce combat.{RESET}")
            player.inventory.remove(item)
        
        elif item == "Defense Boost":
            player.defense += 5
            print(f"\n🛡️  {YELLOW}Vous utilisez un Boost de Défense. Défense augmentée de 5 pour ce combat.{RESET}")
            player.inventory.remove(item)
        
        else:
            print("\n❌ Objet invalide ou non trouvé dans l'inventaire.")

def show_inventory(player):
    if not player.inventory:
        print("🔒 Votre inventaire est vide.")
    else:
        print(f"\n{player.name}'s {GREEN}Inventaire{RESET} :")
        for item in player.inventory:
            print(f" - {YELLOW}{item}{RESET}")
