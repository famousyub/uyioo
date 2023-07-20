import numpy as np
import pandas as pd
from scrapy.selector import Selector
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

import imdb

def get_movie_id(movie_name):
    ia = imdb.IMDb()
    movies = ia.search_movie(movie_name)
    if movies:
        movie = movies[0]
        return movie.movieID
    else:
        return None

film_name = input("Enter film name: ")

i = get_movie_id(film_name)
if i is None:
    print("Movie not found.")
    exit(1)

i = f"tt{i}"

driver = webdriver.Chrome()

url = f"https://www.imdb.com/title/{i}/reviews/?ref_=tt_ql_2"
time.sleep(1)
driver.get(url)
time.sleep(1)

body = driver.find_element(By.CSS_SELECTOR, 'body')

# Scroll to load all review pages
while True:
    old_height = driver.execute_script("return document.body.scrollHeight")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        break

sel = Selector(text=driver.page_source)
review_counts = sel.css('.lister .header span::text').extract_first().replace(',', '').split(' ')[0]
try: 
    more_review_pages = int(review_counts)
except Exception as e:
    print(str(e))
    exit(1)

for _ in tqdm(range(more_review_pages)):
    try:
        css_selector = 'load-more-trigger'
        driver.find_element(By.ID, css_selector).click()
    except:
        pass

rating_list = []
review_date_list = []
review_title_list = []
author_list = []
review_list = []
review_url_list = []
error_url_list = []
error_msg_list = []
reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')

for d in tqdm(reviews):
    try:
        sel2 = Selector(text=d.get_attribute('innerHTML'))
        try:
            rating = sel2.css('.rating-other-user-rating span::text').extract_first()
        except:
            rating = np.NaN
        try:
            review = sel2.css('.text.show-more__control::text').extract_first()
        except:
            review = np.NaN
        try:
            review_date = sel2.css('.review-date::text').extract_first()
        except:
            review_date = np.NaN    
        try:
            author = sel2.css('.display-name-link a::text').extract_first()
        except:
            author = np.NaN    
        try:
            review_title = sel2.css('a.title::text').extract_first()
        except:
            review_title = np.NaN
        try:
            review_url = sel2.css('a.title::attr(href)').extract_first()
        except:
            review_url = np.NaN
        rating_list.append(rating)
        review_date_list.append(review_date)
        review_title_list.append(review_title)
        author_list.append(author)
        review_list.append(review)
        review_url_list.append(review_url)
    except Exception as e:
        error_url_list.append(url)
        error_msg_list.append(e)

review_df = pd.DataFrame({
    'Review_Date': review_date_list,
    'Author': author_list,
    'Rating': rating_list,
    'Review_Title': review_title_list,
    'Review': review_list,
    'Review_Url': review_url_list  # Corrected variable name
})

review_df.to_csv(f'{film_name}_reviews.csv', index=False)  # Save the CSV with a more descriptive name

driver.quit()  # Close the browser after scraping is done