import scipy.stats as stats

#original 
white =[2.4108112169587477 , 1.0332649527617301, 1.2587217805870778, 1.5970868138316188, 0.7375113441022294, 0.7167032181515116,
1.2573547238357505, 0.6156485882746138, 0.6763327040013676]

blue = [1.5656890040503824, 1.1664267407604718, 1.4296725293521368, 2.214172873484972, 0.6982771702585945, 0.7327395265068629,
        1.4650312719386158, 0.6039218917794515, 0.7652000912088601]
#white =[0.4108112169587477 , 1.0332649527617301, 1.2587217805870778, 0.5970868138316188, 0.7375113441022294, 0.7167032181515116,
#1.2573547238357505, 0.6156485882746138, 0.6763327040013676]

#blue = [2.5656890040503824, 1.1664267407604718, 1.4296725293521368, 2.214172873484972, 0.6982771702585945, 0.7327395265068629,
#      1.4650312719386158, 0.6039218917794515, 0.7652000912088601]

print(stats.ttest_rel(white,blue))