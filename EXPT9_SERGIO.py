    #EXPT 9 _ SERGIO _ 2ECE-A 
    import pandas as pd
    
    BearMath = {'Student':['Ice Bear','Panda','Grizzly'], 'Math': [80,95,79]}
    BearElec = {'Student':['Ice Bear','Panda','Grizzly'], 'Electronics': [85,81,83]}
    BearGEAS = {'Student':['Ice Bear','Panda','Grizzly'], 'GEAS': [90,79,93]}
    BearESAT = {'Student':['Ice Bear','Panda','Grizzly'], 'ESAT': [93,89,88]}
    
    bmath = pd.DataFrame(BearMath, columns = ['Student','Math'])
    belec = pd.DataFrame(BearElec, columns = ['Student','Electronics'])
    bgeas = pd.DataFrame(BearGEAS, columns = ['Student','GEAS'])
    besat = pd.DataFrame(BearESAT, columns = ['Student','ESAT'])
    
    merged = pd.merge(bmath,belec,how='right',on='Student')
    merged2 = pd.merge(merged,bgeas,how = 'right', on= 'Student')
    mergedfinal = pd.merge(merged2,besat,how = 'right', on = 'Student')