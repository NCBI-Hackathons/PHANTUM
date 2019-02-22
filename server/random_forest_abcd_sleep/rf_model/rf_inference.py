import sklearn
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

# For parsing json input
# https://stackoverflow.com/questions/21104592/json-to-pandas-dataframe
#import json
#from pandas.io.json import json_normalize

# x is a vector of length 17
# [car_accident, sig_accident, witness_fire, witness_natural_disaster, witness_terrorism, witness_warzone, witness_attack, nonfam_attack, fam_attack, beaten_and_bruised, non_fam_death_threat, fam_death_threat, witness_fighting_in_home, fam_adult_sexual_assult, nonfam_adult_sexual_assult, peer_sexual_assult, sudden_death]

'''
car_accident               = A car accident in which your child or another person in the car was hurt bad enough to require medical attention
sig_accident               = Another significant accident for which your child needed specialized and intensive medical treatment
witness_fire               = Witnessed or caught in a fire that caused significant property damage or personal injury
witness_natural_disaster   = Witnessed or caught in a natural disaster that caused significant property damage or personal injury
witness_terrorism          = Witnessed or present during an act of terrorism (e.g., Boston marathon bombing)
witness_warzone            = Witnessed death or mass destruction in a war zone
witness_attack             = Witnessed someone shot or stabbed in the community
nonfam_attack              = Shot, stabbed, or beaten brutally by a non-family member
fam_attack                 = Shot, stabbed, or beaten brutally by a grown up in the home
beaten_and_bruised         = Beaten to the point of having bruises by a grown up in the home	
non_fam_death_threat       = A non-family member threatened to kill your child
fam_death_threat           = A family member threatened to kill your child
witness_fighting_in_home   = Witness the grownups in the home push, shove or hit one another
fam_adult_sexual_assult    = A grown up in the home touched your child in his or her privates, had your child touch their privates, or did other sexual things to your child
nonfam_adult_sexual_assult = An adult outside your family touched your child in his or her privates, had your child touch their privates or did other sexual things to your child
peer_sexual_assult         = A peer forced your child to do something sexually
sudden_death               = Learned about the sudden unexpected death of a loved one
'''
def inference(x):
        
    model = joblib.load('rf_model/sleep_problems_rf.model')
    y_hat = model.predict(x)
    #print('in rf_inference.inference - y_hat: ', y_hat)
    return y_hat[0]

def zero_test():
    return inference([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
'''
# Sample Code
vec = np.zeros(17)

infvec = [vec]

print(inference([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]]))
print(inference(infvec))
'''
