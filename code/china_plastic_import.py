import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame([[735, 259.4], [735, 244], [583, 222], [5, 2.6]], index=[2015,2016,2017,2018], columns=["Waste Plastic Imports", "Amount"])

fig,ax1=plt.subplots()
ax1.bar(df.index, df["Waste Plastic Imports"],alpha=0.5,width=0.5,color='r', label="Waste Plastic Imports")
ax1.set_xlabel("Time(Year)")
ax1.set_ylabel("Waste Plastic Imports (10^6t)")

ax2 = ax1.twinx()
ax2.plot(df.index, df["Amount"], 'o-', label="Amount")
ax2.set_ylabel("Amount (10^9CNY)")
ax2.set_xticks([2015,2016,2017,2018])

ax1.vlines(2017.5, 0, 800, colors='k', linestyles="dashed")
ax1.annotate("2018-01-01\nChinese \nGovernment\nProhibit Waste\nPlastic Import",
            xy=(2017.5,400), xytext=(2017.6,500),arrowprops=dict(arrowstyle='->'))

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
plt.legend(handles1 + handles2, labels1 + labels2, loc="best")
# ax1.set_title("China Waste Plastic Import")
plt.savefig("figure\Chinese_Plastic_Import.png",dpi=900)
plt.show()

