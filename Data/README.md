## Dataset

To train the model “News Popularity in Multiple Social Media Platforms” Data Set from UCI 
Machine Learning Repository is used.

The given dataset contains a large number of News Article Headlines mapped together with its
Sentiment Score and their respective social feedback on multiple platforms. The collected data accounts 
about 100,000 news items on four different topics: Economy, Microsoft, Obama and Palestine. (UCI 
Machine Learning Repository, n.d.)

The attributes present in the dataset are:
- **IDLink (numeric):** Unique identifier of news items
- **Title (string):** Title of the news item according to the official media sources
- **Headline (string):** Headline of the news item according to the official media sources
- **Source (string):** Original news outlet that published the news item
- **Topic (string):** Query topic used to obtain the items in the official media sources
- **PublishDate (timestamp):** Date and time of the news items' publication
- **SentimentTitle (numeric):** Sentiment score of the text in the news items' title
- **SentimentHeadline (numeric):** Sentiment score of the text in the news items' headline
- **Facebook (numeric):** Final value of the news items' popularity according to the social media 
source Facebook
- **GooglePlus (numeric):** Final value of the news items' popularity according to the social media 
source Google+
- **LinkedIn (numeric):** Final value of the news items' popularity according to the social media 
source LinkedIn

For this project the Headline, SentimentHeadline attributes will only be used and news related to Microsoft will be removed as it is more tech centric and it is quite irrelevant in the context of Nepal. 