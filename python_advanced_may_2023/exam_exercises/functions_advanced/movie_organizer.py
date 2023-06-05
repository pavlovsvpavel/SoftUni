from collections import defaultdict


def movie_organizer(*args):
    result = []
    genre_dict = defaultdict(list)

    for movie, genre in args:
        genre_dict[genre].append(movie)

    sorted_dict = dict(sorted(genre_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    for (gen, movies) in sorted_dict.items():
        result.append(f"{gen} - {len(movies)}")

        for s_movie in sorted(movies, reverse=False):
            result.append(f"* {s_movie}")

    return "\n".join(result)


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("The Matrix", "Sci-fi")))
