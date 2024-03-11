function solve(array) {
    class Song {
        constructor(songType, songName, songTime){
            this.songType = songType;
            this.songName = songName;
            this.songTime = songTime;
        }
    }

    let songs = [];
    let numberOfSongs = array.shift();
    let typeOfSong = array.pop();

    for (let i = 0; i < numberOfSongs; i++) {
        let [type, name, time] = array[i].split("_");

        songs.push(new Song(type, name, time))
    }

    if (typeOfSong === 'all') {
        songs.forEach((object) => console.log(object.songName));
    } else {
        let filteredSongsBySongType = songs.filter((object) => object.songType === typeOfSong);
        filteredSongsBySongType.forEach((object => console.log(object.songName)));
    }
}


solve([4,
    'favourite_DownTown_3:14',
    'listenLater_Andalouse_3:24',
    'favourite_In To The Night_3:58',
    'favourite_Live It Up_3:48',
    'listenLater']
    )

solve([3,
    'favourite_DownTown_3:14',
    'favourite_Kiss_4:16',
    'favourite_Smooth Criminal_4:01',
    'favourite']
    )

solve([2,
    'like_Replay_3:15',
    'ban_Photoshop_3:48',
    'all']
    )