****************************************************************************

#把目录变成Git可以管理的仓库：
$ git init 

#仓库指定用户名和Email地址
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

#把文件添加到仓库(提交的所有修改放到暂存区（Stage）)：
$ git add file1.txt file2.txt file3.txt ...
$ git add -A  提交所有变化
$ git add -u  提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
$ git add .  提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件

#把暂存区的所有修改提交到分支
$ git commit -m "wrote a readme file"

#显示从最近到最远的提交日志，可以加上--pretty=oneline参数
$ git log --pretty=oneline

#查看你的每一次命令记录：
$ git reflog

#查看状态：
$ git status

#回退版本
上一个版本:HEAD^，上上一个版本:HEAD^^，上100个版本:HEAD~100。
$ git reset --hard HEAD^ 
$ git reset --hard commit_id

#查看工作区和版本库里面最新版本的区别：
$ git diff HEAD -- readme.txt

#丢弃工作区的修改
$ git checkout -- readme.txt

#把暂存区的修改撤销掉（unstage），重新放回工作区
$ git reset HEAD readme.txt

#从版本库中删除该文件
$ git rm test.txt
$ git commit -m "remove test.txt"

****************************************************************************

#从本地添加远程库

	GitHub把一个已有的本地仓库与之关联，然后，把本地仓库的内容推送到GitHub仓库。

		$ git remote add origin git@github.com:China-Waukee/库.git
		$ git remote add origin https://github.com/China-Waukee/库.git

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














