import numpy as np
import matplotlib.pyplot as plt

category_names = ['Well Processed', 'Collected But Not Well Processed','Uncollected']
results = {
    "High-Income": [.99, .01, 0],
    "Middle-Income":[.48, .28, .24],
    "Low-Income":[.14, .2, .66]
}


def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = (plt.get_cmap("summer")(
        np.linspace(0.15, 0.85, data.shape[1])))
    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            if c>0:
                ax.text(x, y, str(int(c*100))+"%", ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax

survey(results, category_names)
plt.savefig("figure\Process_Distribution.png",dpi=900)
plt.show()
