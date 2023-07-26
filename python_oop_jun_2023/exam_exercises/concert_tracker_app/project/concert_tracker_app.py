from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @staticmethod
    def __check_for_band_members_needed_skills_to_play_at_concert(band: Band, concert: Concert):
        can_start_concert = False
        current_skills = []

        for member in band.members:
            current_skills.extend(member.skills)

        if concert.VALID_GENRES_SKILLS[concert.genre].issubset(set(current_skills)):
            can_start_concert = not can_start_concert

        return can_start_concert

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        if musician_type not in ConcertTrackerApp.VALID_MUSICIANS.keys():
            raise ValueError("Invalid musician type!")

        for musician in self.musicians:
            if musician.name == name:
                raise Exception(f"{name} is already a musician!")

        new_musician = ConcertTrackerApp.VALID_MUSICIANS[musician_type](name, age)

        self.musicians.append(new_musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        for band in self.bands:
            if band.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)

        self.bands.append(new_band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        for concert in self.concerts:
            if concert.place == place:
                raise Exception(f"{place} is already registered for {concert.genre} concert!")

        new_concert = Concert(genre, audience, ticket_price, expenses, place)

        self.concerts.append(new_concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        for musician in self.musicians:
            if musician.name == musician_name:
                break

        else:
            raise Exception(f"{musician_name} isn't a musician!")

        for band in self.bands:
            if band.name == band_name:
                break

        else:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        for band in self.bands:
            if band.name == band_name:
                break

        else:
            raise Exception(f"{band_name} isn't a band!")

        for musician in self.musicians:
            if musician.name == musician_name and musician in band.members:
                break

        else:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        current_band = next(filter(lambda x: x.name == band_name, self.bands))

        types_of_musicians_in_band = set(map(lambda x: x.__class__.__name__, current_band.members))

        if not set(ConcertTrackerApp.VALID_MUSICIANS.keys()).issubset(types_of_musicians_in_band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        current_concert = next(filter(lambda x: x.place == concert_place, self.concerts))

        if not self.__check_for_band_members_needed_skills_to_play_at_concert(current_band, current_concert):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (current_concert.audience * current_concert.ticket_price) - current_concert.expenses

        return f"{band_name} gained {profit:.2f}$ from the {current_concert.genre} concert in {concert_place}."
