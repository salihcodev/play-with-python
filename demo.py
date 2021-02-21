import requests
import json

# with open('users.json') as u:
#     data = json.load(u)

# base URL
url = "https://jsonplaceholder.typicode.com/comments"
res_get = requests.get(url)


def api_error(param):
    pass


if res_get.status_code != 200:
    # something went wrong :)
    raise api_error('GET /users/ {}'.format(res_get.status_code))
# else continue
parsed_comment = res_get.json()

for comment in parsed_comment:
    print('{} {}'.format(comment['id'], comment['email']))

# user to add
comment_to_add = {"email": "salih@codev.com"}

res_post = requests.post(url, json=comment_to_add)
if res_post.status_code != 201:
    raise api_error('POST /users/ {}'.format(res_post.status_code))

# it gonna return ID: 501 because the tha count of all comment is
print('Created user. ID: {}'.format(res_post.json()["id"]))
