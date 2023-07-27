from typing import List, Optional
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    registered_horses = []

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def __check_for_valid_jockey(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

        raise Exception(f"Jockey {name} could not be found!")

    def __check_for_valid_race_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

        raise Exception(f"Race {race_type} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int) -> Optional[str]:
        if horse_name in HorseRaceApp.registered_horses:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.VALID_HORSE_TYPES:
            current_horse = HorseRaceApp.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(current_horse)
            HorseRaceApp.registered_horses.append(current_horse.name)

            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int) -> str:
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")

        self.jockeys.append(Jockey(jockey_name, age))

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str) -> str:
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

        self.horse_races.append(HorseRace(race_type))

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str) -> str:
        current_jockey = self.__check_for_valid_jockey(jockey_name)

        try:
            current_horse = [x for x in self.horses if x.__class__.__name__ == horse_type and not x.is_taken][-1]

        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if current_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        current_jockey.horse = current_horse
        current_horse.is_taken = not current_horse.is_taken

        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str) -> str:
        current_race = self.__check_for_valid_race_type(race_type)
        current_jockey = self.__check_for_valid_jockey(jockey_name)

        if current_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if current_jockey in current_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str) -> str:
        current_race = self.__check_for_valid_race_type(race_type)

        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        horse_winner_obj = sorted(self.horses, key=lambda x: -x.speed)[0]
        horse_winner_name = horse_winner_obj.name
        horse_winner_high_speed = horse_winner_obj.speed

        jockey_winner = ""

        for jockey in current_race.jockeys:
            if jockey.horse.speed == horse_winner_high_speed:
                jockey_winner += jockey.name
                break

        return f"The winner of the {race_type} race, " \
               f"with a speed of {horse_winner_high_speed}km/h is {jockey_winner}! " \
               f"Winner's horse: {horse_winner_name}."
