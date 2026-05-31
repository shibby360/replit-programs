import os
def main():
  import praw
  # put this stuff as a secret
  r = praw.Reddit(client_id=os.environ['client id'], client_secret=os.environ['client_secret'],
  password=os.environ['password'],
  username=os.environ['username'],
  user_agent=os.environ['user-agent'])
  
  def replyr(post, text):
    post.reply(text + '\n\n*this was through a bot*')
  subreddit = r.subreddit("anishandshiv")
  for submission in subreddit.new(limit=1):
  	replyr(submission, "its a bot")
  	print("Bot replying to : ", submission.title)

# os.system('python videomaker/videomaker.py')
main()