"""
A simple example script to get all posts on a user's timeline.
Originally created by Mitchell Stewart.
<https://gist.github.com/mylsb/10294040>
"""
import facebook

def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['created_time'])


# You'll need an access token here to do anything.  You can get a temporary one
# here: https://developers.facebook.com/tools/explorer/
access_token = 'EAAGTxIEbgkoBAFjCgiGUsHUr8cUxlsCZBEsfdtv5ldKJJL8rN3jOVp9ZCEYJYFqLYTZBT9FpmtZAZC2zTVaLSVFh7ZBBjoJu4ZAS0k8qATDZAOQGkA5OtF0ZCGz77dhzAhcZCsrc7XQ32IBVBDYamKJeWYzfndJvhwpIZANtNjnQQl7Yj5wDou1OFmxNQJfbyZCqiKHBigwSeH8UwgZDZD'
# Look at Bill Gates's profile for this example by using his Facebook id.
user = '2145934545419937'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')
aa = graph.get_object(id='100000102369663_1981229015223825')
print(aa['story'])
