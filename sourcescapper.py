import requests
import csv
from bs4 import BeautifulSoup

def scrape_imdb_movies():
    movie_data = []

    for page in range(1, 11):  # Scraping first 10 pages (you can adjust the range as needed)
        url = f'https://www.imdb.com/search/title/?title_type=feature&start={page * 50}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        movie_tags = soup.find_all('div', {'class': 'lister-item mode-advanced'})

        for movie_tag in movie_tags:
            title = movie_tag.h3.a.text.strip()
            year = movie_tag.h3.find('span', {'class': 'lister-item-year'}).text.strip('()')
            rating = movie_tag.strong.text.strip()

            movie_data.append({'Title': title, 'Year': year, 'Rating': rating})

    return movie_data

def scrape_imdb_comments(movie_data):
    for movie in movie_data:
        comments = []
        ratings = []

        url = f"https://www.imdb.com/title/{movie['Title'].lower().replace(' ', '_')}/reviews"
        page = 1

        while True:
            response = requests.get(f'{url}?sort=helpfulnessScore&dir=desc&ratingFilter=0&perPage=50&filter={page}')
            soup = BeautifulSoup(response.content, 'html.parser')

            comment_tags = soup.find_all('div', {'class': 'text show-more__control'})
            rating_tags = soup.find_all('span', {'class': 'rating-other-user-rating'})

            if not comment_tags:
                break

            for comment_tag, rating_tag in zip(comment_tags, rating_tags):
                comments.append(comment_tag.text.strip())
                ratings.append(rating_tag.find('span').text.strip())

            page += 1

        movie['Comments'] = comments
        movie['Ratings'] = ratings

def save_to_csv(movie_data):
    keys = ['Title', 'Year', 'Rating', 'Comments', 'Ratings']

    with open('imdb_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(movie_data)

if __name__ == '__main__':
    movies = scrape_imdb_movies()
    scrape_imdb_comments(movies)
    save_to_csv(movies)
