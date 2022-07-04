
from columnar import columnar
from click import style
import os



def draw_result(x,y):
    import matplotlib.pyplot as plt
    plt.plot(x,y)
    plt.plot(x,[0 for i in range(len(x))])
    plt.xlabel("turn")
    plt.ylabel("profit")
    plt.show()


def draw_screen(data,headers):
    # os.system("clear")
    os.system("cls")
    print(columnar(data, headers, justify="c"))
    print("waiting...")
