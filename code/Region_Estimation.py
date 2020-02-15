import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
W = np.array([
    [15, 10, 3, 5, 0, 0],
    [-3, 10, 0, 0, 5, 0],
    [0, 10, 0, 0, 0, 5]
])

df = pd.read_excel("data/Region_Estimation.xlsx", sheet_name="Sheet1", index_col="Region")
print(df)

data = df.values

result = pd.DataFrame((W @ data.T).T,index=df.index,columns=["W","r_c","r_p"])
print(result)
result.plot.bar()
plt.xticks(rotation=45)
plt.savefig("Region_Estimation.png")
plt.show()
