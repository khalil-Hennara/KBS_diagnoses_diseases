from Get_Value import *

worldShouldAnswerWith=["ALMOST","VERY MUCH","A LITTLE","SOMETIMES","YES","NEVER","NOT SURE","NO"]

EGDTest=["ULCERS AND EROSIONS IN DOUDENUM","ULCERS AND EROSIONS IN STOMACH","BLUNTED VILLI",
         "SUPER FACIAL INFLAMMATORY INFILTRATE",
         "DIFFUSE ULCERAION","PSEUDO POLPLUS","SUPERFICIAL CHRONIC INFLAMMATION","CRYPT ABSCESS",
         "DEEP AND LONG FISSURES","COBBLESTONING"]

diarrehea=["dIARRHEA","NON_GROSSLY_BLOODY_DIARRHEA","GROSSLY_BLOODY_DIARRHEA","CHRONIC_GREASY_DIARRHEA"]


abdominal=["EPIGASTRIC_ABDOMINAL","LEFT_UPPER_QUADRANT","RIGHT_UPPER_QUADRANT","ABDOMINAL"]

vomitting=["VOMITING","BILE_VOMITTING","BLEEDING_VOMITING"]

EGDTestWord=["VERY CLEAR","A Little","NOT CLEAR"]

LABAnser=["HIGH","NORMAL","LOW"]

def Handling_EGD_input():
    res=[]
    print("-----------------------------------------------------------------------------------------------------------------------")
    for index,item in enumerate(EGDTest):
        print(index+1,"["+item+"]  ",end=" ")
    print("\n---------------------------------------------------------------------------------------------------------------------")
    print("\n+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + ")
    for index,item in enumerate(EGDTestWord):
        print(str(index+1)+"["+item+"]\t",end=" ")
    
    print("\n+ + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + + +")
    print("\nPLEASE MAKE THE ANSWER TOW NUMBER THE FIRST ONE IS THE [MANIFISTATION] THE SECOND ONE IS THE DEGREE OF MANIFASTAION.")
    print("\n*****************************************************")
    print("YOU CAN END THE INPUT BY ENTERING [E\e].")
    print("*****************************************************\n")
    while True:
        f=input("The Number You Wont!")
        if f in ["E","e"]:
            break
        try:
            f=int(f)
            if f>=1 and f<=len(EGDTest):
                while True: 
                    s=input("PLEASE ENTER CERTAINTY NUMBER FROM 1 TO %d"%(len(EGDTestWord)))
                    try:
                        s=int(s)
                        if s>=1 and  s<=len(EGDTestWord):
                            g=get_The_Right_EGD(f-1)
                            c=get_CF_for_EGD(s-1)
                            res.append((g,c))
                            break
                        else:
                            continue
                    except ValueError:
                             print("PLEASE ENTER A VALID CERTAINTY NUMBER FROM 1 TO  %d"%(len(EGDTestWord)))
                             continue
            else :
                print("PLEASE ENTER A VALID MANIFISTATION NUMBER FROM 1 TO %d"%(len(EGDTest)))
        except ValueError:
                print("PLEASE ENTER A VALID MANIFISTATION NUMBER FROM 1 TO %d"%(len(EGDTest)))
                continue
    if len(res)>0:
        return res
    else:return 0
    
def Handling_LAB_input():
    res=[]
    index=1
    print("-----------------------------------------------------------------------------------")    
    for i in LABS:
        i=str(i)
        print(index,"["+i[5:]+"] ",end=" ")
        index+=1
    print("\n-----------------------------------------------------------------------------------")
    index-=1
    while True:
        f=input("PLEASE ENTER THE NUMBER OF [ENZYM] YOU WON'T OR END BY PRESSING [e\E] ")
        print("-----------------------------------------------------------------------------------")
        if f in ["E","e"]:break
        try:
            f=int(f)
            if f>=1 and f<=index:
                for i,item in enumerate(LABAnser):
                    print(i+1,":"+item+" ",end=" ")
                print("\n+ + + + + + + + + + + + + + + + + +\n")
                
                while True:
                    s=input("PLEASE ENTER THE RIGHT RANGE. ")
                    try:
                        s=int(s)
                        if s>=1 and s<=3:
                            if s==2:
                                break
                            if f==index and s==1:
                                f=get_The_Right_Labs(f-1)
                                res.append((f,-0.9))
                            elif f<index and s==3:
                                f=get_The_Right_Labs(f-1)
                                res.append((f,-0.9))
                            else:
                                f=get_The_Right_Labs(f-1)
                                res.append((f,1))
                            break
                    except ValueError:
                        continue    
        except ValueError:
                    continue
    if len(res)>0:
        return res
    else:
        return 0

    

    
def Handling_ECHO_input():
    res=[]
    index=1
    print("-------------------------------------------------------------------------------------")    
    for i in ECHO:
        i=str(i)
        print(index,"["+i[5:]+"] ",end=" ")
        index+=1
    print("\n-----------------------------------------------------------------------------------")    
    index-=1
    while True:
        f=input("PLEASE ENTER THE DESCRIPTION OF WHAT YOU CAN SEE IN THE [ECHO] OR YOU CAN END THE INPUT BY ENTERING [E\e] ")
        print("-----------------------------------------------------------------------------------")    
        if f in ["E","e"]:break
        try:
            f=int(f)
            if f>=1 and f<=index:
                f=get_The_Right_Echo(f-1)
                res.append(f)
        except ValueError:
            continue
    if len(res)>0:
        return res
    else :
        return 0
   




