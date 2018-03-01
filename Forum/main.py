import models
import stores

member1 = models.Member("Member1", "26")
member2 = models.Member("Member2", "30")

MS = stores.MemberStore()
MS.add(member1)
MS.add(member2)

print MS.get_all()

post1 = models.Post("title1", "body1")
post2 = models.Post("title2", "body2")
post3 = models.Post("title3", "body3")

PS = stores.PostStore()
PS.add(post1)
PS.add(post2)
PS.add(post3)

print PS.get_all()
