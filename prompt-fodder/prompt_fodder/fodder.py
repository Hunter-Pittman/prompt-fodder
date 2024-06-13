import praw
import toml
from prompt_fodder import DATADIR
import base64


class Post:
    def __init__(self, subreddit, id, title, content, comments):
        self.id = id
        self.subreddit = subreddit
        self.title = title
        self.content = content
        self.comments = comments

class PromptFodder:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = "python:prompt-fodder:v1.0.0 (by u/PromptFodder)"

    def get_fodder(self, limit):
        reddit = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            user_agent=self.user_agent,
        )
        get_hot_posts(reddit, limit)

def get_config():    
    with open(DATADIR, "r") as f:
        config = toml.load(f)

    return config

def get_hot_posts(reddit, limit):
    print("Aqcuiring reddit posts...")
    config = get_config()
    subreddits = config["search_targets"]["subreddits"]

    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).hot(limit=limit):
            comments = []
            for comment in submission.comments:
                comments.append(comment.body)
                if len(comments) > 10:
                    break
            current_post = Post(subreddit=subreddit, title=submission.title, id=submission.id, content=submission.selftext, comments=comments)
            return current_post