def Handling_Choice_input(Question):
    print("------------------------------------------------------------------------------------------------")
    for index,item in enumerate(worldShouldAnswerWith):
        print(index+1,"["+item+"]\t",end=" ")
    print("\n----------------------------------------------------------------------------------------------")
    while True:
        v=input(Question)
        print("-------------------------------------------------------------------------------------------")
        try:
            v=int(v)
            if v<=len(worldShouldAnswerWith) and v>=1:
                break
            else:
                print("PLEASE CHOOSE A VALID VALUE FROM 1 To %d  \n"%(len(worldShouldAnswerWith)))
        except ValueError:
            print("PLEASE CHOOSE A VALID VALUE FROM 1 To %d \n"%(len(worldShouldAnswerWith)))
            continue
    return v



def Handling_YES_NO_input(Question):
    print ("THE ANSWER SHOULD BE (y\[n]) ")
    ans=input(Question)
    if ans in ["YES","yes","y","Y"]:
         return 1
    else:
         return 0
        

def Handling_diarrhea():
    ans=Handling_YES_NO_input("Is Ther Any Diarrhea ?  ")
    if ans==0:return 0
    else :
        print("-----------------------------------------------------------------------")
        print("could you please choose one of this list to describe The [ DIARRHEA ] you Have ? ")
        print("-----------------------------------------------------------------------\n")
        for index,item in enumerate(diarrehea):
            print(index+1,"["+item+"] ",end=" ")
        while True:
            f=input()
            try:
                f=int(f)
                if f>=1 and f<=len(diarrehea):
                    if f==1:return Clinic.dIARRHEA
                    elif f==2:return Clinic.NON_GROSSLY_BLOODY_DIARRHEA
                    elif f==3:return Clinic.GROSSLY_BLOODY_DIARRHEA
                    elif f==4:return Clinic.CHRONIC_GREASY_DIARRHEA
            except ValueError:
                print("Enter A Valid Value !")

                
                
                
def Handling_Vomitting():
    ans=Handling_YES_NO_input("Do you Have A VOMITTING ? ")
    if ans==0:return 0
    else :
        print("-----------------------------------------------------------------------")
        print("could you please choose one of this list to describe The [ VOMITTING ] you Have ? ")
        print("-----------------------------------------------------------------------\n")
        for index,item in enumerate(vomitting):
            print(index+1,"["+item+"] ",end=" ")
        while True:
            f=input()
            try:
                f=int(f)
                if f>=1 and f<=len(vomitting):
                    if f==1:return Clinic.VOMITING
                    elif f==2:return Clinic.BILE_VOMITTING
                    elif f==3:return Clinic.BLEEDING_VOMITING
            except ValueError:
                print("Enter A Valid Value !")
                
                
                
def Handling_Abdominal():
    ans=Handling_YES_NO_input("Do you Have Abdominal Pain  ? ")
    res=[]
    if ans==0:return 0
    else :
        res.append((Clinic.ABDOMINAL_PAIN,1))
        print("-----------------------------------------------------------------------")
        print("could you please choose one of this list to describe The [ ABDOMINAL PAIN ] you Have ? ")
        print("-----------------------------------------------------------------------\n")
        index=1
        for i in abdominal:
            print(index,"["+i+"] ",end=" ")
            index+=1
        index-=1
        while True:
            f=input()
            try:
                f=int(f)
                
                if f==3:
                    ans=Handling_YES_NO_input("Is There any Pain In The SHOULDER ?  ")
                    if ans == 1:res.append((Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT,1))
                    else :res.append((Clinic.RIGHT_UPPER_QUADRANT_PAIN,1))
                    return res
                
                elif f==2:
                    res.append((Clinic.LEFT_UPPER_QUADRANT_PAIN,1))
                    return res
                
                elif f==1:
                    ans=Handling_YES_NO_input("Is There any Pain in The Back ?  ")
                    if ans==1:res.append ((Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN,1))
                    
                    ans=Handling_YES_NO_input("Is There any Pain In The Chest ?  ")
                    if ans==1:res.append((Clinic.HEART_BURN,1))
                    
                    ans=Handling_YES_NO_input("Dose Pain Worsed By Food ? ")
                    if ans == 1:res.append((Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD,1))
                    else :
                        ans=Handling_YES_NO_input("Dose Pain Releved By Food ?")
                        if ans == 1:res.append((Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD,1))
                    
                    if len(res)>0:
                        return res
                    else:
                        res.append((Clinic.EPIGASTRIC_ABDOMINAL_PAIN,1))
                        return res
                elif f==4:
                    ans=Handling_YES_NO_input("Dose Pain Worsed by Food ?")
                    if ans==1:res.append((Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD,1))
                    
                    ans =Handling_YES_NO_input("Dose Pain Worsed by Strees ?")
                    if ans==1:res.append((Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS,1))
                    return res
                
                else :
                    print("Enter A Valid Value !")
            except ValueError:
                print("Enter A Valid Value ! ")

        
        