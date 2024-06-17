class User:
    def __init__(self, user_id, username):  #constructor method to intialize attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):  #self parameter here means when this method is called it
        user.followers += 1  # knows the object that called it
        self.following += 1


user1 = User("01", "tauseef")
user2 = User("02", "Malik")

user1.follow(user2)
user1.follow(user2)
user2.follow(user1)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
