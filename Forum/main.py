import models
import stores

member1 = models.Member("Hassan", "26")
member2 = models.Member("Khaled", "30")

MS = stores.MemberStore()
MS.add(member1)
MS.add(member2)

MS.delete(2)
print MS.get_all()
print MS.get_by_id(1)
print MS.entity_exists(member1)
print MS.entity_exists(member2)

post1 = models.Post("title1", "body1")
post2 = models.Post("title2", "body2")
post3 = models.Post("title3", "body3")

PS = stores.PostStore()
PS.add(post1)
PS.add(post2)
PS.add(post3)

PS.delete(3)
print PS.get_all()
print PS.get_by_id(1)
print PS.entity_exists(post2)
print PS.entity_exists(post3)
