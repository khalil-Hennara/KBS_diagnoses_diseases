from manifestation import *

def get_The_Right_EGD(value):
        if   value == 0:return EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM
        elif value == 1:return EGD.ULCERS_AND_EROSIONS_IN_STOMACH
        elif value == 2:return EGD.BLUNTED_VILLI
        elif value == 3:return EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE
        elif value == 4:return EGD.DIFFUSE_ULCERAION
        elif value == 5:return EGD.PSEUDO_POLPLUS
        elif value == 6:return EGD.SUPERFICIAL_CHRONIC_INFLAMMATION
        elif value == 7:return EGD.CRYPT_ABSCESS
        elif value == 8:return EGD.DEEP_AND_LONG_FISSURES
        elif value == 9:return EGD.COBBLESTONING
        
def get_The_Right_Labs(value):
        if   value == 0:return LABS.IGA_ATTA
        elif value == 1:return LABS.IGA_AGA
        elif value == 2:return LABS.AMYLAS
        elif value == 3:return LABS.LIBAS
        elif value == 4:return LABS.BILIRUBIN
        elif value == 5:return LABS.WHITE_BLOOD_CELLS
        elif value == 6:return LABS.PLATLTE
        elif value == 7:return LABS.HIMOGLOBIN

def get_The_Right_Echo(value):
        if   value == 0:return ECHO.GALLBLADDER_WALL_THICKENING
        elif value == 1:return ECHO.PERICHOLECYSTIC_FLUID
        elif value == 2:return ECHO.HIBATOMIGALI
        elif value == 3:return ECHO.SPLINO_MIGALI
        elif value == 4:return ECHO.FREE_LIQUADE

def get_the_Right_CF(value):
        if   value == 1:return 0.6
        elif value == 2:return 1.0
        elif value == 3:return 0.2
        elif value == 4:return 0.5
        elif value == 5:return 1.0
        elif value == 6:return -1.0
        elif value == 7:return  0
        elif value == 8:return -1.0

def get_CF_for_EGD(value):
    if value==0:
        return 0.9
    elif value==1:
        return 0.4
    else :
        return 0
 

