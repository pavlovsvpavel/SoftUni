from typing import List, Tuple

from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = [*songs]

    def add_song(self, song: Song) -> str:
        if song in self.songs:
            return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        try:
            current_song = next(filter(lambda x: x.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(current_song)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self) -> str:
        all_songs = '\n'.join([f"== {song.get_info()}" for song in self.songs])

        return f"Album {self.name}\n" + \
               f"{all_songs}\n"
