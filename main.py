# coding: utf-8


import sys, getopt, os, traceback
import traceback
import settings
# import gui


def link():
    try:
        import pexpect
    except ImportError:
        print("""
        You must install pexpect module
        """)
        os.system("pip3 install pexpect")
        sys.exit(1)

    RED_COLOR = '\033[1;31m'  # 红
    GREEN_COLOR = '\033[1;32m'  # 绿
    YELOW_COLOR = '\033[1;33m'  # 黄
    BLUE_COLOR = '\033[1;34m'  # 蓝
    PINK = '\033[1;35m'  # 粉红
    RES = '\033[0m'

    SHOW_SERVER = settings.SHOW_SERVER
    SERVER = settings.SERVER

    def auto_connect(host):
        SSH = "ssh -p %s %s@%s "% (host[0], host[1], host[2])
        if len(host)==4:
            print("采用ssh-copy-id方式连接")
            SSH = "ssh -p %s %s@%s " % (host[0], host[1], host[2])
            child = pexpect.spawn(SSH, echo=False)
        elif os.path.exists(host[4]):
            print("采用密钥文件方式连接")
            SSH = "ssh -p %s %s@%s -i %s " % (host[0], host[1], host[2], host[4])
            child = pexpect.spawn(SSH, echo=False)
            # index = child.expect(['continue connecting (yes/no)?', pexpect.EOF, pexpect.TIMEOUT])
            # if index == 0:
            #     child.sendline('yes')
            #     child.interact()
            # else:
            #     child.interact()
        else:
            print("采用密码方式连接")
            try:
                child = pexpect.spawn(SSH, echo=False)
                index = child.expect(['password:', 'continue connecting (yes/no)?', pexpect.EOF, pexpect.TIMEOUT])
                if index == 0:
                    child.sendline(host[4])
                    child.interact()
                elif index == 1:
                    child.sendline('yes')
                    child.expect(['password:'])
                    child.sendline(host[4])
                elif index == 2:
                    print("子程序异常，退出!")
                    child.close()
                elif index == 3:
                    print("连接超时")
                    child.close()
            except:
                traceback.print_exc()
                child.close()
        if host[3]:
            child.sendline("resize -cu >/dev/null 2>&1")
        child.interact()

    show = "其从如下的连接中选择一个：\n"
    i = 1
    tmp = [""] * 100

    for sel in SHOW_SERVER:
        show = show + "\n" + sel + "\n"
        for server in SHOW_SERVER[sel]:
            if server != "" and server != None:
                show = show + "    |--" + "[" + str(i) + "] " + RED_COLOR + " " + server + " " + RES + "\n"
                tmp[i - 1] = server
                i += 1
    # selectFrame = gui.SelectFrame(SHOW_SERVER)
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


def search(id):
    i = 1
    tmp = [""] * 100
    SHOW_SERVER = settings.SHOW_SERVER
    SERVER = settings.SERVER
    for sel in SHOW_SERVER:
        for server in SHOW_SERVER[sel]:
            if server != "" and server != None:
                tmp[i - 1] = server
                i += 1
    print(SERVER[tmp[id]])


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "l:s:", ["linkId"])
    except getopt.GetoptError:
        sys.exit(2)
    if len(opts) == 0:
        link()
    else:
        for opt, arg in opts:
            if opt == '-s':
                search(int(arg) - 1)


if __name__ == "__main__":
    main(sys.argv[1:])
