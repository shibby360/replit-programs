import praw, os
# put this stuff as a secret
r = praw.Reddit(client_id=os.environ['client id'], client_secret=os.environ['client_secret'],
password=os.environ['password'],
username=os.environ['username'],
user_agent=os.environ['user-agent'])

subreddit = r.subreddit("anishandshiv")
posts = []
for submission in subreddit.hot(limit=10):
  posts.append(submission.title)