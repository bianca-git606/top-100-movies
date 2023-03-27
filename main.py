import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").text

soup = BeautifulSoup(response, 'html.parser')
titles = soup.find_all(name="h3", class_="title")
movies = [title.text for title in titles]
print(movies)

with open("movies.txt", "a", encoding="utf-8") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")
