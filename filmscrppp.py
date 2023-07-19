import requests
import csv
from bs4 import BeautifulSoup

def scrape_imdb():
    comments = []
    ratings = []

    url = 'https://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_links = soup.select('.titleColumn a')

    for movie_link in movie_links:
        movie_url = 'https://www.imdb.com' + movie_link['href']
        movie_comments, movie_ratings = scrape_movie_reviews(movie_url)
        comments.extend(movie_comments)
        ratings.extend(movie_ratings)

    save_to_csv(comments, ratings)

def scrape_movie_reviews(url):
    comments = []
    ratings = []

    page = 1
    while True:
        response = requests.get(f'{url}/reviews/_ajax?paginationKey={page}')
        soup = BeautifulSoup(response.content, 'html.parser')
        comment_tags = soup.select('.content .text')
        rating_tags = soup.select('.content .ipl-ratings-bar .rating-other-user-rating span')

        if not comment_tags:
            break

        for comment_tag, rating_tag in zip(comment_tags, rating_tags):
            comments.append(comment_tag.get_text(strip=True))
            ratings.append(rating_tag.get_text(strip=True))

        page += 1

    return comments, ratings

def save_to_csv(comments, ratings):
    data = zip(comments, ratings)
    with open('imdb_reviews.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Comment', 'Rating'])
        writer.writerows(data)

if __name__ == '__main__':
    scrape_imdb()
