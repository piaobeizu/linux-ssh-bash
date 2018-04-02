# coding: utf-8


import os
import sys
import traceback
import pexpect
import settings

try:
    import pexpect
except ImportError:
    print("""
    You must install pexpect module
    """)
    os.system("pip3 install pexpect")
    sys.exit(1)

SHOW_SERVER = settings.SHOW_SERVER
SERVER = settings.SERVER


def auto_connect(host):
    SSH = "ssh -p %s %s@%s " % (host[0], host[1], host[2])
    try:
        child = pexpect.spawn(SSH)
        index = child.expect(['password:', 'continue connecting (yes/no)?', pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            child.sendline(host[3])
            child.interact()
        elif index == 1:
            child.sendline('yes')
            child.expect(['password:'])
            child.sendline(host[3])
            child.interact()
        elif index == 2:
            print("子程序异常，退出!")
            child.close()
        elif index == 3:
            print("连接超时")
    except:
        traceback.print_exc()


show = "其从如下的连接中选择一个：\n\n"
i = 1
tmp = [""] * 1000

for sel in SHOW_SERVER:
    show = show + sel + "\n"
    for server in SHOW_SERVER[sel]:
        if server != "" and server != None:
            show = show + "    |--" + "[" + str(i) + "] " + server + "\n"
            tmp[i - 1] = server
            i += 1
print(show)
iinput = "steven"
while iinput.isdigit() is not True:
    if iinput != "steven":
        print("\n输入有误，请输入正确的编号数字!\n")
    iinput = input("请输入连接编号：")

select = int(iinput)

try:
    host = SERVER[tmp[select - 1]]
except:
    print("""
    argv error, use it link
    jssh v3, v3 must defined in addr_map
    """)
    sys.exit(1)
auto_connect(host)
