def average_imdb_by_category(movies, category):
    filtered_movies = movies_by_category(movies, category)
    return average_imdb(filtered_movies)

print(average_imdb_by_category(movies_list, "Sci-Fi"))  
