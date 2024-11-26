from google_play_scraper import Sort, reviews_all

app_pac_name = "org.synesisit.convay"

result = reviews_all(
    app_pac_name,
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5 # defaults to None(means all score)
)

print(result)




