
from columnar import columnar
# from click import style
import os




def draw_screen(data,headers):
    # os.system("clear")
    os.system("cls")
    print(columnar(data, headers, justify="c"))
    print("waiting...")
