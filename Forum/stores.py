class MemberStore():
    members = []
    last_id = 1

    def add(self, member):
        member.id = MemberStore.last_id
        MemberStore.members.append(member)
        MemberStore.last_id += 1

    def get_all(self):
        return MemberStore.members

    def get_by_id(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.id == id:
                result = member
                break
        return result

    def get_by_name(self, id):
        all_members = self.get_all()
        result = None
        for member in all_members:
            if member.name == name:
                result = member
                break
        return result

    def delete(self, id):
        member = self.get_by_id(id)
        MemberStore.members.remove(member)

    def entity_exists(self, member):
        if self.get_by_id(member.id) == None:
            return  False
        return True
    
    def update(self, member):
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member
        return result

class PostStore():
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
        return None

    def delete(self, id):
        post = self.get_by_id(id)
        PostStore.posts.remove(post)

    def entity_exists(self, post):
        if self.get_by_id(post.id) == None:
            return  False
        return True
