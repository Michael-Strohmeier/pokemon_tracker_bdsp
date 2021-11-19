import pandas as pd
import os


class PokemonFinder:
    def __init__(self):
        self.df = pd.read_csv("bdsp_pokemon_loc.csv")
        self.df["Location"] = [location.split("\n") for location in self.df["Location"]]

        self.found_pokemon = None
        if os.path.isfile("found_pokemon.txt"):
            with open("found_pokemon.txt", "r") as f:
                self.found_pokemon = set(f.read().split("\n"))
        else:
            self.found_pokemon = set()

        self.location_dict = None
        self.get_location_dict()

    def get_location_dict(self):
        if self.location_dict is not None:
            return self.location_dict

        self.location_dict = dict()

        for pokemon, location_list in zip(self.df["Pokemon"], self.df["Location"]):
            for location in location_list:
                if location in self.location_dict:
                    self.location_dict[location].append(pokemon)
                else:
                    self.location_dict[location] = [pokemon]

        return self.location_dict

    def get_locations(self):
        arr = list(self.location_dict.keys())
        arr.sort()

        return arr

    def add_pokemon(self, pokemon):
        self.found_pokemon.add(pokemon)

        with open("found_pokemon.txt", "w") as f:
            for pokemon in self.found_pokemon:
                f.write(f"{pokemon}\n")

        return f"Added Pokemon: {pokemon}\n"

    def is_found(self, pokemon):
        if pokemon in self.found_pokemon:
            return f"{pokemon} has already been found.\n"
        return f"{pokemon} has NOT been found!\n"

    def remaining_in_location(self, location):
        if location not in self.location_dict:
            return "Location not found."

        arr = []
        for pokemon in self.location_dict[location]:
            if pokemon not in self.found_pokemon:
                arr.append(pokemon)

        return arr
