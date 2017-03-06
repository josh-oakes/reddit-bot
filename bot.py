import praw

def get_reddit_instance():
    reddit = praw.Reddit('bot1', user_agent='jmost2 bot1 v0.1')
    return reddit

def run_bot(reddit):
    for comment in reddit.subreddit('test').comments(limit=25):
        if "salt" in comment.body:
            print("Salty string found")
            comment.reply("[Too much salt](http://i.imgur.com/pCqy1sC.jpg)")
            print(comment.author)

reddit = get_reddit_instance()
run_bot(reddit)