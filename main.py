
class Dragon:
    def __init__(self, dragon_type, color, element, wings, tail, size, name):
        self.dragon_type = dragon_type
        self.color = color
        self.element = element
        self.wings = wings
        self.tail = tail
        self.size = size
        self.name = name

    def display_dragon(self):
        print("\n--- Dragon Card ---")
        print(f"Name: {self.name}")
        print(f"Type: {self.dragon_type}")
        print(f"Color: {self.color}")
        print(f"Element: {self.element}")
        print(f"Wings: {self.wings}")
        print(f"Tail: {self.tail}")
        print(f"Size: {self.size}")
        print("-------------------")

    def save_dragon(self):
        filename = f"{self.name.lower().replace(' ', '_')}.txt"
        with open(filename, "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Type: {self.dragon_type}\n")
            f.write(f"Color: {self.color}\n")
            f.write(f"Element: {self.element}\n")
            f.write(f"Wings: {self.wings}\n")
            f.write(f"Tail: {self.tail}\n")
            f.write(f"Size: {self.size}\n")
        print(f"Dragon {self.name} saved to {filename}")

def create_dragon():
    print("\n--- Create Your Dragon ---")
    dragon_type = input("Enter dragon type (e.g., Fire, Ice, Shadow, Water): ")
    color = input("Enter dragon color: ")
    element = input("Enter dragon element (e.g., Fire, Ice, Lightning, Poison, Darkness): ")
    wings = input("Enter wing type (e.g., Large, Small, Webbed, Feathered): ")
    tail = input("Enter tail type (e.g., Long, Short, Spiked, Flaming): ")
    size = input("Enter dragon size (e.g., Small, Medium, Large, Colossal): ")
    name = input("Enter dragon name: ")

    return Dragon(dragon_type, color, element, wings, tail, size, name)

def main():
    while True:
        print("\n1. Create a new dragon")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            my_dragon = create_dragon()
            my_dragon.display_dragon()
            save_choice = input("Save this dragon? (yes/no): ")
            if save_choice.lower() == 'yes':
                my_dragon.save_dragon()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
