class MemberStore:
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        for member in MemberStore.members:
            if id == member.id:
                return member
        return "Not found"

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def entity_exists(self, member):
        if self.get_by_id(member.id) == "Not found":
            return  "Not Exists"
        return "Exists"
    
    def update(self, member):

class PostStore:
    posts = []
    last_id = 1

    def add(self, post):
        post.id = PostStore.last_id
        PostStore.posts.append(post)
        PostStore.last_id += 1

    def get_all(self):
        return self.posts

    def get_by_id(self, id):
        for post in PostStore.posts:
            if id == post.id:
                return post
        return "Not found"

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def entity_exists(self, post):
        #result = "Exists"
        if self.get_by_id(post.id) == "Not found":
            return  "Not Exists"
        return "Exists"