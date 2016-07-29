import praw

reddit = praw.Reddit("Linux/python/PRAW:com.alexharman.DoylistBot:v0.1 (by /u/krytorii)")

with open("client_auth.txt") as f:
    client_id = f.readline().split()[1]
    client_secret = f.readline().split()[1]

reddit.set_oauth_app_info(client_id, client_secret, "http://127.0.0.1:65010/authorize_callback")
url = reddit.get_authorize_url('MyChromebook', ['edit', 'history', 'identity', 'read', 'submit', 'vote'], True)

print "Please visit this URL to allow this script to access the provided account:"
print url

print "\n\n The \"accept\" button will route you to another URL that won't load. Paste the text that comes after the \"&code=\" into the next input"

code = raw_input("input code: ")
access_information = reddit.get_access_information(code)
reddit.set_access_credentials(**access_information)
token = access_information["refresh_token"]

f = open("token.txt", 'w')
f.write(token)
f.close()
print "The refresh token " + token + " has been stored in token.txt"

