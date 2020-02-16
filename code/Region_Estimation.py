import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
W = np.array([
    [10, 2, 5, 0, 0],
    [0, 0, 5, 0, 0],
    [5, 0, 0, 3, 0],
    [5, 0, 0, 0, 3]
])

df = pd.read_excel("data/Region_Estimation.xlsx",
                   sheet_name="standard", index_col="Region")
data = df.values


result = pd.DataFrame((W @ data.T).T, index=df.index,
                      columns=["Y", "Y_In", "r_c", "r_p"])
# print(result)
nan_excel = pd.DataFrame()
nan_excel.to_excel("result\Region_Estimaiton_Result.xlsx")
writer = pd.ExcelWriter("result\Region_Estimaiton_Result.xlsx")
result.to_excel(writer, sheet_name="pre")

result = result.apply(lambda x: ((x-np.mean(x))/np.std(x)))
# print(result)
result.to_excel(writer, sheet_name="standard")
writer.save()


index = np.arange(3)
error_config = {'ecolor': '0.3'}
bar_width = 0.2
fig, ax = plt.subplots()
rect0 = ax.bar(index - 2 * bar_width, result["Y"], bar_width, alpha=0.5,
               color='r', yerr=0.1 * result["Y"].std(), error_kw=error_config, label="Y")

rect1 = ax.bar(index - bar_width, result["Y_In"], bar_width, alpha=0.5, color='y',
               yerr=0.1 * result["Y_In"].std(), error_kw=error_config, label="Y_In")

rect2 = ax.bar(index, result["r_c"], bar_width, alpha=0.5, color='b',
               yerr=0.1 * result["r_c"].std(), error_kw=error_config, label="r_c")

rect3 = ax.bar(index + bar_width, result["r_p"], bar_width, alpha=0.5, color='g',
               yerr=0.1 * result["r_p"].std(), error_kw=error_config, label="r_p")

ax.hlines(0, -0.5, 2.5, colors='k', linestyles="dashed")
ax.set_xticks(index)
ax.set_xticklabels(tuple(result.index))
ax.legend(loc="best")
plt.savefig("figure\Region_Estimation.png", dpi=900)
plt.show()
