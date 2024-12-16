class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.xp = 0
        self.inventory = ["Couteau"]
        self.xp_needed = 100

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gagne {amount} XP.")
        if self.xp >= self.xp_needed:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3
        self.xp -= self.xp_needed
        self.xp_needed += 50
        print(f"{self.name} est maintenant au niveau {self.level}!")
        print(f"HP: {self.hp}, Attaque: {self.attack}, Défense: {self.defense}, XP requis: {self.xp_needed}")

    def show_stats(self):
        GREEN = "\033[92m"
        CYAN = "\033[96m"
        RESET = "\033[0m"
        print(f"\n📊 {CYAN}Statistiques de {self.name} :{RESET}")
        print(f"{GREEN}Niveau{RESET}: {self.level}")
        print(f"{GREEN}HP{RESET}: {self.hp}")
        print(f"{GREEN}Attaque{RESET}: {self.attack}")
        print(f"{GREEN}Défense{RESET}: {self.defense}")
        print(f"{GREEN}XP{RESET}: {self.xp}/{self.xp_needed}\n")
