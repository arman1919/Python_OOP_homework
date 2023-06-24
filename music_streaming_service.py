
class song:

    def __init__(self,title,artist,length) -> None:
        self.title = title
        self.artist = artist
        self.length = length



class album:
    def __init__(self,title, artist,release_date) -> None:
        self.title = title
        self.artist = artist
        self.release_date = release_date
        self.album_song = {}


class playlist:
    def __init__(self,name,songs_included) -> None:
        self.name = name
        self.songs_included = songs_included



class  music_streaming_service:
    def __init__(self) -> None:
        self.playlists = {}
        self.albums = {}
        self.songs = {}
        self.play_history = []
        

    
    def careate_playlist(self,name:str,songs_included = {}):
        self.playlists[name] = playlist(name,songs_included)


    def careate_album(self,title:str,artist:str,release_date:int):
        
        self.albums[title] = album(title,artist,release_date)


    def add_song(self,title:str,artist:str,length:int):
        self.songs[title] = song(title,artist,length)
    
    def serach_song(self,name:str):
        if name in self.songs:

            print(f"Playing song '{name}' | lenght- {self.songs[name].length}")
        else:
            print("not songs with that name")

    def add_song_to_playlist(self,name_playlist,song):
        if name_playlist in self.playlists:
            self.playlists[name_playlist].songs_included[song.name] = song
        else:
            print("not playlist with that name")

    def dell_song_to_playlist(self,name_playlist,song):

        if name_playlist in self.playlists:
            if song.name in self.playlists[name_playlist].songs_included:
                self.playlists[name_playlist].songs_included.pop(song.name)
                
            else:
                print("not songs with that name")

        else:
            print("not playlist with that name")


    def add_albom(self,title, artist,release_date):
        self.albums[title] = album(title,artist,release_date)

        for i in self.songs:
            if self.songs[i].artist == artist:
                self.albums[title].album_song[self.songs[i].title] = self.songs[i]
    
    def paly(self,name):
        if name in self.songs:
            song = self.songs[name]
            print(f"Played {song.artist} - {name} | length - {song.length}")
            self.play_history.append(song)

        elif name in self.playlists:
            playlist = self.playlists[name]
            print(f"Played playlist {name} | {len(playlist.songs_included)} - songs")
            for i in playlist.songs_included:
                self.play_history.append(playlist.songs_included[i])
        elif name in self.albums:
            album = self.albums[name]

            print(f"Played album {name} | artist - {album.artist} | release_date - {album.release_date} |{len(album.album_song)} - songs")
            
            for i in album.album_song:
                self.play_history.append(album.album_song[i])
            
            
            
muz_palyer = music_streaming_service()
muz_palyer.add_song("Mi gna","Tatul",150)
muz_palyer.add_song("Anapati arev","Tata",90)

muz_palyer.add_albom("Rabiz","Tatul","25.12.2003")

print(muz_palyer.albums["Rabiz"].album_song["Mi gna"].artist)

muz_palyer.paly("Mi gna")
print()
muz_palyer.paly("Rabiz")
