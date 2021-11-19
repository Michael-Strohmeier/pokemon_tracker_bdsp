import pokemon_finder as poke

if __name__ == "__main__":
    pf = poke.PokemonFinder()

    print("\nRemaining pokemon in location:")
    print("\tl LOCATION_NAME\n")

    print("Add pokemon to found pokemon list:")
    print("\ta POKEMON_NAME\n")

    print("Print game locations:")
    print("\tg\n")

    print("Check if pokemon already found:")
    print("\tf POKEMON_NAME\n")

    s = input("Enter command: ")
    while s != "q":
        arr = s.split(" ")
        command = arr[0]
        if command == "l":
            print(pf.remaining_in_location(" ".join(arr[1:])), "\n")
        if command == "a":
            print(pf.add_pokemon(arr[1]))
        if command == "g":
            print(pf.get_locations(), "\n")
        if command == "f":
            print(pf.is_found(arr[1]))

        s = input("Enter command: ")
