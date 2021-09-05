from manifestation import *

GASTRO_ESPHAGEL = {Clinic.HEART_BURN:0.7,Clinic.REGURGITATION:0.2,Clinic.DYSPHAGIA:0.3}

DOUDENUM_ULCER  = {Clinic.EPIGASTRIC_ABDOMINAL_PAIN_RELIVED_WITH_FOOD:0.7,Clinic.NOUSEA:0.2,
                    Clinic.BLEEDING_VOMITING:0.5,EGD.ULCERS_AND_EROSIONS_IN_DOUDENUM:0.9}

GASTRIC_ULCER   = {Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WORSED_WITH_FOOD:0.7,Clinic.NOUSEA:0.2,
                    Clinic.BLEEDING_VOMITING:0.5,EGD.ULCERS_AND_EROSIONS_IN_STOMACH:0.9}

CELIAC_DISEASE  = {Clinic.CHRONIC_GREASY_DIARRHEA:0.7,Clinic.WEIGH_LOSS:0.6,LABS.HIMOGLOBIN:0.4,
                    LABS.IGA_AGA:0.7,LABS.IGA_ATTA:0.9,EGD.BLUNTED_VILLI:0.9,
                    EGD.SUPER_FACIAL_INFLAMMATORY_INFILTRATE:0.8}

ULCERATIVE_COLITIS = {Clinic.GROSSLY_BLOODY_DIARRHEA:0.7,Clinic.TENESMUS:0.3,Clinic.ERYTHEMA_NODOSUM:0.2,
                       Clinic.UVEITIS:0.2,Clinic.SERONEG_ARTHRITIS:0.2,EGD.DIFFUSE_ULCERAION:0.7,
                        EGD.PSEUDO_POLPLUS:0.5,EGD.SUPERFICIAL_CHRONIC_INFLAMMATION:0.8,
                        EGD.CRYPT_ABSCESS:0.6}

CROHN_DISEASE  = {Clinic.ABDOMINAL_PAIN:0.5,Clinic.FAVER:0.2,Clinic.WEIGH_LOSS:0.4,Clinic.dIARRHEA:0.4,
                    Clinic.NON_GROSSLY_BLOODY_DIARRHEA:0.7,EGD.DEEP_AND_LONG_FISSURES:0.8,
                    EGD.COBBLESTONING:0.9}

ACUT_PANCREATITIS = {Clinic.EPIGASTRIC_ABDOMINAL_PAIN_WITH_BACK_PAIN:0.6,Clinic.NOUSEA:0.2,Clinic.VOMITING:0.2,
                     LABS.AMYLAS:0.6,LABS.LIBAS:0.8}


CHOLECYSTITIS   = {Clinic.RIGHT_UPPER_QUADRANT_PAIN_SHOULDER_RIGHT:0.7,Clinic.NOUSEA:0.2,
                   Clinic.VOMITING:0.2,Clinic.FAVER:0.2,ECHO.GALLBLADDER_WALL_THICKENING:0.8,
                   ECHO.PERICHOLECYSTIC_FLUID:0.7}


CHOLANGITIS   = {Clinic.RIGHT_UPPER_QUADRANT_PAIN:0.7,Clinic.JAUNDIC:0.7,
                  Clinic.FAVER:0.7,LABS.BILIRUBIN:0.6,LABS.WHITE_BLOOD_CELLS:0.5}


IBS     = {Clinic.ABDOMINAL_PAIN_WORSE_BY_FOOD:0.7,Clinic.ABDOMINAL_PAIN_WORSE_BY_STRESS:0.7,Clinic.ABDOMINAL_PAIN:0.2,
           Clinic.ABDOMINAL_FLATULENCE:0.5,Clinic.CONSTIPATION:0.2,Clinic.dIARRHEA:0.2}                          
