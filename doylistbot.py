import praw

# Read details from file
with open("client_auth.txt") as f:
    client_id = f.readline().split()[1]
    client_secret = f.readline().split()[1]
with open("token.txt") as f:
    token = f.readline()

bot_message =  "Please use this comment to contain all your Doylist (out of universe) answers and comments.\n\n"
bot_message += "I am a bot, created by /u/krytorii. Please leave any feedback in /r/doylistbot"

# Login
reddit = praw.Reddit("Linux/python/PRAW:com.alexharman.DoylistBot:v0.1 (by /u/krytorii)")
reddit.set_oauth_app_info(client_id, client_secret, "http://127.0.0.1:65010/authorize_callback")
reddit.refresh_access_information(token)

# Do this when we start up so we don't respond to threads we've already responded to
my_comments = reddit.get_me().get_comments(1)
for comment in my_comments:
    last_submission = praw.helpers.convert_id36_to_numeric_id(comment.submission.fullname[3:])

subreddit = reddit.get_subreddit("DoylistBot")


# Main loop
for post in praw.helpers.submission_stream(reddit, subreddit):
    if praw.helpers.convert_id36_to_numeric_id(post.fullname[3:]) > last_submission:
        print post
        post.add_comment(bot_message)
    last_submission = praw.helpers.convert_id36_to_numeric_id(post.fullname[3:])
