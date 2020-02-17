import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
W = np.array([
    [10, 3, 2, 5, 0, 0, 0],
    [0, 0, 0, 0, 10, 0, 0],
    [5, -1, 0, 0, 0, 3, 0],
    [5, 0, 0, 0, 0, 0, 3]
])  # 收入 人口 替代, P_Y,P_i,P_c,P_p


df = pd.read_excel("data/data for AHP.xlsx",
                   sheet_name="Input", index_col="Region")
data = df.values

result = pd.DataFrame((W @ data.T).T, index=df.index,
                      columns=["Y", "Y_Import", "r_c", "r_p"])


nan_excel = pd.DataFrame()
nan_excel.to_excel("result\Region_Estimaiton_Result.xlsx")
writer = pd.ExcelWriter("result\Region_Estimaiton_Result.xlsx")
result.to_excel(writer, sheet_name="pre")
result = result.apply(lambda x: ((x-np.mean(x))/np.std(x)))
# print(result)
result.to_excel(writer, sheet_name="standard")
writer.save()
result = result.T
print(result)


index = np.arange(4)
error_config = {'ecolor': '0.3'}
bar_width = 0.25
fig, ax = plt.subplots()

rect0 = ax.bar(index - bar_width, result["China"], bar_width, alpha=0.5,
               color='r', label="China")

rect1 = ax.bar(index, result["EU"], bar_width,
               alpha=0.5, color='y', label="EU")

rect2 = ax.bar(index + bar_width, result["India"], bar_width, alpha=0.5, color='b',
               label="India")

# rect3 = ax.bar(index + bar_width, result["r_p"], bar_width, alpha=0.5, color='g',
#           yerr=0.1 * result["r_p"].std(), error_kw=error_config, label="r_p")

ax.hlines(0, -0.5, 4, colors='k', linestyles="dashed")

for i in range(4):
    if i>=2:
        plt.text(i - 0.1, -0.15, result.index[i])
    elif i==1:
        plt.text(i - 0.3, -0.15, result.index[i])
    else:
        plt.text(i - 0.07, -0.15, result.index[i])

ax.legend(loc="best")
ax.set_xticks([])
plt.savefig("figure\Region_Estimation.png", dpi=900)
plt.show()
