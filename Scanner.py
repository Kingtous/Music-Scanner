#图形界面
import tkinter
import tkinter.font
import tkinter.filedialog
import text

def getPath1():
    global path1
    text.rootdir=tkinter.filedialog.askdirectory()
    path1.set(text.rootdir)

def getPath2():
    global path2
    text.output=tkinter.filedialog.asksaveasfilename(initialfile= '输出.txt',defaultextension = '.txt')
    path2.set(text.output)

#font=tkinter.font.Font(family='微软雅黑',size=20,weight=tkinter.font.BOLD)

root=tkinter.Tk()
root.title('Music Scanner V2.0---Kingtous')
root['height']=400
root['width']=600

path1=tkinter.StringVar()
path1.set('')
path2=tkinter.StringVar()
path2.set('')

labelname=tkinter.Label(root,text='扫描的目录',justify=tkinter.RIGHT,width=80,font=('微软雅黑',12))
labelname.place(x=30,y=60,width=100,height=30)

textarea=tkinter.Entry(root,width=80,textvariable=path1,font=('微软雅黑',15))
textarea.place(x=130,y=60,width=360,height=30)

buttonscan=tkinter.Button(root,text='浏览',command=getPath1)
buttonscan.place(x=510,y=60,width=50,height=30)


labelname=tkinter.Label(root,text='输出文件',justify=tkinter.RIGHT,width=80,font=('微软雅黑',12))
labelname.place(x=30,y=130,width=100,height=30)

textarea=tkinter.Entry(root,width=80,textvariable=path2,font=('微软雅黑',15))
textarea.place(x=130,y=130,width=360,height=30)

buttonscan=tkinter.Button(root,text='浏览',command=getPath2)
buttonscan.place(x=510,y=130,width=50,height=30)


buttonstart=tkinter.Button(root,text='开始扫描',command=text.main,font=('微软雅黑',13))
buttonstart.place(x=250,y=250,width=100,height=50)


menubar=tkinter.Menu(root)

submenu1=tkinter.Menu(menubar,tearoff=0)
submenu1.add_command(label='关于程序',command=text.about)
submenu1.add_command(label='QQ:1147079871')
submenu1.add_separator()
submenu1.add_command(label='退出',command=root.quit)


submenu2=tkinter.Menu(menubar,tearoff=0)
submenu2.add_command(label='使用说明',command=text.help)

menubar.add_cascade(label='文件',menu=submenu1)
menubar.add_cascade(label='帮助',menu=submenu2)


root.config(menu=menubar)
root.mainloop()
