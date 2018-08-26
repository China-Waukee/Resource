
#关于github报错connect to host github.com port 22: Connection timed out的解决

报错内容如下：

	ssh: connect to host github.com port 22: Connection timed out
	fatal: Could not read from remote repository.
	Please make sure you have the correct access rights
	and the repository exists.
	
#分析

	看到这个信息的时候，感觉是不是因为断网或者被墙了导致的连接失败。
	网页登录github，发现一切正常并没有问题。
	注意到了报错信息里的 port 22   
	是端口的原因吗？我照着网上的说法 用443端口连接了一次github，命令如下：
	$ ssh -T -p 443 git@ssh.github.com
	成功
	
#直接有效的解决方案：

	通过修改github连接方式，从之前设置的ssh方法转成https方法（我理解为登录操作）。命令如下：
	$ git config --local -e   //编辑本地git配置
	将
	url = git@github.com:你的用户名/仓库名.git
	改为
	url = https://github.com/你的用户名/仓库名.git
	然后esc   :wq保存修改回车
	终于能正常使用了（虽然开始要输入账号和密码）
	这种方法虽然并没有根本解决ssh连接失败的问题，但能将代码传上去了。
