import json
import requests

def bestInGenre(genre):
    best_movie_name = ""
    best_rating = 0
    best_movie_names_with_tie = []

    for i in range(1, 11):
        url = f"https://jsonmock.hackerrank.com/api/tvseries?page={i}"
        response = requests.get(url)
        temp1 = json.loads(response.content)
        print(temp1)
        for movie in temp1['data']:
            if genre in movie['genre'] and 'imdb_rating' in movie:
                imdb_rating = float(movie['imdb_rating'])
                if imdb_rating > best_rating:
                    best_rating = imdb_rating
                    best_movie_name = movie['name']
                    best_movie_names_with_tie.append(best_movie_name)
                elif imdb_rating == best_rating:
                    best_movie_names_with_tie.append(movie['name'])
                elif imdb_rating < best_rating:
                    continue

    print(best_movie_names_with_tie)

genre_to_search ='Music'  #  this to the genre you want to search for
best_movie = bestInGenre(genre_to_search)

if best_movie:
    print(f"The best-rated {genre_to_search} movie is '{best_movie}'.")
else:
    print(f"No {genre_to_search} movie found.")




