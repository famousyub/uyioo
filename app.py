import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

def my_function(x):
  return list(dict.fromkeys(x))

import csv

def save_data_to_csv(data, filename):
    fieldnames = ['Comment', 'Rating']  # Define the field names for the CSV file

    with open(filename, 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row with field names
        import  time 
        time.sleep(1)
        print (data)
        for item ,  rate in data:
            writer.writerow({'Comment': item,'Rating' : rate})

# Example data

# Save data to CSV



app = Flask(__name__)









@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/film/<film_name>',methods=["GET"])
def film(film_name):
    # Construct the IMDb URL for the film
    url = f"https://www.imdb.com/find?q={film_name}&ref_=nv_sr_sm"

    # Send a GET request to IMDb and parse the HTML response
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first search result and extract the film's URL
    result = soup.find(class_='result_text')
    print(result)
    import time
    time.sleep(1)
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
        comments.append(review.find(class_='text').text.strip())
        ratings.append(review.find(class_='rating-other-user-rating').span.text.strip())

    return render_template('film.html', title=title, rating=rating, comments=comments, ratings=ratings)




@app.route('/', methods=['GET', 'POST'])

def index():




    if request.method == 'POST':
        movie_title = request.form['movie_title']
        comments, ratings = scrape_imdb(movie_title,10)
        comments_count = len(comments)
        ratings =  list(map(int,ratings)) 
        comments = my_function(comments)
       
        data   = zip(comments,ratings)

        save_data_to_csv(data, 'commentsandrate.csv')

        return render_template('index.html',  comments=comments, ratings=ratings,comments_count=comments_count)
    return render_template('index.html')

def scrape_imdb(movie_title,page_number=10):
    comments = []
    ratings = []

    url = f'https://www.imdb.com/title/{movie_title}/reviews'
    page = 1

    while True:
        response = requests.get(f'{url}?sort=helpfulnessScore&dir=desc&ratingFilter=0&perPage=50&filter={page}')
        soup = BeautifulSoup(response.content, 'html.parser')
        print(response)

        comment_tags = soup.find_all('div', {'class': 'text show-more__control'})
        rating_tags = soup.find_all('span', {'class': 'rating-other-user-rating'})

        if not comment_tags:
            break

        for comment_tag, rating_tag in zip(comment_tags, rating_tags):
            comments.append(comment_tag.text.strip())
            ratings.append(rating_tag.find('span').text.strip())


           

            

        page += 1

        print(page)


        if(page==page_number) :
            break

    return comments, ratings

if __name__ == '__main__':
    app.run(debug=True)
