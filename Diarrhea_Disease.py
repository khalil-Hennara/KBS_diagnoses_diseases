from Disease_CF import *
from Handling_Function import *
from fact_list import *

class Find_Disease_Realting_to_diarrhea:
        
        #Rule 96
        @Rule (AS.gol<<GoalisTo(action="Diarrhea"),
               NOT(Fact(name="diarrhea"))
              )
        @Rule(salience=priority-96)
        def func_96(self,gol):
            ans=Handling_diarrhea()
            if ans!=0:
                self.declare(Manifestaion(name=ans,CF=1))
            else :
                self.modify(gol,action="getAnother")
            self.declare(Fact(name="diarrhea"))
           
    
        #Rule 97
        @Rule(Manifestaion(name=Clinic.dIARRHEA),
              NOT(GoalisTo(action="getColon")),
              AS.gol<<GoalisTo(action=MATCH.ac)
             )
        @Rule(salience=priority-97)
        def func_97(self,gol):
            self.modify(gol,action="getColon")
    
    
        #Rule 98
        @Rule (Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA),
               NOT(Manifestaion(name=Clinic.WEIGH_LOSS))
              )
        @Rule (salience=priority-96)
        def func_98(self):
            ans=Handling_Choice_input("Do you Have WEIGH LOSS ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
    
        #Rule 99
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               NOT(Fact(name="LAB")),
               NOT(Fact(name="EGD"))
              )
        @Rule (salience=priority-96)
        def func_99(self,c0,c1,f0):
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . .  .\n")
            print("You probably Have [CELIAC DISEASE] but you Should made blood Test or [EGD] Test \n" )
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . .  .\n")
        
            ans=Handling_YES_NO_input("Would you made a [Blood] Test.")
            if ans==0:
                ans=Handling_YES_NO_input("Would you made [EGD] Test.")
                if ans==0:
                    c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
                    c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
                    cf=CF(c0,c1)
                    if check_Finish(cf):
                        self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
                    self.retract(f0)
                else:
                    ans=Handling_EGD_input()
                    if ans!=0:
                        for item in ans:
                            self.declare(Manifestaion(name=item[0],CF=item[1]))
                            self.declare(Fact(name="EGD"))
                    else:
                        c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
                        c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
                        cf=CF(c0,c1)
                        if check_Finish(cf):
                            self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
                        self.retract(f0)
            else:
                ans=Handling_LAB_input()
                if ans!=0:
                    for item in ans:
                        self.declare(Manifestaion(name=item,CF=1))
                        self.declare(Fact(name="LAB"))
                else:
                    c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
                    c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
                    cf=CF(c0,c1)
                    if check_Finish(cf):
                        self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
                    self.retract(f0)
        
        
        #Rule 160
        @Rule(Manifestaion(name=LABS.IGA_AGA),
              NOT(Manifestaion(name=Clinic.WEIGH_LOSS)),salience=priority-96
             )
        def func_160(self):
            ans=Handling_Choice_input("Do you Have [wight loss] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
            
        #Rule 161
        @Rule(Manifestaion(name=LABS.IGA_ATTA),
              NOT(Manifestaion(name=Clinic.WEIGH_LOSS)),salience=priority-96
             )
        def func_161(self):
            ans=Handling_Choice_input("Do you Have [wight loss] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
        
        
        #Rule 162
        @Rule(Manifestaion(name=LABS.IGA_AGA),
              NOT(Fact(name="diarrhea")),salience=priority-96
             )
        def func_162(self):
            ans=Handling_Choice_input("Do you Have [Greasy Diarrhea] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=ans))
            self.declare(Fact(name="diarrhea"))
        
                         
        #Rule 162
        @Rule(Manifestaion(name=LABS.IGA_ATTA),
              NOT(Fact(name="diarrhea")),salience=priority-97
             )
        def func_163(self):
            ans=Handling_Choice_input("Do you Have [Greasy Diarrhea] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=ans))
            self.declare(Fact(name="diarrhea"))
        
        
                         
        #Rule 100_1
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3)
              )
        @Rule (salience=priority-97)
        def func_100_1(self,f1,f2,f3,c1,c2,c3):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            
            cf=CF(c1,c2)
            cf=CF(cf,c3)            
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f2)
            self.retract(f3)
                         
        #Rule 100_2
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              
              )
        @Rule (salience=priority-98)
        def func_100_2(self,f1,f2,f3,c1,c2,c3,f4,c4):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c1,c2)
            cf=CF(cf,c3)            
            cf=CF(cf,c4) 
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f2)
            self.retract(f3)
            self.retract(f4)
        
        #Rule 100_3
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              
              )
        @Rule (salience=priority-99)
        def func_100_3(self,f1,f2,f3,c1,c2,c3):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c1,c2)            
            cf=CF(cf,c4) 
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f2)
            self.retract(f4)
                         
       
        #Rule 100_4
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              )
        @Rule (salience=priority-100)
        def func_100_4(self,f1,f3,c1,c3,f4,c4):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c1,c3)            
            cf=CF(cf,c4) 
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f3)
            self.retract(f4)
        
        #Rule 100_5
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2)
              )
        @Rule (salience=priority-101)
        def func_100_5(self,f1,f2,c1,c2):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            cf=CF(c1,c2)
             
                         
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f2)
        
                         
       #Rule 100_6
        @Rule (AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c2)
              )
        @Rule (salience=priority-102)
        def func_100_6(self,f1,f2,c1,c2):
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_AGA]
            cf=CF(c1,c2) 
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f2)
                          
        #Rule 100
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              )
        @Rule (salience=priority-94)
        def func_100(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)            
            cf=CF(cf,c4)
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
            self.retract(f3)
            self.retract(f4)
                
            
        #Rule 101
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3)
               )
        @Rule (salience=priority-95)
        def func_101(self,f0,f1,f2,f3,c0,c1,c2,c3):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)            
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
            self.retract(f3)
                 
            
        
        #Rule 102
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              )
        @Rule (salience=priority-99)
        def func_102(self,f0,f1,f2,f4,c0,c1,c2,c4):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c4)
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
            self.retract(f4)
                
        #Rule 103
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              )
        @Rule (salience=priority-100)
        def func_103(self,f0,f1,f3,f4,c0,c1,c3,c4):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)            
            cf=CF(cf,c4)
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f3)
            self.retract(f4)
                   
        #Rule 104
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=LABS.IGA_ATTA,CF=MATCH.c2)
              )
        @Rule (salience=priority-101)
        def func_104(self,f0,f1,f2,c0,c1,c2):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[LABS.IGA_ATTA]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
        
        
        #Rule 105
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=LABS.IGA_AGA,CF=MATCH.c3)
               )
        @Rule (salience=priority-102)
        def func_105(self,f0,f1,f3,c0,c1,c3):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c3=c3*CELIAC_DISEASE[LABS.IGA_AGA]
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)            
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f3)
        
        #Rule 106
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f4<<Manifestaion(name=LABS.HIMOGLOBIN,CF=MATCH.c4)
              )
        @Rule (salience=priority-103)
        def func_106(self,f0,f1,f4,c0,c1,c4):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c4=c4*CELIAC_DISEASE[LABS.HIMOGLOBIN]
            
            cf=CF(c0,c1)
            cf=CF(cf,c4)
             
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f4)
                
            
        
        
        
        #Rule 164
        @Rule(Manifestaion(name=EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE),
              NOT(Manifestaion(name=Clinic.WEIGH_LOSS)),
              salience=priority-104
             )
        def func_164(self):
            ans=Handling_Choice_input("Do you Have [Wight Loss] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
        
        
        
        #Rule 165
        @Rule(Manifestaion(name=EGD.BLUNTED_VILLI),
              NOT(Manifestaion(name=Clinic.WEIGH_LOSS)),
              salience=priority-105
             )
        def func_165(self):
            ans=Handling_Choice_input("Do you Have [Wight Loss] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.WEIGH_LOSS,CF=ans))
        
        
        
        #Rule 166
        @Rule(Manifestaion(name=EGD.BLUNTED_VILLI),
              NOT(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA)),NOT(Fact(name="ok")),salience=priority-104
             )
        def func_166(self):
            ans=Handling_Choice_input("Do you Have [Greasy Diarrhea] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=ans))
            self.declare(Fact(name="ok"))
            self.declare(Fact(name="diarrhea"))
        
        #Rule 167
        @Rule(Manifestaion(name=EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE),
              NOT(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA)),NOT(Fact(name="ok")),salience=priority-96
             )
        def func_167(self):
            ans=Handling_Choice_input("Do you Have [Greasy Diarrhea] ? ")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=ans))
            self.declare(Fact(name="ok"))
            self.declare(Fact(name="diarrhea"))
            
        
        
        #Rule 107
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=EGD.BLUNTED_VILLI,CF=MATCH.c3)
               )
        @Rule (salience=priority-106)
        def func_107(self,f0,f1,f2,f3,c0,c1,c2,c3):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE]
            c3=c3*CELIAC_DISEASE[EGD.BLUNTED_VILLI]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
            self.retract(f3)
        
        #Rule 108
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE,CF=MATCH.c2),
               )
        @Rule (salience=priority-108)
        def func_108(self,f0,f1,f2,c0,c1,c2):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c2=c2*CELIAC_DISEASE[EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE]
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f2)
            
         
        #Rule 109
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=EGD.BLUNTED_VILLI,CF=MATCH.c3)
               )
        @Rule (salience=priority-107)
        def func_109(self,f0,f1,f3,c0,c1,c3):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]
            c3=c3*CELIAC_DISEASE[EGD.BLUNTED_VILLI]
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
            self.retract(f0)
            self.retract(f3)
                
        #Rule  110
        @Rule (AS.f0<<Manifestaion(name=Clinic.CHRONIC_GREASY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.WEIGH_LOSS,CF=MATCH.c1)
              )
        @Rule (salience=priority-109)
        def func_110(self,f0,f1,c0,c1):
            c0=c0*CELIAC_DISEASE[Clinic.CHRONIC_GREASY_DIARRHEA]
            c1=c1*CELIAC_DISEASE[Clinic.WEIGH_LOSS]    
            cf=CF(c0,c1)
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.CELIAC_DISEASE,pro=cf))
                self.retract(f0)
                
            else :
                self.retract(f0)
        
        
        
        
        #Rule 111
        @Rule (Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA),
               NOT(Manifestaion(name=Clinic.TENESMUS))
              )
        @Rule (salience=priority-100)
        def func_111(self):
            ans=Handling_Choice_input("Do you Have Tenesum")
            ans=get_the_Right_CF(ans)
            self.declare(Manifestaion(name=Clinic.TENESMUS,CF=ans))
        
        
        #Rule 112
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA),
               Manifestaion(name=Clinic.TENESMUS),
               NOT(Fact(name="EGD"))
              )
        @Rule(salience=priority-100)
        def func_112(self,f0):
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . .  .\n")
            print("You probably Have [CELIAC DISEASE] but you Should made blood Test or [EGD] Test\n" )
            print(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .. . . .  .\n")
            ans=Handling_EGD_input()
            if ans!=0:
                for item in ans:
                    self.declare(Manifestaion(name=item[0],CF=item[1]))
                self.declare(Fact(name="EGD"))
            else:
                self.retract(f0)
            
            
        #Rule 113    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_113(self,f0,f1,f2,f3,f4,f5,c0,c1,c2,c3,c4,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)
            cf=CF(cf,c4)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f3)
                self.retract(f4)
                self.retract(f5)
            
        
        
        #Rule 114    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4)
              )
        @Rule(salience=priority-100)
        def func_114(self,f0,f1,f2,f3,f4,c0,c1,c2,c3,c4):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)
            cf=CF(cf,c4)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f3)
                self.retract(f4)
           
        
        #Rule 115    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_115(self,f0,f1,f2,f3,f5,c0,c1,c2,c3,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f3)
                self.retract(f5)
        
        
        
        #Rule 116    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_116(self,f0,f1,f2,f4,f5,c0,c1,c2,c4,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c4)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f4)
                self.retract(f5)
        
    
    
        #Rule 117    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_117(self,f0,f1,f3,f4,f5,c0,c1,c3,c4,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)
            cf=CF(cf,c4)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f3)
                self.retract(f4)
                self.retract(f5)
            
        
        
        #Rule 118    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3)
               )
        @Rule(salience=priority-100)
        def func_118(self,f0,f1,f2,f3,c0,c1,c2,c3):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c3)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f3)
            
        
        
        #Rule 118.1    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4)
              )
        @Rule(salience=priority-100)
        def func_118_1(self,f0,f1,f2,f4,c0,c1,c2,c4):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c4)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f4)
            
        
        #Rule 119    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4)
               )
        @Rule(salience=priority-100)
        def func_119(self,f0,f1,f3,f4,c0,c1,c3,c4):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)
            cf=CF(cf,c4)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f3)
                self.retract(f4)
               
        
        
        #Rule 120    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_120(self,f0,f1,f2,f5,c0,c1,c2,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
                self.retract(f5)
        
        
        #Rule 121    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_121(self,f0,f1,f3,f5,c0,c1,c3,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f3)
                self.retract(f5)
        
        
        
        
        #Rule 122    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f4<<Manifestaion(name=EGD.SUPERFICIAL_CHRONIC_INFLAMMATION,CF=MATCH.c4),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        
        @Rule(salience=priority-100)
        def func_122(self,f0,f1,f4,f5,c0,c1,c4,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c4=c4*ULCERATIVE_COLITIS[EGD.SUPERFICIAL_CHRONIC_INFLAMMATION]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c4)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f4)
                self.retract(f5)
        
           
            
       #Rule 123    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f2<<Manifestaion(name=EGD.DIFFUSE_ULCERAION,CF=MATCH.c2)
               )
        @Rule(salience=priority-100)
        def func_123(self,f0,f1,f2,c0,c1,c2):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c2=c2*ULCERATIVE_COLITIS[EGD.DIFFUSE_ULCERAION]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c2)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f2)
        
        
        #Rule 124    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f3<<Manifestaion(name=EGD.PSEUDO_POLPLUS,CF=MATCH.c3),
              )
        @Rule(salience=priority-100)
        def func_124(self,f0,f1,f3,c0,c1,c3):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c3=c3*ULCERATIVE_COLITIS[EGD.PSEUDO_POLPLUS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c3)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f3)
        
        
        #Rule 125    
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA,CF=MATCH.c0),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS,CF=MATCH.c1),
               AS.f5<<Manifestaion(name=EGD.CRYPT_ABSCESS,CF=MATCH.c5)
              )
        @Rule(salience=priority-100)
        def func_125(self,f0,f1,f5,c0,c1,c5):
            c0=c0*ULCERATIVE_COLITIS[Clinic.GROSSLY_BLOODY_DIARRHEA]
            c1=c1*ULCERATIVE_COLITIS[Clinic.TENESMUS]
            c5=c5*ULCERATIVE_COLITIS[EGD.CRYPT_ABSCESS]
            
            
            cf=CF(c0,c1)
            cf=CF(cf,c5)
            
            if check_Finish(cf):
                self.declare(Answer(name=DISEASE.ULCERATIVE_COLITIS,pro=cf))
                self.retract(f0)
                self.retract(f1)
                self.retract(f5)
        
        #Rule 126
        @Rule (AS.f0<<Manifestaion(name=Clinic.GROSSLY_BLOODY_DIARRHEA),
               AS.f1<<Manifestaion(name=Clinic.TENESMUS)
              )
        @Rule (salience=priority-126)
        def func_126(self,f0,f1):
            self.retract(f0)
            self.retract(f1)
        
        

        #Rule 127
        @Rule (NOT(GoalisTo(action="getAnother")),
               NOT(GoalisTo(action="getColon")),
               AS.gol<<GoalisTo(action=MATCH.ac)
              )
        def func_127(self,gol):
            self.modify(gol,action="getAnother")
        
            
        