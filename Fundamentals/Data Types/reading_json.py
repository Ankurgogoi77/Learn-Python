#api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=2
import json
import requests
print(requests.__version__)

#Failing to provide the correct credentials will result in a 401 Unauthorized error
#url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=10"

#select top 10 trending tweets with logos
response = requests.get(url)
tweets = response.json()
print(tweets)
print(tweets)

for tweet in tweets:
    print(tweet['text'])
    print(tweet['user']['name'])
    print(tweet['user']['screen_name'])
    print(tweet['user']['profile_image_url'])
    
    print(tweet['entities']['media'][0]['media_url'])
    
    print(tweet['created_at'])
    print(tweet['retweet_count'])
    print(tweet['favorite_count'])
    print(tweet['lang'])
    print(tweet['source'])
    print(tweet['in_reply_to_screen_name'])
    print(tweet['in_reply_to_status_id'])
    print(tweet['in_reply_to_user_id'])
    print(tweet['geo'])
    print(tweet['coordinates'])
    print(tweet['place'])
    print(tweet['contributors'])
    print(tweet['is_quote_status'])
    print(tweet['quoted_status_id'])
    print(tweet['quoted_status'])
    print(tweet['retweeted'])
    print(tweet['possibly_sensitive'])
    print(tweet['filter_level'])
    print(tweet['lang'])
    print(tweet['matching_rules'])
    print(tweet['current_user_retweet'])
    print(tweet['scopes'])
    print(tweet['withheld_in_countries'])
    print(tweet['withheld_scope'])
    print(tweet['truncated'])
    print(tweet['display_text_range'])
    print(tweet['extended_entities'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
    print(tweet['quoted_status_id_str'])
    print(tweet['quoted_status_permalink'])
