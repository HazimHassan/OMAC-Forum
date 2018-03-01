class MemberStore:
    members = []

    def add(self, member):
        self.members.append(member)

    def get_all(self):
        return self.members
'''
    def get_by_id(self, id):
      # search for member by id

    def update(self, member):
     # update member data

    def delete(self, id):
      # delete member by id

    def entity_exists(self, member):
      # checks if an entity exists in a store
'''
class PostStore:
    posts = []

    def add(self, post):
        self.posts.append(post)

    def get_all(self):
        return self.posts
