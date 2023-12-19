import concurrent
import random
import time
from tkinter import *
from tkinter import ttk

from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

def autorization():
    link = list(link_var.get())
    login = login_var.get()
    password = password_var.get()

    link.insert(8, login + ':' + password + '@')
    link = ''.join(map(str, link))
    driver.get(link)

driver = webdriver.Chrome()
driver.set_window_size(1500, 1000)

width = driver.execute_script("return window.innerWidth")
height = driver.execute_script("return window.innerHeight")

action = ActionChains(driver)

stop_flag = False

def click():
    global stop_flag
    while not stop_flag:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        action.move_by_offset(x, y).click().perform()
        action.move_by_offset(-x, -y).perform()

def spacebar_pressing():
    global stop_flag
    while not stop_flag:
        timer = random.randint(0, 3)
        action.send_keys(Keys.SPACE).perform()
        time.sleep(timer)

def esc_pressing():
    global stop_flag
    while not stop_flag:
        action.send_keys(Keys.ESCAPE).perform()
        time.sleep(30)

def arrow_up_pressing():
    global stop_flag
    while not stop_flag:
        timer = random.randint(0, 10)
        action.send_keys(Keys.ARROW_UP).perform()
        time.sleep(timer)

def arrow_down_pressing():
    global stop_flag
    while not stop_flag:
        timer = random.randint(0, 10)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(timer)

functions = [click, spacebar_pressing, esc_pressing, arrow_up_pressing, arrow_down_pressing]

pool_executor = None

def pool():
    global pool_executor
    global stop_flag
    stop_flag = False
    pool_executor = concurrent.futures.ThreadPoolExecutor(max_workers=len(functions))

    for func in functions:
        pool_executor.submit(func)

def stop_pool():
    global stop_flag
    stop_flag = True

root = Tk()
root.title("Monkey test")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Enter the data").grid(column=2, columnspan=1, row=0, sticky=(W, E))

ttk.Label(mainframe, text="Game link").grid(column=1, columnspan=1, row=1, sticky=(W, E))

link_var = StringVar()
link_entry = ttk.Entry(mainframe, width=7, textvariable=link_var)
link_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, text="Login").grid(column=1, columnspan=1, row=2, sticky=(W, E))

login_var = StringVar()
login_entry = ttk.Entry(mainframe, width=7, textvariable=login_var)
login_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, text="Password").grid(column=1, columnspan=1, row=3, sticky=(W, E))

password_var = StringVar()
password_entry = ttk.Entry(mainframe, width=7, textvariable=password_var)
password_entry.grid(column=2, row=3, sticky=(W, E))

ttk.Button(mainframe, text="Autorization", command=autorization).grid(column=2, row=4, sticky=(W, E))
ttk.Button(mainframe, text="Go", command=pool).grid(column=2, row=5, sticky=(W, E))
ttk.Button(mainframe, text="Stop", command=stop_pool).grid(column=2, row=6, sticky=(W, E))

root.mainloop()