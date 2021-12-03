
import fbchat
import os

class messenger():
    def __init__(self) -> None:
        self.username = os.environ.get('USERNAME')
        self.password = os.environ.get('FACEBOOK_PASSWORD')
        print(self.password[-1])
        self.client = fbchat.Client(self.username, self.password)
        
    
    def printFriends(self):

        name = str('nhat tu')
        friends = client.getUsers(name)  # return a list of names
        friend = friends[0]
        print(friend)

# username = str(raw_input("Username: "))
# client = fbchat.Client(username, getpass())
# no_of_friends = int(raw_input("Number of friends: "))
# for i in xrange(no_of_friends):
#     name = str(raw_input("Name: "))
#     friends = client.getUsers(name)  # return a list of names
#     friend = friends[0]
#     msg = str(raw_input("Message: "))
#     sent = client.send(friend.uid, msg)
#     if sent:
#         print("Message sent successfully!")