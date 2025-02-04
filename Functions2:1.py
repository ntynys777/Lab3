def is_high_rated(movie):
    return movie["imdb"] > 5.5


print(is_high_rated({"name": "Hitman", "imdb": 6.3, "category": "Action"}))  
print(is_high_rated({"name": "AlphaJet", "imdb": 3.2, "category": "War"}))  
