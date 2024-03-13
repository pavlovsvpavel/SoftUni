function solve(input) {
    function getMovieName(string) {
        let movieName = string.substring(0, index - 1);
        return movieName;
    }

    let allMovies = [];
    

    for (let element of input) {
        let movieName = "";
        let director = "";
        let date = "";  

        if (element.includes('addMovie')) {
            movieName = element.substring('addMovie'.length + 1);
            allMovies.push({
                'name': movieName,
            });

        } else if (element.includes('directedBy')) {
            index = element.indexOf("directedBy");
            movieName = getMovieName(element);
            director = element.substring(index + "directedBy".length + 1);
            
        } else if (element.includes('onDate')) {
            index = element.indexOf("onDate");
            movieName = getMovieName(element);
            date = element.substring(index + "onDate".length + 1);
        }

        for (const movie of allMovies) {
            if (movie['name'] === movieName) {
                if (director) {
                    movie['director'] = director;
                } else if (date) {
                    movie['date'] = date;
                } 
            }
        } 
    }

    // for (const movie of allMovies) {
    //     let values = Object.values(movie)
    //     if (values.length === 3) {
    //         console.log(JSON.stringify(movie));
    //     }
    // }

    allMovies
        .filter(movie => movie.director && movie.date)
        .forEach(movie => console.log(JSON.stringify(movie)));
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ])

solve ([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    )