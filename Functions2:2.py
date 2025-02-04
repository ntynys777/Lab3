def high_rated_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


movies_list = [
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "The Matrix", "imdb": 8.7, "category": "Sci-Fi"},
]

print(high_rated_movies(movies_list))
