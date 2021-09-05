from Disease_CF import *
from Handling_Function import *
from fact_list import *

class Find_Upper_Left_And_Normal_Abdominal_Pain_Disease:
    
    #Rule 77
    @Rule (AS.f0<<Manifestaion(name=Clinic.LEFT_UPPER_QUADRANT_PAIN),
           AS.gol<<GoalisTo(action=MATCH.ac))
    @Rule(salience=priority-77)
    def func_77(self,gol,f0):
        self.modify(gol,action="Diarrhea")
        self.retract(f0)
    
    #Rule 78
    @Rule (Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           NOT(Manifestaion(name=Clinic.FAVER)))
    @Rule(salience=priority-78)
    def func_78(self):
        ans=Handling_Choice_input("Do you Have [Fever] ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    #Rule 79
    @Rule (Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           NOT(Manifestaion(name=Clinic.WEIGH_LOSS)))
    @Rule(salience=priority-78)
    def func_79(self):
        ans=Handling_Choice_input("Do you Have [WEIGH_LOSS] ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
    
    
    
    #Rule 80
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           NOT(Fact(name="diarrhea")),
           AS.gol<<GoalisTo(action=MATCH.ac)
          )
    @Rule (salience=priority-80)
    def func_80(self,gol,f0):
        ans=Handling_diarrhea()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=0.93))
        else :
            self.modify(gol,action="getColon")
            self.retract(f0)
        self.declare(Fact(name="diarrhea"))
        
    
    #Rule 81
    @Rule (Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           Fact(name="diarrhea"),
           NOT(Fact(name="EGD"))
          )
    @Rule (salience=priority-80)
    def func_81(self):
        print("You probably Have [CROHN DISEASE] but to be sure you shoudl make an [EGD] Test.")
        ans=Handling_EGD_input()
        if ans!=0:
            for item in ans:
                self.declare(Manifestaion(name=item[0],CF=item[1]))
                self.declare(Fact(name="EGD"))
    
    #Rule 82
    @Rule (Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA),
           NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN)),
           NOT(Manifestaion(name=Clinic.FAVER))
          )
    @Rule (salience=priority-81)
    def func_82(self):
        ans=Handling_Choice_input("Do you Have Fever ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    #Rule 83
    @Rule (Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA),
           NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN)),
           NOT(Manifestaion(name=Clinic.WEIGH_LOSS))
          )
    @Rule (salience=priority-82)
    def func_83(self):
        ans=Handling_Choice_input("Do you Have [WEIGH LOSS] ?")
        ans =get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
        
    #Rule 84
    @Rule (Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA),
           NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN))
          )
    @Rule (salience=priority-83)
    def func_84(self):
        ans=Handling_Choice_input("Do you Have [ABDOMINAL PAIN] ?")
        ans =get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=ans))
     
    #Rule 82.1
    @Rule (Manifestaion(name=EGD.COBBLESTONING),
           NOT(Manifestaion(name=Clinic.FAVER))
          )
    @Rule (salience=priority-84)
    def func_82_1(self):
        ans=Handling_Choice_input("Do you Have Fever ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    #Rule 82.2
    @Rule (Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES),
           NOT(Manifestaion(name=Clinic.FAVER))
          )
    @Rule (salience=priority-85)
    def func_82_2(self):
        ans=Handling_Choice_input("Do you Have Fever ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    
    #Rule 83.1
    @Rule (Manifestaion(name=EGD.COBBLESTONING),
           NOT(Manifestaion(name=Clinic.WEIGH_LOSS))
          )
    @Rule (salience=priority-86)
    def func_83_1(self):
        ans=Handling_Choice_input("Do you Have [WEIGH LOSS] ?")
        ans =get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
    
    
    
    #Rule 83.2
    @Rule (Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES),
           NOT(Manifestaion(name=Clinic.WEIGH_LOSS))
          )
    @Rule (salience=priority-87)
    def func_83_2(self):
        ans=Handling_Choice_input("Do you Have [WEIGH LOSS] ?")
        ans =get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
    
    
    #Rule 85.1
    @Rule (Manifestaion(name=EGD.COBBLESTONING),
           NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN)),
           NOT(Fact("okk"))
          )
    @Rule (salience=priority-88)
    def func_85_1(self):
        ans=Handling_Choice_input("Do you Have Abdominal Pain ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=ans))
        self.declare(Fact("okk"))
        
    #Rule 85.2
    @Rule (Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES),
           NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN)),
           NOT(Fact("okk"))
          )
    @Rule (salience=priority-89)
    def func_85_2(self):
        ans=Handling_Choice_input("Do you Have Abdominal Pain  ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=ans))
        self.declare(Fact("okk"))
    #Rule 85.3
    @Rule(Manifestaion(name=EGD.COBBLESTONING),
          NOT(Fact(name="diarrhea")),salience=priority-90)
    def func_85_3(self):
        ans=ans=Handling_diarrhea()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=0.98))
        self.declare(Fact(name="diarrhea"))
            
    #Rule 85.3
    @Rule(Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES),
          NOT(Fact(name="diarrhea")),salience=priority-91)
    def func_85_4(self):
        ans=ans=Handling_diarrhea()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=0.98))
        self.declare(Fact(name="diarrhea"))
        
    
    #Rule 85
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES,CF=MATCH.c4),
           AS.f5<<Manifestaion(name=EGD.COBBLESTONING,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
          )
    @Rule(salience=priority-92)
    def func_85(self,f0,f1,f2,f3,f4,f5,c0,c1,c2,c3,c4,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.NON_GROSSLY_BLOODY_DIARRHEA]
        c4=c4*CROHN_DISEASE[EGD.DEEP_AND_LONG_FISSURES]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f3)
        self.retract(f4)
        self.retract(f5)
   
    
    #Rule 86
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.dIARRHEA,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES,CF=MATCH.c4),
           AS.f5<<Manifestaion(name=EGD.COBBLESTONING,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-93)
    def func_86(self,f0,f1,f2,f3,f4,f5,c0,c1,c2,c3,c4,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.dIARRHEA]
        c4=c4*CROHN_DISEASE[EGD.DEEP_AND_LONG_FISSURES]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f4)
        self.retract(f5)
    
    
    #Rule 87
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES,CF=MATCH.c4),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-94)
    def func_87(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.NON_GROSSLY_BLOODY_DIARRHEA]
        c4=c4*CROHN_DISEASE[EGD.DEEP_AND_LONG_FISSURES]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f3)
        self.retract(f4)
        
    
    #Rule 88
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c3),
           AS.f5<<Manifestaion(name=EGD.COBBLESTONING,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-95)
    def func_88(self,f0,f1,f2,f3,f5,c0,c1,c2,c3,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.NON_GROSSLY_BLOODY_DIARRHEA]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f3)
        self.retract(f5)
    
    
    
    #Rule 88.1
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f5<<Manifestaion(name=EGD.COBBLESTONING,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-96)
    def func_88_1(self,f0,f1,f2,f5,c0,c1,c2,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c5)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f5)
    
   

    #Rule 88.2
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f5<<Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-97)
    def func_88_2(self,f0,f1,f2,f5,c0,c1,c2,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c5)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f5)
   
    #Rule 89
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c3),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-98)
    def func_89(self,f0,f1,f2,f3,c0,c1,c2,c3):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.NON_GROSSLY_BLOODY_DIARRHEA]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f3)
    
    
    #Rule 90
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.dIARRHEA,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=EGD.DEEP_AND_LONG_FISSURES,CF=MATCH.c4),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-99)
    def func_90(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.dIARRHEA]
        c4=c4*CROHN_DISEASE[EGD.DEEP_AND_LONG_FISSURES]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f4)
        
    
    
    #Rule 91
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.dIARRHEA,CF=MATCH.c3),
           AS.f5<<Manifestaion(name=EGD.COBBLESTONING,CF=MATCH.c5),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-100)
    def func_91(self,f0,f1,f2,f3,f5,c0,c1,c2,c3,c5):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.dIARRHEA]
        c5=c5*CROHN_DISEASE[EGD.COBBLESTONING]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
        self.retract(f5)
    
    #Rule 92
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.dIARRHEA,CF=MATCH.c3),
           NOT(GoalisTo(action="getColon"))
           
           )
    @Rule(salience=priority-101)
    def func_92(self,f0,f1,f2,f3,c0,c1,c2,c3):
        c0=c0*CROHN_DISEASE[Clinic.ABDOMINAL_PAIN]
        c1=c1*CROHN_DISEASE[Clinic.FAVER]
        c2=c2*CROHN_DISEASE[Clinic.WEIGH_LOSS]
        c3=c3*CROHN_DISEASE[Clinic.dIARRHEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CROHN_DISEASE,pro=cf))
          
    
    #Rule 94
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           AS.f1<<Manifestaion(name=Clinic.FAVER),
           AS.f2<<Manifestaion(name=Clinic.WEIGH_LOSS),
           AS.f3<<Manifestaion(name=Clinic.NON_GROSSLY_BLOODY_DIARRHEA),
           NOT(GoalisTo(action="getColon"))
           
          )
    @Rule(salience=priority-103)
    def func_94(self,f0,f1,f2,f3):
            self.retract(f3)
    
    
    #Rule 95
    @Rule (AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN),
           NOT(GoalisTo(action="getColon")),
           NOT(GoalisTo(action="getAnother")),
           AS.gol<<GoalisTo(action=MATCH.ac)
          )
    @Rule(salience=priority-104)
    def func_95(self,gol,f0):
        self.modify(gol,action="getColon")
    