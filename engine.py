#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ABS import *
from Diarrhea_Disease import *
from Colon_Disease import *
from Right_Upper import *
from Right_upper_AB import *
from Abdominal_Pain import *


# In[2]:


class engine(Find_Disease_Realting_to_diarrhea,
             Find_Soluation_For_Epegastric_Abdominal,
             Find_soluation_For_upper_Right_ABS_With_Shoulder_Pain,
             Find_solution_For_Right_upper_AB,
             Find_Upper_Left_And_Normal_Abdominal_Pain_Disease,
             getColon,
             KnowledgeEngine):
    
        
    @DefFacts()
    def start(self):
        yield GoalisTo(action="Abs")
        
    @Rule(GoalisTo(action="getAnother"),Answer(),NOT(Fact("Done")),salience=-1)
    def Done(self):
        print("Done !")
        self.declare(Fact("Done"))
        
    @Rule(GoalisTo(action="getAnother"),NOT(Answer()))
    def Another(self):
        print("Sorry The Disease you have,it's not in our database")
        
    @Rule(Answer(name=MATCH.name,pro=MATCH.cf),salience=0)
    def answer(self,name,cf):
            name=str(name)
            name=name[name.find("."):]
            print("you Have [ %s ] with probability %f"%(name[1:],cf))
    


# In[4]:


t=engine()
t.reset()
t.run()


# In[24]:

