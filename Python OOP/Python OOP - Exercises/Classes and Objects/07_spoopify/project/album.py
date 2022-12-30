from project.song import Song


class Album:
    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        if song in self.songs:
            return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return "Cannot add songs. Album is published."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        try:
            removed_song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        if self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remove(removed_song)
        
        return f"Removed song {removed_song.name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        album_details = [f"Album {self.name}"]
        [album_details.append(f'== {s.get_info()}') for s in self.songs]

        return '\n'.join(album_details)
