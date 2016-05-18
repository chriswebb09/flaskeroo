from twitter import Twitter, OAuth, TwitterHTTPError

class QueryTwitterApi(object):
    auth_tokens = {
    "OAUTH_TOKEN" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "OAUTH_SECRET" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "CONSUMER_KEY" : "XXXXXXXXXXXXXXXXXXXXX",
    "CONSUMER_SECRET" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }

    def __init__(self, query):
        self.query = query

    def connect_twitter_api(self):
        pass

    def get_query_results(self):
        pass



t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

def

def search_tweets(q, count=100, max_id=None):
    return t.search.tweets(q=q, result_type='recent', count=count, lang="en", max_id=max_id)


print [(t['text'], t['id']) for t in search_tweets('web development', 5)['statuses']]
