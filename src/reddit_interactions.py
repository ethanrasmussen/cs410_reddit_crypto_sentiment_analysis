import requests


def get_subreddit_feed_json(subreddit_name:str):
    return requests.get(f"https://www.reddit.com/r/{subreddit_name}.json").json()

def get_post_json(subreddit_name:str, post_id:str):
    return requests.get(f"https://www.reddit.com/r/{subreddit_name}/comments/{post_id}/.json").json()


class RedditPost:
    def __init__(self, id:str, title:str, text_content:str, subreddit:str, author:str) -> None:
        self.id = id
        self.title = title
        self.content = text_content
        self.subreddit = subreddit
        self.author = author

def get_post_from_id(subreddit_name:str, post_id:str):
    post_dict = get_post_json(subreddit_name=subreddit_name, post_id=post_id)
    return RedditPost(
        id=None,
        title=None,
        text_content=None,
        subreddit=None,
        author=None
    )

def get_posts_from_subreddit(subreddit_name:str, after_timestamp = None):
    pass