from multiprocessing.connection import wait
import time
import praw 

reddit = praw.Reddit(client_id="id", client_secret= "secret", user_agent="user agent", username="usr", password="pwd")

print(reddit.user.me())
print(reddit.read_only)

subreddits = ['Selfpromtion']

title = "Title of YouTube Video"

link = "Link to YT video"

count = 0

for subreddit in subreddits:
    count+= 1
    try:
        reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)
        print("Sucessfully posted to:",subreddit,"Posted to,",count,"of",len(subreddits),"subreddits")

    except praw.exceptions.RedditAPIExceptions as exception:
        for subexception in exception.items:
            if subexception.error_type == "RATELIMIT":
                wait = str(subexception).replace("RATELIMIT: you are doing that too much. try again in","")
                if 'minute' in wait:
                    wait = wait[:2]
                    wait = int(wait)+1
                    print(wait)

                else: wait = 1
                
                print("waiting for:",wait,"minutes")
                time.sleep(wait*60)
                reddit.subreddit(subreddit).submit(title,url=link,send_replies=False)
                print("Sucessfully posted to:",subreddit,"Posted to,",count,"of",len(subreddits),"subreddits")

        