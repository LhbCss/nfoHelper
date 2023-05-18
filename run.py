# -*- coding: utf-8 -*-
import re
import os


"""
KMP 算法获取 next[] 的函数
"""
def Get_next(p,next):
    nums=len(p)
    for m in range(1,nums):
        k = 1
        for i in range(0,m):

            if i+1>=m-i:
                break
            if p[0:i+1]==p[m-i-1:m]:
                k=i+2
        next.append(k)



"""
KMP
"""
def KMP(s,p,next):
    nums1=len(s)
    nums2=len(p)
    i=j=0
    while i!=nums1 and j!=nums2:
        if s[i]!=p[j]:
            j=next[j]
            i+=1
        else :
            i+=1
            j+=1
    if j!=nums2 :
        #匹配失败
        return -1
    else:
        #匹配成功
        return i - nums2 + 1



"""
该函数所修改的文件夹名必须是 【[艺人名]】[番号] 格式的，函数的执行效果是修改 [艺人名] 为新艺人名
"""
def change_dirs_name(dir, name, cnt):
    dirs = os.listdir(dir)
    for dirc in dirs:
        if os.path.isdir(dirc) is True: # 是文件夹
            if dirc.find('【') != -1:
                index = dirc.find('】')
                last = dirc[index:]
                print("发现匹配的文件夹：{}，已成功修改其名称".format(dirc))
                os.rename('.\\' + dirc, '.\\' + '【' + name + last)
                cnt += 1
    print("修改完成，已成功作用于：{} 个文件夹.".format(cnt))



"""
操纵读写指针对 .nfo 描述文件特定标签进行修改，步骤如下：

一、将读写指针定位到 <actor> 标签下的字标签 <name>
二、通过 KMP 算法将模式串向女艺人名字主串匹配，若匹配成功则进入下一步（无差别修改不存在这一步）
三、从读写指针处往后读取直至文件末尾，将文本保存在 rest 变量中
四、读写指针回退到 <name> 标签行的上一行，并删除余下内容
五、写入新的 <name>[name]</name> 行
六、将 rest 中的内容还原至描述文件中

"""
def match_then_insert(filename, match, content, method):
    global cnt
    """匹配后在该行追加
    :param filename: 要操作的文件
    :param match: 匹配内容
    :param content: 追加内容
    """
    before = ''
    after = ''
    if method == '2':
        with open(filename, mode='rb+') as f:
            while True:
                line = f.readline()  # 逐行读取
                if len(line) == 0 : break
                else:
                    line_str = line.decode().splitlines()[0]
                    if re.search(match, line_str) != None:
                        # 匹配成功
                        str = line_str
                        Get_next(str, next)
                        res = KMP(str, old, next)
                        if res == -1:
                            print("对不起，该小姐姐的名字不匹配。")
                        else:
                            flag = 1
                            before = str[:res - 1]
                            after = str[res + len(old) - 1:]
                            rest = f.read()  # 读取余下内容
                            f.seek(-len(rest), 1)  # 光标移动回原位置
                            f.seek(-len(line), 1)  # 光标移动到上一行
                            f.truncate()  # 删除余下内容
                            content = "{}{}{}\n".format(before, new, after)
                            f.write(content.encode())  # 插入指定内容
                            f.write(rest)  # 还原余下内容
                            cnt += 1
                            break
    else:
        with open(filename, mode='rb+') as f:
            while True:
                line = f.readline()  # 逐行读取
                if len(line) == 0 : break
                else:
                    line_str = line.decode().splitlines()[0]
                    if re.search(match, line_str) != None:  # match = <name>
                        # 匹配成功
                        rest = f.read()  # 读取余下内容
                        f.seek(-len(rest), 1)  # 光标移动回原位置
                        f.seek(-len(line), 1)  # 光标移动到上一行
                        f.truncate()  # 删除余下内容
                        content = "    <name>{}</name>\n".format(name)
                        f.write(content.encode())  # 插入指定内容
                        f.write(rest)  # 还原余下内容
                        cnt += 1
                        break



