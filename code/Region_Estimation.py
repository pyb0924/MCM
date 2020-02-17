import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
W = np.array([
    [10, 3, 2, 5, 0, 0, 0],
    [0, 0, 0, 0, 10, 0, 0],
    [5, -1, 0, 0, 0, 3, 0],
    [5, 0, 0, 0, 0, 0, 3]
])  # the matrix W

# Read from excel file
df = pd.read_excel("data/data for AHP.xlsx",
                   sheet_name="Input", index_col="Region")
data = df.values

# get result
result = pd.DataFrame((W @ data.T).T, index=df.index,
                      columns=["Y", "Y_Import", "r_c", "r_p"])

# write result to excel file
nan_excel = pd.DataFrame()
nan_excel.to_excel("result\Region_Estimaiton_Result.xlsx")
writer = pd.ExcelWriter("result\Region_Estimaiton_Result.xlsx")
result.to_excel(writer, sheet_name="pre")
result = result.apply(lambda x: ((x-np.mean(x))/np.std(x))) # standardize output
result.to_excel(writer, sheet_name="standard")
writer.save()

# draw
result = result.T
index = np.arange(4)
error_config = {'ecolor': '0.3'}
bar_width = 0.25
fig, ax = plt.subplots()

rect0 = ax.bar(index - bar_width, result["China"], bar_width, 
                color='#FFFF99', label="China")
rect1 = ax.bar(index, result["EU"], bar_width, color='#FFCC99', label="EU")
rect2 = ax.bar(index + bar_width, result["India"], bar_width,  
                color='#FF9999',label="India")
# add axis
ax.hlines(0, -0.5, 4, colors='k', linestyles="dashed")
# add xticks
for i in range(4):
    if i==0:
        plt.text(i - 0.07, -0.15, result.index[i])
    elif i==1:
        plt.text(i - 0.3, -0.15, result.index[i])
    else:
        plt.text(i - 0.1, -0.15, result.index[i])
ax.set_xticks([])

ax.legend(loc="best")
plt.savefig("figure\Region_Estimation.png", dpi=900)
plt.show()
