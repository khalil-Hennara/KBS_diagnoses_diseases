from Disease_CF import *
from Handling_Function import *
from fact_list import *

class Find_Soluation_For_Epegastric_Abdominal:

    #get Fact From Clinic Manifestation
    #Rule 0
    @Rule(AS.G<<GoalisTo(action=L("Abs")))
    @Rule(salience=priority)
    def func_0(self,G):
        ans=Handling_Abdominal()
        if ans!=0:
            for item in ans:
                self.declare(Manifestaion(name=item[0],CF=float(item[1])))
        else:
            self.modify(G,action="Diarrhea")
        return
    
    
    
    #Rule 1
    @Rule(Manifestaion(name=Clinic.HEART_BURN),
         NOT(Manifestaion(name=Clinic.REGURGITATION))
         )
    @Rule(salience=priority-1)
    def func_1(self):
        Reg=Handling_Choice_input("Do you Have REGURGITATION  ?" )
        Reg=get_the_Right_CF(Reg)
        self.declare(Manifestaion(name=Clinic.REGURGITATION,CF=Reg))
        
        
    @Rule(Manifestaion(name=Clinic.HEART_BURN),
         NOT(Manifestaion(name=Clinic.DYSPHAGIA))
         )
    @Rule(salience=priority-1)
    def func_1_1(self):
        Reg=Handling_Choice_input("Do you Have DYSPHAGIA ?" )
        Reg=get_the_Right_CF(Reg)
        self.declare(Manifestaion(name=Clinic.REGURGITATION,CF=Reg))
        

    #Rule 2    
    @Rule(AS.f1<<Manifestaion(name=Clinic.HEART_BURN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.REGURGITATION,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=Clinic.DYSPHAGIA,CF=MATCH.c2)
         )
    @Rule(salience=priority-2)
    def func_2(self,c0,c1,c2,f1,f2,f3):
        c0 = c0*GASTRO_ESPHAGEL[Clinic.HEART_BURN]
        c1 = c1*GASTRO_ESPHAGEL[Clinic.DYSPHAGIA]
        c2 = c2*GASTRO_ESPHAGEL[Clinic.REGURGITATION]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRO_ESPHAGEAL_REFLUX,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
        
    #Rule 3
    @Rule(AS.f1<<Manifestaion(name=L(Clinic.HEART_BURN),CF=MATCH.c1),
          AS.f2<<Manifestaion(name=L(Clinic.REGURGITATION),CF=MATCH.c2))
    @Rule(salience=priority-3)
    def func_3(self,c1,c2,f1,f2):
        c1=c1*GASTRO_ESPHAGEL[Clinic.HEART_BURN]
        c2=c2*GASTRO_ESPHAGEL[Clinic.REGURGITATION]
        cf=CF(c1,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRO_ESPHAGEAL_REFLUX,pro=cf))
            self.retract(f1)
            self.retract(f2)
    
    #Rule 4
    @Rule(AS.f1<<Manifestaion(name=L(Clinic.HEART_BURN),CF=MATCH.c0),
          AS.f2<<Manifestaion(name=L(Clinic.DYSPHAGIA),CF=MATCH.c1)
          )
    @Rule(salience=priority-4)
    def func_4(self,c0,c1,f1,f2):
        c0=c0*GASTRO_ESPHAGEL[Clinic.HEART_BURN]
        c1=c1*GASTRO_ESPHAGEL[Clinic.DYSPHAGIA]
        cf=CF(c0,c1)
        print(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRO_ESPHAGEAL_REFLUX,pro=cf))
            self.retract(f1)
            self.retract(f2)
    
    #Rule 5
    @Rule(AS.f1<<Manifestaion(name=L(Clinic.HEART_BURN),CF=MATCH.c0))
    @Rule(salience=priority-5)
    def func_5(self,c0,f1):
        c0 = c0*GASTRO_ESPHAGEL[Clinic.HEART_BURN]
        print(c0)
        if check_Finish(c0):
            self.declare(Answer(name=DISEASE.GASTRO_ESPHAGEAL_REFLUX,pro=c0))
        self.retract(f1)
  
        
    #Rule 6
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN),
         NOT(Manifestaion(name=Clinic.NOUSEA))
         )
    @Rule(salience=priority-6)
    def func_6(self):
        ans=Handling_Choice_input("Do you Have Nousea ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.NOUSEA,CF=ans))    
    
    
    #Rule 6.1
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN),
          NOT(Manifestaion(name=Clinic.BILE_VOMITTING)),
          NOT(Manifestaion(name=Clinic.VOMITING)),
          NOT(Manifestaion(name=Clinic.BLEEDING_VOMITING))
         )
    @Rule(salience=priority-6)
    def func_6_1(self):
        ans=Handling_Vomitting()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=1.0))
        else:
            self.declare(Manifestaion(name=Clinic.BILE_VOMITTING,CF=-0.97))
            self.declare(Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=-0.97))
            self.declare(Manifestaion(name=Clinic.VOMITING,CF=-0.97))
    
    
    #Rule 6.2
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN),
          NOT(Fact(name="LAB")),
          salience=priority-7)
    def func_6_2(self):
        print("You probably Have [ACUT PANCREATITIS] But you Have make a Blood Test.")
        ans=Handling_LAB_input()
        if ans!=0:
            for item in ans:
                self.declare(Manifestaion(name=item[0],CF=item[1]))
            self.declare(Fact(name="LAB"))
    
    
    #Rule 7
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=LABS.AMYLAS,CF=MATCH.c1),
          TEST(lambda c1:c1>0),
          AS.f3<<Manifestaion(name=LABS.LIBAS,CF=MATCH.c2),
          TEST(lambda c2:c2>0)
         )
    @Rule(salience=priority-7)
    def func_7(self,c0,c1,c2,f1,f2,f3):
        c0=c0*ACUT_PANCREATITIS[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN]
        c1=c1*ACUT_PANCREATITIS[LABS.AMYLAS]
        c2=c2*ACUT_PANCREATITIS[LABS.LIBAS]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.ACUT_PANCREATITIS,pro=cf))
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
    
    #Rule 8
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=LABS.LIBAS,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=LABS.AMYLAS,CF=MATCH.c2)
         )
    @Rule(salience=priority-8)
    def func_8(self,c0,c1,f1,f2,f3):
            self.retract(f1)
            self.retract(f2)
            self.retract(f3)
        
    
    #Rule 9
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=LABS.LIBAS,CF=MATCH.c1),
          TEST(lambda c1:c1>0)
          )
    @Rule(salience=priority-9)
    def func_9(self,c0,c1,f1,f2):
        c0=c0*ACUT_PANCREATITIS[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN]
        c1=c1*ACUT_PANCREATITIS[LABS.LIBAS]
        cf=CF(c0,c1)
        self.declare(Answer(name=DISEASE.ACUT_PANCREATITIS,pro=cf))
        self.retract(f1)
        self.retract(f2)
        
        
    #Rule 10
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=LABS.AMYLAS,CF=MATCH.c1),
          TEST(lambda c1:c1>0)
          )
    @Rule(salience=priority-10)
    def func_10(self,c0,c1,f1,f2):
        c0=c0*ACUT_PANCREATITIS[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN]
        c1=c1*ACUT_PANCREATITIS[LABS.AMYLAS]
        cf=CF(c0,c1)
        self.declare(Answer(name=DISEASE.ACUT_PANCREATITIS,pro=cf))
        self.retract(f1)
        self.retract(f2)
        
        
    
    #Rule 11
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,CF=MATCH.c0),
          Manifestaion(name=Clinic.VOMITING,CF=MATCH.c1),
          Manifestaion(name=Clinic.NOUSEA,CF=MATCH.c2)
         )
    @Rule(salience=priority-11)
    def func_11(self,c0,c1,c2,f1):
        c0=c0*ACUT_PANCREATITIS[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN]
        c1=c1*ACUT_PANCREATITIS[Clinic.VOMITING]
        c2=c2*ACUT_PANCREATITIS[Clinic.NOUSEA]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.ACUT_PANCREATITIS,pro=cf))
        self.retract(f1)
        
    
    #Rule 12
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),
          NOT(Manifestaion(name=Clinic.NOUSEA))
         )
    @Rule(salience=priority-12)
    def func_12(self):
        ans=Handling_Choice_input("Do you Have a [NOUSEA] ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.NOUSEA,CF=ans))
    
    #Rule 13
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),
          NOT(Manifestaion(name=Clinic.BLEEDING_VOMITING)),
          NOT(Manifestaion(name=Clinic.BILE_VOMITTING)),
          NOT(Manifestaion(name=Clinic.VOMITING))
         )
    @Rule(salience=priority-13)
    def func_13(self):
        ans=Handling_Vomitting()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=1.0))
    
    
    #Rule 14
    @Rule (Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),
           NOT(Fact(name="EGD"))
          )
    @Rule(salience=priority-14)
    def func_14(self):
        print("* * * * * * * * * * * * * * * * * *  * * * * * * *  * ")
        print("You probaley Have [DOUDENUM ULCER] But you should make an [EGD] Test." )
        print("* * * * * * * * * * * * * * * * * *  * * * * * * *  * ")
        ans=Handling_EGD_input()
        if ans!=0:
            for item in ans:
                self.declare(Manifestaion(name=item[0],CF=item[1]))
            self.declare(Fact(name="EGD"))
        
    #Rule 15
    @Rule(AS.f1<<Manifestaion(name=EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=L(Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),CF=MATCH.c1),
          Manifestaion(name=L(Clinic.BLEEDING_VOMITING),CF=MATCH.c2)
         )
    @Rule(salience=priority-15)
    def func_15(self,c0,c1,c2,f1,f2):
        c1=c1*DOUDENUM_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD]
        c2=c2*DOUDENUM_ULCER[Clinic.BLEEDING_VOMITING]
        c0=c0*DOUDENUM_ULCER[EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM]
        cf=CF(c1,c2)
        cf=CF(cf,c0)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.DOUDENUM_ULCER,pro=cf))
            self.retract(f2)
            self.retract(f1)
    
    #Rule 16
    @Rule(AS.f1<<Manifestaion(name=EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=L(Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),CF=MATCH.c1),
          )
    @Rule(salience=priority-16)
    def func_16(self,c0,c1,f1,f2):
        c1=c1*DOUDENUM_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD]
        c0=c0*DOUDENUM_ULCER[EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.DOUDENUM_ULCER,pro=cf))
            self.retract(f2)
            self.retract(f1)
    
    #Rule 17
    @Rule(AS.f1<<Manifestaion(name=L(Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),CF=MATCH.c0),
          Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=MATCH.c1) 
         )
    @Rule(salience=priority-17)
    def func_17(self,c0,c1,f1):
        c0=c0*DOUDENUM_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD]
        c1=c1*DOUDENUM_ULCER[Clinic.BLEEDING_VOMITING]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.DOUDENUM_ULCER,pro=cf))
            self.retract(f1)
    
    #Rule 18
    @Rule(AS.f1<<Manifestaion(name=L(Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD),CF=MATCH.c0))
    @Rule(salience=priority-18)
    def func_18(self,c0,f1):
        c0=c0*DOUDENUM_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD]
        if check_Finish(c0):
            self.declare(Answer(name=DISEASE.DOUDENUM_ULCER,pro=c0))
            self.retract(f1)
            
    #Rule 19
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD),
          NOT(Manifestaion(name=Clinic.NOUSEA))
         )
    @Rule(salience=priority-19)
    def func_19(self):
        ans=Handling_Choice_input("Do you Have a [NOUSEA] ? ")
        ans=get_the_Right_CF(ans)
        self.declare(Manifestaion(name=Clinic.NOUSEA,CF=ans))
    
    
    #Rule 20
    @Rule(Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD),
          NOT(Manifestaion(name=Clinic.BLEEDING_VOMITING)),
          NOT(Manifestaion(name=Clinic.BILE_VOMITTING)),
          NOT(Manifestaion(name=Clinic.VOMITING))
         )
    @Rule(salience=priority-20)
    def func_20(self):
        ans=Handling_Vomitting()
        if ans!=0:
            self.declare(Manifestaion(name=ans,CF=1.0))
        else:
            self.declare (Manifestaion(name=Clinic.BILE_VOMITTING,CF=-0.97))
            self.declare(Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=-0.98))
            self.declare(Manifestaion(name=Clinic.VOMITING,CF=-0.98))
    
    
    #Rule 21
    @Rule (Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD),
           NOT(Fact(name="EGD")))
    @Rule(salience=priority-21)
    def func_21(self):
        print("* * * * * * * * * * * * * * * * * *  * * * * * * *  * ")
        print("You probaley Have [STOMICH_ULCER] But you should make an [EGD] Test." )
        print("* * * * * * * * * * * * * * * * * *  * * * * * * *  * ")
        ans=Handling_EGD_input()
        if ans!=0:
            for item in ans:
                self.declare(Manifestaion(name=item[0],CF=item[1]))
            self.declare(Fact(name="EGD"))
    
    
    #Rule 22
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=MATCH.c1),
          AS.f3<<Manifestaion(name=EGD.ULCERS_AND_EROSIONS_IN_STOMACH,CF=MATCH.c2)
         )
    @Rule(salience=priority-22)
    def func_22(self,c0,c1,c2,f1,f2,f3):
        c0=c0*GASTRIC_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD]
        c1=c1*GASTRIC_ULCER[Clinic.BLEEDING_VOMITING]
        c2=c2*GASTRIC_ULCER[EGD.ULCERS_AND_EROSIONS_IN_STOMACH]
        cf=CF(c0,c1)
        cf=CF(cf,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRIC_ULCER,pro=cf))
        self.retract(f3)
        self.retract(f1)    
    #Rule 23
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD,CF=MATCH.c0),
          AS.f3<<Manifestaion(name=EGD.ULCERS_AND_EROSIONS_IN_STOMACH,CF=MATCH.c2)
         )
    @Rule(salience=priority-23)
    def func_23(self,c0,c2,f1,f3):
        c0=c0*GASTRIC_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD]
        c2=c2*GASTRIC_ULCER[EGD.ULCERS_AND_EROSIONS_IN_STOMACH]
        cf=CF(c0,c2)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRIC_ULCER,pro=cf))
        self.retract(f1)
        self.retract(f3)
    
    #Rule 24
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD,CF=MATCH.c0),
          AS.f2<<Manifestaion(name=Clinic.BLEEDING_VOMITING,CF=MATCH.c1)
          )
    @Rule(salience=priority-24)
    def func_24(self,c0,c1,f1,f2):
        c0=c0*GASTRIC_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD]
        c1=c1*GASTRIC_ULCER[Clinic.BLEEDING_VOMITING]
        cf=CF(c0,c1)
        if check_Finish(cf):
            self.declare(Answer(name=DISEASE.GASTRIC_ULCER,pro=cf))
        self.retract(f1)
            
    #Rule 25
    @Rule(AS.f1<<Manifestaion(name=Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD,CF=MATCH.c0))
    @Rule(salience=priority-25)
    def func_25(self,f1,c0):
        c0=c0*GASTRIC_ULCER[Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD]
        if check_Finish(c0):
            self.declare(Answer(name=DISEASE.GASTRIC_ULCER,pro=c0))
        self.retract(f1)