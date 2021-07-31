badlist = ['bitch', 'fuck','crap','asshole']
tweet = input("What is your tweet?\n")

def censor_tweet(tweet):
  if ',' or '.'
  tweet_list = tweet.lower().split()
  #print(tweet_list)
  #print(badlist)
  for i in range(len(tweet_list)):
    for j in range(len(badlist)):
      if tweet_list[i] == badlist[j]:
        badword = tweet_list[i]
        censor = '*'*len(badword)
        #print(censor)
        tweet_list[i] = censor
        #print(tweet_list)
  censor_string = ' '.join(tweet_list)
  return censor_string

print(censor_tweet(tweet))