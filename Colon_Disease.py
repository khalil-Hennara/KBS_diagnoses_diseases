from Disease_CF import *
from Handling_Function import *
from fact_list import *



class getColon:
    
    #Rule  128
    @Rule(GoalisTo(action="getColon"),
          NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN)),
         )
    @Rule(salience=priority-300)
    def func_128(self):
        ans=Handling_Choice_input("Do you Have [ABDOMINAL PAIN] ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=ans))
        
    #Rule  129
    @Rule(GoalisTo(action="getColon"),
          NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD)),
          Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.cf),
          TEST(lambda cf:cf>0)
         )
    @Rule (salience=priority-301)
    def func_129(self):
        ans=Handling_Choice_input("Dose Pain Worsed by Food ?" )
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=ans))
    
    
    #Rule  130
    @Rule(GoalisTo(action="getColon"),
          NOT(Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS)),
          Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.cf),
          TEST(lambda cf:cf>0)
         )
    @Rule (salience=priority-302)
    
    def func_130(self):
        ans=Handling_Choice_input("Dose Pain Worsed by strees ?" )
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=ans))
    
    
    #Rule 131
    @Rule(GoalisTo(action="getColon"),
          NOT(Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE)),
          )
    @Rule (salience=priority-303)
    
    def func_131(self):
        ans=Handling_Choice_input("Do you Have [ABDOMINAL FLATULENCE]  ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=ans))
    
    
    
    #Rule 134
    @Rule (GoalisTo(action="getColon"),
           NOT(Fact(name="diarrhea")),
           NOT(Manifestaion(name=Clinic.CONSTIPATION))
          )
    @Rule(salience=priority-306)
    def func_134(self):
        ans=Handling_YES_NO_input("Do you Have [CONSTIPATION] ? " )
        if ans!=0:
            self.declare(Manifestaion(name=Clinic.CONSTIPATION,CF=1))
        else:
            ans=Handling_YES_NO_input("Do you Have [diarrhea] ? ")
            if ans!=0:
                self.declare(Manifestaion(name=Clinic.dIARRHEA,CF=1))
            self.declare(Fact(name="diarrhea"))
    
    
    
    #Rule 135
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=Clinic.CONSTIPATION,CF=MATCH.c4)
          )
    @Rule(salience=priority-306)
    def func_135(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4,gol):
        print(135)
        c0=c0*IBS[Clinic.ABDOMINAL_PAIN]
        c1=c1*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD]
        c2=c2*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        c4=c4*IBS[Clinic.CONSTIPATION]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f2)
        self.retract(f3)
        self.retract(f4)
        self.modify(gol,action="getAnother")
    
    
    #Rule 136
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3),
           AS.f4<<Manifestaion(name=Clinic.dIARRHEA,CF=MATCH.c4)
          )
    @Rule(salience=priority-307)
    def func_136(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4,gol):
        print(136)
        
        c0=c0*IBS[Clinic.ABDOMINAL_PAIN]
        c1=c1*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD]
        c2=c2*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        c4=c4*IBS[Clinic.dIARRHEA]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f2)
        self.retract(f3)
        self.retract(f4)
        self.modify(gol,action="getAnother")
            
    
    #Rule 137
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f0<<Manifestaion(name=Clinic.ABDOMINAL_PAIN,CF=MATCH.c0),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3)
          )
    @Rule(salience=priority-308)
    def func_137(self,f0,f1,f2,f3,c0,c1,c2,c3,gol):
        print(137)
        
        c0=c0*IBS[Clinic.ABDOMINAL_PAIN]
        c1=c1*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD]
        c2=c2*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))

        self.retract(f0)
        self.retract(f1)
        self.retract(f2)
        self.retract(f3)
        self.modify(gol,action="getAnother")
            
    
    
    #Rule 138
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=MATCH.c1),
           AS.f2<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3)
          )
    @Rule(salience=priority-307)
    def func_138(self,f1,f2,f3,c1,c2,c3,gol):
        print(138)
        
        c1=c1*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD]
        c2=c2*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        
        cf=CF(c1,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))
            
        self.retract(f1)
        self.retract(f2)
        self.retract(f3)
        self.modify(gol,action="getAnother")
        
        
    #Rule 139
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,CF=MATCH.c1),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3)
          )
    @Rule(salience=priority-308)
    def func_139(self,f1,f3,c1,c3,gol):
        print(139)
        
        c1=c1*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        
        cf=CF(c1,c3)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))
            
        self.retract(f1)
        self.retract(f3)
        self.modify(gol,action="getAnother")
            
            
    
    #Rule 140
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f2<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,CF=MATCH.c2),
           AS.f3<<Manifestaion(name=Clinic.ABDOMINAL_FLATULENCE,CF=MATCH.c3)
          )
    @Rule(salience=priority-309)
    def func_140(self,f2,f3,c2,c3,gol):
        print(140)
        c2=c2*IBS[Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS]
        c3=c3*IBS[Clinic.ABDOMINAL_FLATULENCE]
        cf=CF(c2,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.IBS,pro=cf))
        self.modify(gol,action="getAnother")
        self.retract(f2)
        self.retract(f3)
    
    
    
    #Rule 141
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN)
          )
    @Rule(salience=priority-310)
    def func_141(self,f1,gol):
        print(141)
        
        self.retract(f1)
        self.modify(gol,action="getAnother")
    
    
    
    #Rule 141
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD)
          )
    @Rule(salience=priority-311)
    def func_142(self,f1,gol):
        print(142)
        
        self.retract(f1)
        self.modify(gol,action="getAnother")
    
    #Rule 141
    @Rule (AS.gol<<GoalisTo(action="getColon"),
           AS.f1<<Manifestaion(name=Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS)
          )
    @Rule(salience=priority-312)
    def func_143(self,f1,gol):
        print(143)
        self.retract(f1)
        self.modify(gol,action="getAnother")
    