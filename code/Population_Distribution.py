import matplotlib.pyplot as plt
plt.figure()
labels = ['High-Income', 'Middle-Income', 'Low-Income']
sizes = [10.88, 44.2, 8.69]
explode = (0.05, 0.05, 0.05)
color = ['#FFFF99', '#FFcc99', '#FF9999']

patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels,
                                  colors=color, autopct='%3.1f%%', labeldistance=1.1,
                                  shadow=False, startangle=90, pctdistance=0.6)

for t in l_text:
    t.set_size(16)
for t in p_text:
    t.set_size(18)

plt.axis('equal')
plt.axis('equal')
plt.savefig("figure\Population_Distribution.png",dpi=900)
plt.show()
