from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





# Replace 'path/to/chromedriver' with the actual path to your chromedriver executable
driver = webdriver.Chrome()
driver.maximize_window()



film_name = "Interstellar"  # Replace with the actual film name
url = f"https://www.imdb.com/find?q={film_name}&ref_=nv_sr_sm"
driver.get(url)



result = driver.find_element_by_class_name('result_text')
film_url = result.find_element_by_tag_name('a').get_attribute('href')
driver.get(film_url)



while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "load-more-trigger"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
        load_more_button.click()
    except:
        break



reviews = driver.find_elements_by_class_name('text')
ratings = driver.find_elements_by_css_selector('.rating-other-user-rating span')
comments = [review.text.strip() for review in reviews]
ratings = [rating.text.strip() for rating in ratings]


print("Comments:", comments)
print("Ratings:", ratings)



driver.quit()
