#操作方法
import os
import re
import tkinter.messagebox
import subprocess

rootdir = ''
output = ''
rule = r'(.+)\.+(mp3|ape|flac|wav|m4a|wma|cda|ra|ogg|aac|mid|midi|vqf|aiff)$'
count = 0
error = 0


def fw(rootdir, file):
    global count, rule, judge, error
    try:
        list = os.listdir(rootdir)  # 包含文件和文件夹
    except:
        error = error + 1
        file.write('=' * 100 + '\n' + '无法访问，请确认是否有该目录的访问权限：' + rootdir + '\n')
        return
    dirlist = []
    judge = False
    for i in range(0, len(list)):
        if rootdir[-1]!='/':
            rootdir=rootdir+'/'
        path = os.path.join(rootdir + list[i])
        if os.path.isfile(path):  # 是文件
            m = re.match(rule, path, re.IGNORECASE)
            if not m:
                continue
            else:
                if judge == False:  # 第一次输出这个文件夹下的文件，加入文件夹目录
                    judge = True
                    file.write('=' * 100 + '\n' + '当前目录：' + rootdir + '\n')
                file.write(list[i] + '\n')
                count = count + 1
        if os.path.isdir(path):
            dirlist.append(rootdir + list[i] + '/')
    for i in range(0, len(dirlist)):
        fw(dirlist[i], file)


def main():
    file = open(output, 'w+', encoding='utf-8')
    if rootdir == '' or output == '' or not os.path.isdir(rootdir) or not os.path.isfile(output):
        tkinter.messagebox.showerror('扫描', '选择的文件夹或文件无效，请重新输入！')
        return
    tkinter.messagebox.showinfo(title='正在扫描', message='扫描时间和文件数量成正比。\n扫描完成前，程序会进入无响应阶段，不是死机，请耐心等待...')

    fw(rootdir, file)
    file.close()
    tkinter.messagebox.showinfo(title='扫描歌曲', message='共查找到' + str(count) + '首歌曲，已写入，' + output)
    if error != 0:
        tkinter.messagebox.showerror(title='扫描歌曲', message='其中有' + str(error) + '个文件夹无法访问，请确认是否有足够权限进入这些文件夹！')
    #print(output)
    subprocess.Popen(['notepad',output])


def about():
    tkinter.messagebox.showinfo(title='关于', message='作者：Kingtous，版权所有')


def help():
    tkinter.messagebox.showinfo('使用说明',
                                '本程序可以扫描指定目录下所有的音频媒体，并用记事本显示\n支持扫描的类型：mp3 | ape | flac | wav | m4a | wma | cda | ra | ogg | aac | mid | midi | vqf | aiff\n浏览要扫描的位置以及输出文件，点击“开始扫描”即可')
