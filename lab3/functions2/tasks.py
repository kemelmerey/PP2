#You are given the following dictionary called "movies": 

# Dictionary of movies
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]
#Do the following tasks:

#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def above_5_5(movie):
    return movie["imdb"] > 5.5
#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def movies_above_5_5(movies):
    return [movie for movie in movies if above_5_5(movie)]
#Write a function that takes a category name and returns just those movies under that category.
def movies_in_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
#Write a function that takes a list of movies and computes the average IMDB score.
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
#Write a function that takes a category and computes the average IMDB score.
def average_imdb_score_in_category(movies, category):
    category_movies = movies_in_category(movies, category)
    return average_imdb_score(category_movies)
#example
print(above_5_5({"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}))
print(movies_above_5_5(movies))
print(movies_in_category(movies, "Romance"))
print(average_imdb_score(movies))
print(average_imdb_score_in_category(movies, "Romance"))