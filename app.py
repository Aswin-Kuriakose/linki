import matplotlib.pyplot as plt
from dates import getDates
from values import getValues

dates, sorted_files = getDates()
values = getValues()
# print(values[0])
# '''
fig, ax0 = plt.subplots()

cmap = 'tab20c'
fig.tight_layout()
# cmap = 'summer'
for i in range(len(values)):
    plt.pcolor(values[i], cmap=cmap)
    # plt.pcolor(data, cmap=cmap)

    plt.title('Pcolor Graph')
    # plt.colorbar() 
    plt.show()
    # plt.savefig(f"{dates[i]}")


# '''