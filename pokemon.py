import random

# Define a simple Pokémon class
class Pokemon:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves

    def attack(self, move, opponent):
        damage = self.moves[move]
        opponent.health -= damage
        return damage

# Define Pokémon
pikachu = Pokemon("Pikachu", 100, {"Thunderbolt": 20, "Quick Attack": 10, "Iron Tail": 15})
charmander = Pokemon("Charmander", 100, {"Flamethrower": 25, "Scratch": 10, "Ember": 15})

# Battle function
def battle(pokemon1, pokemon2):
    print(f"A wild {pokemon2.name} appeared! {pokemon1.name}, I choose you!")

    while pokemon1.health > 0 and pokemon2.health > 0:
        print("\nYour turn!")
        print(f"{pokemon1.name}'s Moves:")
        for i, move in enumerate(pokemon1.moves.keys(), 1):
            print(f"{i}. {move}")

        try:
            choice = int(input("Choose a move (1-3): ")) - 1
            move = list(pokemon1.moves.keys())[choice]
        except (ValueError, IndexError):
            print("Invalid choice! You missed your turn.")
            move = None

        if move:
            damage = pokemon1.attack(move, pokemon2)
            print(f"{pokemon1.name} used {move}! It dealt {damage} damage.")

        if pokemon2.health <= 0:
            print(f"{pokemon2.name} fainted! You win!")
            break

        print("\nOpponent's turn!")
        opponent_move = random.choice(list(pokemon2.moves.keys()))
        damage = pokemon2.attack(opponent_move, pokemon1)
        print(f"{pokemon2.name} used {opponent_move}! It dealt {damage} damage.")

        if pokemon1.health <= 0:
            print(f"{pokemon1.name} fainted! You lose!")
            break

        print(f"\n{pokemon1.name}'s health: {pokemon1.health}")
        print(f"{pokemon2.name}'s health: {pokemon2.health}")

# Start the battle
battle(pikachu, charmander)
