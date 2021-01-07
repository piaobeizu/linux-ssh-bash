# linux-ssh-bash
linux和mac环境的ssh连接工具

# 使用实例：
1. git clone 
2. sudo ln -s /path/to/lssh.sh /usr/local/bin/lssh
3. sudo chmod +x /usr/local/bin/lssh
4. 将服务器信息配置到settings.py中，其中：
> SHOW_SERVER={"分组名":["显示名称1",...],...}

> SERVER={"显示名称1":[“端口”,"用户名","ip","密码"],...}
5. 执行lssh，选择对应的编号就可以登陆上指定的服务器了

# FAQ
- Q：环境

  本项目需要python3的环境支持

- Q：第一次使用报错

  本项目需要python环境安装 pexpect 模块，请自行百度怎么安装 pexpect 模块
