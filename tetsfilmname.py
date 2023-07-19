import requests
from bs4 import BeautifulSoup
import time

film_name = "titanic"  # Replace with the actual film name

url = f"https://www.imdb.com/find?q={film_name}&ref_=nv_sr_sm"

# Send a GET request to IMDb and parse the HTML response
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the first search result and extract the film's URL
result = soup.find(class_='result_text')
print(result)

# Extract the film URL
film_url = 'https://www.imdb.com' + result.a['href']

# Send another GET request to the film's page and parse the HTML response
response = requests.get(film_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the film's details
title = soup.find(class_='title_wrapper').h1.text.strip()
rating = soup.find(class_='ratingValue').strong.span.text.strip()

# Extract the comments and ratings
comments = []
ratings = []
reviews = soup.find_all(class_='review-container')
for review in reviews:
    comment = review.find(class_='text')
    rating = review.find(class_='rating-other-user-rating')
    if comment is not None:
        comments.append(comment.text.strip())
    if rating is not None:
        ratings.append(rating.span.text.strip())

# Print the extracted details
print("Film Title:", title)
print("Rating:", rating)
print("Comments:", comments)
print("Ratings:", ratings)
