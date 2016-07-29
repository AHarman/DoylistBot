import praw

with open("client_auth.txt") as f:
    client_id = f.readline().split()[1]
    client_secret = f.readline().split()[1]
with open("token.txt") as f:
    token = f.readline()

reddit = praw.Reddit("Linux/python/PRAW:com.alexharman.DoylistBot:v0.1 (by /u/krytorii)")

reddit.set_oauth_app_info(client_id, client_secret, "http://127.0.0.1:65010/authorize_callback")

reddit.refresh_access_information(token)

subreddit = reddit.get_subreddit("DoylistBot")

for post in praw.helpers.submission_stream(reddit, subreddit):
    print post
    post.add_comment("Just seeing if I can comment")
