import tweepy

akey = "JUuAx42iwjEhHPvBkrSrWFVqO"
askey = "TbOouI9UXJGFhgK6BExvS1GbhFqpwv7fUEd6AREm8j05BFGlmj"
atoken = "1053163840794312704-WaAk6sWEBApTtbyVXfpNRRHhM23amL"
astoken = "x7ae5w3SbNS0lrWIJ3hccjc1TkwjBFN5GYRlVVWijsVo9"



auth = tweepy.OAuthHandler(akey,askey)
auth.set_access_token(atoken,astoken)
auth.secure = True
api = tweepy.API(auth)
tweet1 = " this is my first tweet"
api.update_status(status = tweet1)
