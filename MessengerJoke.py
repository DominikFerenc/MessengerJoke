from fbchat import Client
from fbchat.models import Message
user_name = 'your_username'
password = 'your_password'

import fbchat # type: ignore
### see https://github.com/fbchat-dev/fbchat/issues/615#issuecomment-710127001
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
client = Client(user_name, password)

users = client.fetchAllUsers()
users2 = client.searchForUsers('who')
print(users2)
while 1:
    client.send(Message(text="message"), thread_id='for example 122324455')

client.logout()