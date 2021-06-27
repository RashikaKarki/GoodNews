from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Script.preprocess_data import clean_data
from Script.train import train_using_logistic_regression

def get_data():
    urls = ["https://risingnepaldaily.com/main-news"]
    driver = set_up_driver()
    headlines = []
    for url in urls:
        driver.get(url)
        headlines_tag = driver.find_elements_by_class_name("trand")
        for i in headlines_tag:
            headlines.append(i.text)
    driver.close()
    #headlines = ["Be a better ancestor: five ways to be good to future generations", "A ‘forest’ has sprung up in an unlikely location in London", "Chop and change: the company recycling chopsticks into beautiful homewares", "Timber’s time: wood is making a comeback in construction, bringing many benefits"]
    print("Cleaning Data...")
    data = clean_data(headlines)
    print("Predicting...")
    y_pred = train_using_logistic_regression(data)
    print("Storing it...")
    positive_headlines = dict()

    for i,y in enumerate(y_pred):
        if int(y) == 1:
            positive_headlines[headlines[i]] = "Positive"
        else:
            positive_headlines[headlines[i]] = "Negative"

    return positive_headlines

def set_up_driver():
    # Settings of Chrome
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver
