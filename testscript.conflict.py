
class solution:
    name = 'yuan'
    def __init__(self,age,other):
        self.age = age
        print other

s1 = solution(12,'hello')
print s1.name
s1.name = 'qijie'
print s1.name
s2 = solution(13,'world')
print s2.name