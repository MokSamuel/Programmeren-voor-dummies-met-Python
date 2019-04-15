def linplot(filepath, xlabel = str, ylabel = str, col1 = 0, col2 = 1, col3 = 2):
    import matplotlib.pyplot as plt
    name = importasarray(filepath)
    (slope, intercept, r_value, p_value, std_err) = linregression(name, col1, col2, col3)
    (samp, conc_samp, np_sample) = sampledata(name, col1, col2, col3)
    x = name[:,col1]
    y = name[:,col2]
# maak een plotje
    plt.scatter(x, y, label="original data")
    plt.scatter(samp, conc_samp, label="samples")
    plt.plot(x, intercept + slope*x, "r", label="fitted line")

# pas je labels aan
    plt.xlabel(str(xlabel))
    plt.ylabel(str(ylabel))
    plt.legend()
    return(plt.show())

# to clear plot: plt.clf()

#importeer excel als een array
def importasarray(filepath):
    import pandas as pd
    import numpy as np
    pd_data = pd.read_excel(filepath)
# windows heeft als standaard \ python gebruikt /
# van dataframe naar array
    name = np.array(pd_data)
    return name
    
def linregression(name, col1 = 0, col2 = 1, col3 = 2):
    import scipy.stats as st
    #andere optie: "from scipy import stats as st"
    x = name[:,col1]
    y = name[:,col2]
    # gebruik st.linregress voor de waarden van: slope of regression line, intercept of regression line, correlation coefficient, two sided p-value, standard error of estimated gradient
    slope, intercept, r_value, p_value, std_err = st.linregress(x,y)
# andere optie: slope, intercept, r_value, p_value, std_err = st.linregress(np_data[:,0], np_data[:,1])
    return (slope, intercept, r_value, p_value, std_err)

def sampledata(name, col1 = 0, col2 = 1, col3 = 2):
    import numpy as np
    samp = name[:, col3][~np.isnan(name[:,col3])]
    (slope, intercept, r_value, p_value, std_err) = linregression(name, col1, col2, col3)
# bepaal concentratie
    conc_samp = intercept + slope * samp
    np_sample = np.array([samp, conc_samp])
    return (samp, conc_samp, np_sample)