"""
程序入口，主要接收用户选择，并通过 os 循环遍历文件夹调用方法完成批量修改的操作。
"""
if __name__ == '__main__':
    cnt = 0
    choose = input("-------------------\n-                 -\n- Designed by LHB -\n-    2023/1/9     -\n-                 -\n-------------------\n\n请选择你想要进行的操作：\n输入 1 -> 批量修改当前路径下的文件夹名称\n输入 2 -> 扫描当前路径下所有文件夹内的 .nfo 文件并修改骚逼的名字\n输入 3 -> 无差别将当前目录下的所有文件夹内的 .nfo 文件中女艺人的名字更改为特定值（直接回车即为空名字）\n输入 4 -> 无差别将当前目录下的所有文件夹名内女艺人的名称更改为特定值（直接回车即为空名字）\n输入 5 -> 无差别更改当前目录下所有文件夹名的艺人名字与所有文件夹内 .nfo 文件中的女艺人名字\n")
    if choose == '1':
        """
        此选项与 change_dirs_name(dir, name, cnt) 方法需要特定格式的文件夹名不同，是无差别批量修改当前目录下的所有文件夹名。
        分三种情况：匹配字符在文件名开头、中间、末尾，需要分别对新文件夹名做不同的拼接处理。
        """
        path = os.getcwd()
        list = os.listdir(path)
        old = input("请输入需要修改的文件夹所包含的字符：")
        new = input("请输入希望用于替换以上字符的新字符：")
        for elem in list:
            next = [0]
            Get_next(elem, next)
            res = KMP(elem, old, next)
            if res == -1:
                pass
                # 匹配失败
            else:
                print("发现匹配的文件夹：{}，已成功修改其名称".format(elem))
                if res == 1:
                    # 匹配字符在开头的情况
                    after = elem[len(old):]
                    os.rename('.\\' + elem, '.\\' + '{}{}'.format(new, after))
                elif res + len(old) - 1 == len(elem):
                    # 匹配字符在末尾的情况
                    before = elem[:res - 1]
                    os.rename('.\\' + elem, '.\\' + '{}{}'.format(before, new))
                else:
                    # 匹配字符在中间的情况
                    before = elem[:res - 1]
                    after = elem[res + len(old) - 1:]
                    os.rename('.\\' + elem, '.\\' + '{}{}{}'.format(before, new, after))
                cnt += 1
        print("修改完成，已成功作用于：{} 个文件.".format(cnt))


    elif choose == '2':
        old = input("请输入需要修改的女艺人的名字：")
        new = input("请输入这个女艺人所改的名字：")
        next = [0]
        str = ""  # 存放匹配成功的行
        path = os.getcwd()
        files = os.listdir
        flag = 0
        dir = os.getcwd()
        dirs = os.listdir(dir)
        for dirc in dirs:
            if os.path.isdir(dirc) is True:
                # 是文件夹
                dircs = os.listdir(dirc)
                for item in dircs:
                    if item.endswith(".nfo"):
                        # 是 .nfo 文件
                        file_name = "{}\{}\{}".format(dir, dirc, item)
                        print("发现 .nfo 文件：{}！！".format(file_name))
                        match_then_insert(file_name, match="<name>", content=new, method=2)
                        if flag == 1:
                            cnt += 1
            else:
                pass

        print("修改完成，已成功作用于：{} 个文件.".format(cnt))


    elif choose == '3':
        name = input("请输入女艺人们的新名字：")
        dir = os.getcwd()
        dirs = os.listdir(dir)
        flag = 0
        next = [0]
        str = ""  # 存放匹配成功的行
        for dirc in dirs:
            if os.path.isdir(dirc) is True:
                # 是文件夹
                dircs = os.listdir(dirc)
                for elem in dircs:
                    if elem.endswith(".nfo"):
                        file_name = "{}\{}\{}".format(dir, dirc, elem)
                        print("发现 .nfo 文件：{}！！".format(file_name))
                        match_then_insert(file_name, match="<name>", content=name, method=3)
                        if flag == 1:
                            cnt += 1
        print("修改完成，已成功作用于：{} 个 .nfo 文件.".format(cnt))


    elif choose == '4':
        dir = os.getcwd()
        name = input("请输入女艺人们的新名字：")
        change_dirs_name(dir, name, cnt)


    elif choose =='5':
        dir = os.getcwd()
        name = input("请输入女艺人们的新名字：")
        change_dirs_name(dir, name, cnt)
        dirs = os.listdir(dir)
        flag = 0
        next = [0]
        str = ""  # 存放匹配成功的行
        for dirc in dirs:
            if os.path.isdir(dirc) is True:
                # 是文件夹
                dircs = os.listdir(dirc)
                for elem in dircs:
                    if elem.endswith(".nfo"):
                        file_name = "{}\{}\{}".format(dir, dirc, elem)
                        print("发现 .nfo 文件：{}！！".format(file_name))
                        match_then_insert(file_name, match="<name>", content=name, method=3)
                        if flag == 1:
                            cnt += 1
        print("修改完成，已成功作用于：{} 个 .nfo 文件.".format(cnt))
    else:
        print("^^别乱输啊表哥。")

    wait = input("按回车键退出")