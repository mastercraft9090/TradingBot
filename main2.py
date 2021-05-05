import tkinter as tk
import logging
from BinanceFutures import get_contracts

logger = logging.getLogger()
logger.debug("This message is only important when debugging the program")
logger.info("This just shows basic info")
# logger.warning("This message is about something you should pay attention to")
# logger.error("This message helps debug an error that occurred in your program")

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s ')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)



   #if __name__ == '__main2__':
binance_contracts = get_contracts()
root = tk.Tk()
root.configure(bg='gray12')
i = 0
j = 0

calibri_font = ("calibri", 11, "normal")
for contract in binance_contracts:
    #label_widget = tk.Label(root, text=contract, borderwidth=1, relief=tk.SOLID, width=13)
    label_widget = tk.Label(root, text=contract, bg='gray12', fg='SteelBlue1', width=13)
   # grid() pack()
    #label_widget.pack(side=tk.LEFT)
    label_widget.grid(row=i, column=j, sticky='we')

    if i == 10:
        j += 1
        i = 0
    else:
       i += 1
root.mainloop()
