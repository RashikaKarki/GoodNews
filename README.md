# GoodNews

Sentiment Analysis Model to predict good or positive news from Headlines.

### Motivation

After the coronavirus pandemic started the news article had started being overwhelmingly negative with lots of news article covering the death tolls and economic crisis. If we look at the Google Trend on “Positive News” or “Good News” during the time when the Pandemic started, we can clearly see the need of a portal with just positive news.

![image](https://user-images.githubusercontent.com/41114269/123546458-4b0d2000-d77c-11eb-8194-444eebc7c8a3.png)

 
 ### Project Structure
 
```
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│
├───App
│   │   main.py
│   │
│   ├───Data
│   │       data.json
│   │
│   ├───Model
│   │       chi_selector.pkl
│   │       logistic_regression.pkl
│   │       vectorizer.pkl
│   │
│   ├───Script
│   │   │   preprocess_data.py
│   │   │   scrape.py
│   │   │   train.py
│   │   │   __init__.py
│
├───Data
│       Clean_data.csv
│       News.csv
│       README.md
│
└───Notebook
    │   Good News Classifying Model - Cleaning.ipynb
    │   Good News Classifying Model.ipynb
    │   replacement.json

```

### Run the API

Make sure you have python3 and pip installed


Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

## Usage


Start flask server
```bash
$ export FLASK_APP=main.py
$ flask run
```

## How to call the Flask API?

### Get Data

- **API Call:** `http://127.0.0.1:5000/get_data` 
- **Request Method:** get
- **Returns:** JSON
```javascript

    {
    "Meeting Of Organising Committee Of CPN-UML 10th General Convention On June 30": "Negative",
    "Nepal In Desperate Need Of Life-Saving Vaccines": "Positive",
    "Nepal’S Foreign Policy Has Taken Concrete Shape, Says PM": "Positive",
    "PM Instructs For Prompt Disaster Response, Relief": "Negative"
    }

```

![image](https://user-images.githubusercontent.com/41114269/123552333-620c3c00-d795-11eb-8f04-172121321203.png)
