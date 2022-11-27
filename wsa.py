from tkinter import *
from os import popen
import threading
import psutil 
 
def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid


class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        while True:
        	if isinstance(checkprocess("vmmemWSA"),int):
        		print("wsa运行中")
        	else:
        		print("wsa停止运行")

def uninstall_apk():
	dialog = Tk()
	dialog.geometry("400x80")
	Label(dialog,text="输入要卸载的软件包名:").place(x="10",y="0")
	package = Entry(dialog,width=31)
	package.place(x="10",y="30")
	Button(dialog,text="确定",command=lambda:popen("wsaclient /uninstall "+package.get())).place(x="300",y="28")
	dialog.mainloop()

def open_apk():
	dialog = Tk()
	dialog.geometry("400x80")
	Label(dialog,text="输入要打开的软件包名:").place(x="10",y="0")
	package = Entry(dialog,width=31)
	package.place(x="10",y="30")
	Button(dialog,text="确定",command=lambda:popen("start wsa://"+package.get())).place(x="300",y="28")
	dialog.mainloop()

window = Tk()
window.geometry("300x500+10+10")
Button(window,text="打开WSA",command=lambda:popen("wsaclient")).place(x="10",y="10")
Button(window,text="关闭WSA",command=lambda:popen("wsaclient /shutdown")).place(x="10",y="50")
Button(window,text="重启WSA",command=lambda:popen("wsaclient /restart")).place(x="10",y="90")
Button(window,text="打开开发者选项",command=lambda:popen("start wsa-client://developer-settings")).place(x="10",y="130")
Button(window,text="卸载应用",command=lambda:uninstall_apk()).place(x="10",y="170")
Button(window,text="打开应用",command=lambda:open_apk()).place(x="10",y="210")
# thread1 = myThread(1, "WSA_Checker",)
# thread1.start()
window.mainloop()