
class Ghost:
    def __init__(self,toggle):
        self.jhk = toggle
        self.age = toggle
        self.home = toggle
        self.mental_state = toggle
        self.explore_asylum = toggle

    def Toggle(self,random_variable):
        random_variable = 'active'


dead = Ghost('inactive')

print(dead.explore_asylum)

def test():
    Ghost.Toggle(dead.explore_asylum)

#test()
dead.explore_asylum = 'active'
print(dead.explore_asylum)