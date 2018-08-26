#从本地添加远程库

	GitHub把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

		$ git remote add origin git@github.com:China-Waukee/Cloud.git
		$ git remote add origin https://github.com/China-Waukee/Cloud.git

	把本地库的所有内容推送到远程库上

		$ git push -u origin master
		把本地库的内容推送到远程，用git push命令，实际上是把当前分支master推送到远程。
		由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令

#从远程库克隆到本地

	登陆GitHub，创建一个新的仓库
	我们勾选Initialize this repository with a README，这样GitHub会自动为我们创建一个README.md文件。创建完毕后，可以看到README.md文件

	用命令git clone克隆一个本地库
	
		$ git clone git@github.com:michaelliao/gitskills.git
		$ git clone https://github.com/China-Waukee/Cloud.git


