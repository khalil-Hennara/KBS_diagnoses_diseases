from Disease_CF import *
from Handling_Function import *
from fact_list import *


class Find_solution_For_Right_upper_AB:
    
    #Rule 58
    @Rule (Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN),
           NOT(Manifestaion(name=Clinic.FAVER)))
    @Rule(salience=priority-58)
    def func_58(self):
        ans=Handling_Choice_input("Do you Have Fever ?")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    
    #Rule 59
    @Rule(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN),
          NOT(Manifestaion(name=Clinic.JAUNDIC)))
    @Rule(salience=priority-59)
    def func_59(self):
        ans=Handling_Choice_input("Do you Have Jundic ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.JAUNDIC,CF=ans))
    
    #Rule 60
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          NOT(Fact(name="LAB"))
        )
        
    @Rule(salience=priority-60)
    def func_60(self,f0,f1,f2,c0,c1,c2):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if cf*10>=8.2:
            print("You probably Have [CHOLANGITIS] and we sure about That  more than 82% ")
            print("If you Won't you can Make blood Test for more accurecy ")
            ans=Handling_YES_NO_input("Do you Won't make A blood Test ? ")
            if ans==0:
                self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
                self.retract(f1)
                self.retract(f0)
            else:
                ans=Handling_LAB_input()
                if ans!=0:
                    for item in ans:
                        self.declare(Manifestaion(name=item[0],CF=item[1]))
                    self.declare(Fact(name="LAB"))
        else:
            print("you may be Have [CHOLANGITIS] But you should make a blood Test.")
            ans=Handling_LAB_input()
            if ans!=0:
                for item in ans:
                    self.declare(Manifestaion(name=item[0],CF=item[1]))
                self.declare(Fact(name="LAB"))
    
    
    #Rule 60.1
    @Rule(Manifestaion(name=LABS.BILIRUBIN),
          NOT(Manifestaion(name=Clinic.FAVER)),
         salience=priority-60)
    def func_60_1(self):
            ans=Handling_Choice_input("Do you Have Fever ?")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    
    #Rule 60.2
    @Rule(Manifestaion(name=LABS.BILIRUBIN),NOT(Manifestaion(name=Clinic.JAUNDIC)),salience=priority-60)
    def func_60_2(self):
            ans=Handling_Choice_input("Do you Have Jundic ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.JAUNDIC,CF=ans))
    
    #Rule 60.3
    @Rule(Manifestaion(name=LABS.BILIRUBIN),
          NOT(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN)),salience=priority-61
         )
    def func_60_3(self):
        ans=Handling_Choice_input("Do you Have any Pain in The Right upper side of your abs ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=ans))
    
    
    
    #Rule 61
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-61)
    def func_61(self,c0,c1,c2,c3,c4,f0,f1,f2,f3,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f3)
        self.retract(f4)
        
    #Rule 62
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3)
         )
    @Rule(salience=priority-62)
    def func_62(self,c0,c1,c2,c3,f0,f1,f2,f3):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f3)
    
    
    #Rule 63
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-63)
    def func_63(self,c0,c1,c2,c4,f0,f1,f2,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f4)

            
    #Rule 64
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-64)
    def func_64(self,c0,c1,c3,c4,f0,f1,f3,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f3)
        self.retract(f4)
 

    #Rule 65
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-65)
    def func_65(self,c0,c2,c3,c4,f0,f2,f3,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4) 
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f3)
        self.retract(f4)

            
    #Rule 66
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2)
          )
    @Rule(salience=priority-66)
    def func_66(self,c0,c1,c2,f0,f1,f2):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
    
    
    #Rule 67
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3)
         )
    @Rule(salience=priority-67)
    def func_67(self,c0,c1,c3,f0,f1,f3):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f3)
    
    
    #Rule 68
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3)
         )
    @Rule(salience=priority-68)
    def func_68(self,c0,c2,c3,f0,f2,f3):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f3)
    
    
    #Rule 69
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-69)
    def func_69(self,c0,c1,c4,f0,f1,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c1)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
        self.retract(f4)
    
    
    #Rule 70
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-71)
    def func_70(self,c0,c2,c4,f0,f2,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c2=c2*CHOLANGITIS[Clinic.FAVER]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c2)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f4)
     
    
    #Rule 71
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c3),
          AS.f4<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c4)
         )
    @Rule(salience=priority-70)
    def func_71(self,c0,c3,c4,f0,f3,f4):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c3=c3*CHOLANGITIS[LABS.BILIRUBIN]
        c4=c4*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c3)
        cf=CF(cf,c4)
        
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f3)
        self.retract(f4)
    
    #Rule 72
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.JAUNDIC,CF=MATCH.c1)
          )
    @Rule(salience=priority-80)
    def func_72(self,c0,c1,f0,f1):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.JAUNDIC]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
    
    #Rule 73
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c1)
          )
    @Rule(salience=priority-81)
    def func_73(self,c0,c1,f0,f1):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[Clinic.FAVER]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
         
    
    #Rule 74
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=LABS.BILIRUBIN,CF=MATCH.c1)
          )
    @Rule(salience=priority-74)
    def func_74(self,c0,c1,f0,f1):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[LABS.BILIRUBIN]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
    
    
    #Rule 75
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0),
          AS.f1<<Manifestaion(name=LABS.WHITE_BLOOD_CELLS,CF=MATCH.c1)
          )
    @Rule(salience=priority-75)
    def func_75(self,c0,c1,f0,f1):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        c1=c1*CHOLANGITIS[LABS.WHITE_BLOOD_CELLS]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=cf))
        self.retract(f0)
        self.retract(f1)
    
    #Rule 76
    @Rule(AS.f0<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN,CF=MATCH.c0))
    @Rule(salience=priority-61)
    def func_76(self,c0,f0):
        c0=c0*CHOLANGITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN]
        if check_Finish(c0):
            self.declare(Answer(name=DISEASE.CHOLANGITIS,pro=c0))
        self.retract(f0)
    
    
    