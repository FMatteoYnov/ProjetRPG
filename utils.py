def quit_game():
    confirm = input("Êtes-vous sûr de vouloir quitter ? (oui/non): ").lower()
    if confirm == "oui":
        print("Merci d'avoir joué ! À bientôt.")
        exit()
    else:
        print("Retour au jeu.")
