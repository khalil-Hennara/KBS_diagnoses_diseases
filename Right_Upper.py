from Disease_CF import *
from Handling_Function import *
from fact_list import *


class Find_soluation_For_upper_Right_ABS_With_Shoulder_Pain:
    
    #Rule 26
    @Rule(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT),
          NOT(Manifestaion(name=Clinic.NOUSEA))
         )
    @Rule(salience=priority-26)
    def func_26(self):
        ans=Handling_Choice_input("Do you Have a [NOUSEA] ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.NOUSEA,CF=ans))
    
    
    #Rule 27
    @Rule(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT),
          NOT(Manifestaion(name=Clinic.VOMITING)),
          NOT(Manifestaion(name=Clinic.BLEEDING_VOMITING)),
          NOT(Manifestaion(name=Clinic.BILE_VOMITTING))
         )
    @Rule(salience=priority-27)
    def func_27(self):
        ans=Handling_Vomitting()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=1.0))
    
        else:
            self.declare (Manifestaion(name=Clinic.BILE_VOMITTING,CF=-0.97))
            self.declare(Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=-0.98))
            self.declare(Manifestaion(name=Clinic.VOMITING,CF=-0.98))
    
    
    
    #Rule 28
    @Rule(Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT),
          NOT(Manifestaion(name=Clinic.FAVER))
         )
    @Rule(salience=priority-28)
    def func_28(self):
        ans=Handling_Choice_input("Do you Have Fever ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.FAVER,CF=ans))
    
    
    #Rule 29
    @Rule (Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT),
           NOT(Fact(name="ECHO"))
          )
    @Rule (salience=priority-29)
    def func_29(self):
        print("You probably Have [CHOLECYSTITIS] But you Have to make an [ECHO] ")
        ans=Handling_ECHO_input()
        if ans !=0:
            for item in ans:
                self.declare(Manifestaion(name=item,CF=0.98))
            self.declare(Fact(name="ECHO"))
    
    #Rule 30
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-30)
    def func_30(self,f1,f2,f3,f4,f5,f6,c0,c1,c2,c3,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
    
    #Rule 31
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4)
         )
    @Rule(salience=priority-31)
    def func_31(self,f1,f2,f3,f4,f5,c0,c1,c2,c3,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
            
    #Rule 32
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-32)
    def func_32(self,f1,f2,f3,f4,f6,c0,c1,c2,c3,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
            
            
    #Rule 33
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-33)
    def func_33(self,f1,f2,f3,f5,f6,c0,c1,c2,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
    
    
    #Rule 34
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-34)
    def func_34(self,f1,f2,f4,f5,f6,c0,c1,c3,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            
    #Rule 35
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-35)
    def func_35(self,f1,f3,f4,f5,f6,c0,c2,c3,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
            
    #Rule 36
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3)
         )
    @Rule(salience=priority-36)
    def func_36(self,f1,f2,f3,f4,c0,c1,c2,c3):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
    
    #Rule 37
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4)
         )
    @Rule(salience=priority-37)
    def func_37(self,f1,f2,f3,f5,c0,c1,c2,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
    
    #Rule 38
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4)
         )
    @Rule(salience=priority-38)
    def func_38(self,f1,f2,f4,f5,c0,c1,c3,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            
    
    #Rule 39
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4)
         )
    @Rule(salience=priority-39)
    def func_39(self,f1,f3,f4,f5,c0,c2,c3,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
            
    
    
    #Rule 40
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-40)
    def func_40(self,f1,f2,f3,f6,c0,c1,c2,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
            
    #Rule 41
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-41)
    def func_41(self,f1,f2,f4,f6,c0,c1,c3,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f4)
            
            
    #Rule 42
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-42)
    def func_42(self,f1,f3,f4,f6,c0,c2,c3,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
    
    
    
    #Rule 43
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-43)
    def func_43(self,f1,f2,f5,f6,c0,c1,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
          
    
    
    #Rule 44
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-44)
    def func_44(self,f1,f3,f5,f6,c0,c2,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c2)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
    
    
    #Rule 45
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-45)
    def func_45(self,f1,f4,f5,f6,c0,c3,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c3)
        cf=CF(cf,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
    
    
    #Rule 46
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2)
         )
    @Rule(salience=priority-46)
    def func_46(self,f1,f2,f3,c0,c1,c2):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
    
    
    
    #Rule 47
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3)
         )
    @Rule(salience=priority-47)
    def func_47(self,f1,f2,f4,c0,c1,c3):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        cf=CF(c0,c1)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
    
    
    #Rule 48
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f4<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c3)
         )
    @Rule(salience=priority-48)
    def func_48(self,f1,f3,f4,c0,c2,c3):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c3=c3*CHOLECYSTITIS[Clinic.VOMITING]
        cf=CF(c0,c2)
        cf=CF(cf,c3)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
            
    #Rule 49
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c1),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-49)
    def func_49(self,f1,f2,f6,c0,c1,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c1=c1*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
    
    
    #Rule 50
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c2),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-50)
    def func_50(self,f1,f3,f6,c0,c2,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c2=c2*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c2)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f3)
    
    
    #Rule 51
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4),
          AS.f6<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c5)
         )
    @Rule(salience=priority-51)
    def func_51(self,f1,f5,f6,c0,c4,c5):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        c5=c5*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c4)
        cf=CF(cf,c5)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
    
    
    #Rule 52
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=Clinic.FAVER,CF=MATCH.c4)
         )
    @Rule(salience=priority-52)
    def func_52(self,f1,f5,c0,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[Clinic.FAVER]
        cf=CF(c0,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
    
    
    #Rule 53
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c4)
         )
    @Rule(salience=priority-53)
    def func_53(self,f1,f5,c0,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[Clinic.NOUSEA]
        cf=CF(c0,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
    
    
    #Rule 54
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=Clinic.VOMITING,CF=MATCH.c4)
         )
    @Rule(salience=priority-54)
    def func_54(self,f1,f5,c0,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[Clinic.VOMITING]
        cf=CF(c0,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            
            
    #Rule 55
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=ECHO.GALLBLADDER_WALL_THICKENING,CF=MATCH.c4)
         )
    @Rule(salience=priority-55)
    def func_55(self,f1,f5,c0,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[ECHO.GALLBLADDER_WALL_THICKENING]
        cf=CF(c0,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f5)
            
            
    #Rule 56
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0),
          AS.f5<<Manifestaion(name=ECHO.PERICHOLECYSTIC_FLUID,CF=MATCH.c4)
         )
    @Rule(salience=priority-56)
    def func_56(self,f1,f5,c0,c4):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        c4=c4*CHOLECYSTITIS[ECHO.PERICHOLECYSTIC_FLUID]
        cf=CF(c0,c4)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=cf))
            self.retract(f1)
            self.retract(f5)
    
     #Rule 57
    @Rule(AS.f1<<Manifestaion(name=Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,CF=MATCH.c0))
    @Rule(salience=priority-57)
    def func_57(self,f1,c0):
        c0=c0*CHOLECYSTITIS[Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT]
        if check_Finish(c0):
            self.declare(Answer(name=DISEASE.CHOLECYSTITIS,pro=c0))
            self.retract(f1)
    