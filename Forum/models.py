class Member():

    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
    
    def __str__(self):
        return  "Name: "+ self.name



class Post():

    def __init__(self, title, body):
        self.id = 0
        self.title = title
        self.body = body
    
    def __str__(self):
        return  "Title: "+ self.title
        