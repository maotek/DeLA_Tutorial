# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    import numpy as np
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.set_title('click on points')

    line, = ax.plot(np.random.rand(100), 'o', pickradius=5)  # 5 points tolerance


    def onpick(event):
        thisline = event.artist
        xdata = thisline.get_xdata()
        ydata = thisline.get_ydata()
        ind = event.ind
        points = tuple(zip(xdata[ind], ydata[ind]))
        print('onpick points:', points)


    fig.canvas.mpl_connect('pick_event', onpick)

    plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
