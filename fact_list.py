from experta import *

class GoalisTo(Fact):
    pass

class Manifestaion(Fact):
    pass

class Disease(Fact):
    pass

class Answer(Fact):
    pass

priority=1000


def CF(cf1,cf2):
    if cf1>=0 and cf2>=0:
        return cf1+cf2-(cf1*cf2)
    elif cf1<0 and cf2<0:
        return cf1+cf2+(cf1*cf2)
    else :
        return (cf1+cf2)/(1-min(abs(cf1),abs(cf2)))
    
def check_Finish(cf):
    if cf*10 >= 7:
        return True
    else :return False