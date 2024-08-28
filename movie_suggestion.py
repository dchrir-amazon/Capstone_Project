import requests
from bs4 import BeautifulSoup
import random

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

LANGUAGE_CODES = {
    "TAMIL" : "ta",
    "TELUGU" : "te",
    "ENGLISH" : "en",
    "HINDI" : "hi"
    
}

def get_movies_by_genre_and_language(genre, language):
    try:
        url = f'https://www.imdb.com/search/title/?genres={genre}&languages={language}'
        print(f"Fetching URL: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content,'html.parser')
        movies = []
        
        for item in soup.find_all(class_='ipc-title__text'):
            movies.append(item.get_text(strip=True))
            
        movies = movies[1:-1]
        
        print(f'Found {len(movies)} movies.')
        return movies
    
    except requests.RequestException as e:
        print(f'An error occured while fetching data:{e}')
        return[]
    
def suggest_movie(genre, language):
    movies= get_movies_by_genre_and_language(genre,language)
    if not movies:
        return "No movies found for this genre and language"
    return random.choice(movies)

if __name__=="__main__":
    genre= input("Enter a genre (Biography, Comedy ,Crime ,Documentary, Drama ,Family, Fantasy ,History, Horror, Mystery ,Romance ,Sci-Fi, Thriller, War) :").lower()
    language= input("Enter a language : te , ta , en , hi ").lower()
    suggestiobn= suggest_movie(genre,language)
    print(f'Movie suggestion for {genre} genere in {language} language: {suggestiobn}')