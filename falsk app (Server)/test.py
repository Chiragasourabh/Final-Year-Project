import features_extraction
import sys
import joblib
import numpy as np
import time

def check(url,clf):
    # url=sys.argv[1]
    fT = time.time()
    features_test = features_extraction.main(url)
    feT = time.time()
    features_test = np.array(features_test).reshape((1, -1))
    prT=time.time()
    pred = clf.predict(features_test)
    # pred1 = clf1.predict(features_test)
#     prob=clf.predict_proba(features_test)
    preT=time.time()

#     pred=[1]
    print("\n")
    print("Feature extraction Time = "+str(feT-fT))
    print("Prediction Time = "+str(preT-prT))
    print("Total Time = "+str(preT-fT))
    print("\n")

    if int(pred[0])==1:
        print(url)
        print ("ML Model Predicts This as a safe website.")
        return False
    #     # return str(url)+" is a safe website."
        
    elif int(pred[0])==-1:
        print(url)
        print ("ML Model Predicts This as a phishing website..!")
        return True
        # return str(url)+" is a phishing website..!"

        
