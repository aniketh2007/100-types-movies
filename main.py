import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Getting the information from the website
response = requests.get(url=URL)
movie_pg = response.text
#getting the required piece of data using the html.parser and selecting the required data
soup = BeautifulSoup(movie_pg, "html.parser")
all_movies = soup.find_all(name="h3",class_="title")

#Creating a list comprehension to get only text using getText() and we reverse the list
movie_titles = [ movie.getText() for movie in all_movies]
movie_names = movie_titles[::-1]

#Creating a text file which contents only the movie names.
with open("movies.txt","w") as file:
    for movie in movie_names:
        file.write(f"{movie}\n")


