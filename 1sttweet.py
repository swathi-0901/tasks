import tweepy

api_key = "JUuAx42iwjEhHPvBkrSrWFVqO"
apisecret_key = "TbOouI9UXJGFhgK6BExvS1GbhFqpwv7fUEd6AREm8j05BFGlmj"
access_token = "1053163840794312704-WaAk6sWEBApTtbyVXfpNRRHhM23amL"
asecret_token = "x7ae5w3SbNS0lrWIJ3hccjc1TkwjBFN5GYRlVVWijsVo9"



auth = tweepy.OAuthHandler(api_key,apisecret_key)
auth.set_access_token(access_token,asecret_token)
auth.secure = True
api = tweepy.API(auth)
tweet1 = input(" enter the tweet you what to ...")
api.update_status(status = tweet1)
