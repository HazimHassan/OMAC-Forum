class Member():

    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []
    
    def __str__(self):
        return "Name: {self.name}, Age: {self.age}"



class Post():

    def __init__(self, title, body, member_id):
        self.id = 0
        self.title = title
        self.body = body
        self.member_id = member_id
    
    def __str__(self):
        return "Title: {self.title}, Bdoy: {self.body}"
        