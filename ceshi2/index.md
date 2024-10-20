---
layout: custom
title: Git总结
showMiniToc: true
---

## 总结

```javascript
git init
```

```
git add .
```

```
git commit -m "提交说明"
```

```
git remote rm origin
git remote add origin git@gitee.com:mroph/novel.git
```

```
git pull --rebase origin master
git push -u origin master
```

## 详细步骤

### 初始化

#### 定位工作目录

打开 Git Bash 终端，使用 `cd`命令加上要切换的路径，例如：`cd /c/Users/username/Documents`；按下回车键，即可切换到指定的路径。需要注意的是路径中需要使用正斜杠 / 分隔路径，而不是反斜杠 \。

使用`pwd`可以显示当前路径

#### 初始化用户信息

```
git config --global user.name 'better'
git config --global user.email '1063266220@qq.com'
```

### 创建本地仓库

创建本地仓库的方法有两种：

- 一种是创建全新的仓库：`git init`，会在当前目录初始化创建仓库，也可指定目录：`git init [文件目录]`执行命令后，如下显示

```
$ git init
Initialized empty Git repository in /Users/michael/learngit/.git/
```

创建完多出了一个被隐藏的.git 目录，这就是本地仓库 Git 的工作场所，而且是一个空的仓库（empty Git repository）。没事千万不要手动修改这个目录里面的文件，不然改乱了，就把 Git 仓库给破坏了。

- 另一种是克隆远程仓库：`git clone [url]`
  克隆远程仓库，如在 github 上创建的仓库“`https://github.com/kwonganding/KWebNote.git`”

```
$ git clone 'https://github.com/kwonganding/KWebNote.git'
Cloning into 'KWebNote'...
remote: Enumerating objects: 108, done.
remote: Counting objects: 100% (108/108), done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 108 (delta 48), reused 88 (delta 34), pack-reused 0
Receiving objects: 100% (108/108), 9.36 KiB | 736.00 KiB/s, done.
Resolving deltas: 100% (48/48), done.
```

会在当前目录下创建“KWebNote”项目目录。

### 暂存区 add

把工作区变化放到暂存区中，执行命令`git add .`可以一次性把所有变化文件放入暂存区

```
$ git add .
```

执行上面的命令，没有任何显示，说明添加成功。也可以先执行`git rm --cached <file>`命令将指定的`file`从当前的暂存区中删除但保留文件在本地工作目录中。
| **指令** | **描述** |
| --- | --- |
| git add \[file1\] \[file2\] | 添加文件到暂存区，包括修改的文件、新增的文件 |
| git add \[dir\] | 同上，添加目录到暂存区，包括子目录 |
| git add . | 同上，添加**所有**修改、新增文件（未跟踪）到暂存区 |
| git rm \[file\] | 删除工作区文件，并且将这次删除放入暂存区 |
|git rm --cached [file]|删除放入暂存区 ，但该文件会保留在工作区|

### 提交 commit-记录

把暂存区内容提交到版本库，命令如下（此处文字说明可以不加引号）

```
git commit -m '提交的内容说明'
```

执行上面的命令，如下显示

```
$ git commit -m "wrote a readme file"
[master (root-commit) eaadf4e] wrote a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 readme.txt
```

`git commit`命令执行成功后会告诉你，`1 file changed`：1 个文件被改动（我们新添加的 readme.txt 文件）；`2 insertions`：插入了两行内容（readme.txt 有两行内容）。
以上命令相当于存档了一次，在版本库中产生一次提交记录并生成版本号。本次存档，不耽误我们在工作区 (项目文件夹) 下继续编写项目

如果改的代码过多，忘记改过哪些了，可以运行`git status`命令来查看 git 仓库变化，只能看未提交的所有变更的文件状态
| **指令** | **描述** |
| --- | --- |
| git commit -m '说明' | 提交变更，参数`-m`设置提交的描述信息，应该正确提交，不带该参数会进入说明编辑模式 |
| git commit -a | 参数`-a`，表示直接从工作区提交到版本库，略过了`git add`步骤，不包括新增的文件 |
| git commit \[file\] | 提交暂存区的指定文件到仓库区 |
| git commit --amend -m | 使用一次新的`commit`，替代上一次提交，会修改`commit`的`hash`值（id） |
| git **reflog** | 查看所有可用的历史版本记录（实际是 HEAD 变更记录），包含被回退的记录（**重要**） |
| git status | 查看本地仓库状态，比较常用的指令，加参数`-s`简洁模式 |

### 将本地代码仓库关联到 gitee 上`git remote add`

- 第一次提交直接执行以下命令关联

```
 git remote add origin 仓库地址
```

此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改；

- 第二次提交先删除，再关联

```
git remote rm origin
git remote add origin 仓库地址
```

否则会在使用命令`git remote add`时报错：`fatal: remote origin already exists.`，说明本地库已经关联了一个名叫`origin`的远程库，

### 将代码由本地仓库上传到 gitee 远程仓库

执行以下命令，先拉取后推送

```
git pull --rebase origin master
git push -u origin master
```

| **远程仓库指令**                    | **描述**                                                           |
| ----------------------------------- | ------------------------------------------------------------------ |
| git clone \[git 地址\]              | 从远程仓库克隆到本地（当前目录）                                   |
| git remote -v                       | 查看所有远程仓库，不带参数`-v`只显示名称                           |
| git remote show \[remote\]          | 显示某个远程仓库的信息                                             |
| **git remote add \[name\] \[url\]** | 增加一个新的远程仓库，并命名                                       |
| git remote rename \[old\] \[new\]   | 修改远程仓库名称                                                   |
| **git pull \[remote\] \[branch\]**  | 取回远程仓库的变化，并与本地版本合并                               |
| **git pull**                        | 同上，针对当前分支                                                 |
| git fetch \[remote\]                | 获取远程仓库的所有变动到本地仓库，不会自动合并！需要手动合并       |
| **git push**                        | 推送当前分支到远程仓库                                             |
| git push \[remote\] \[branch\]      | 推送本地当前分支到远程仓库的指定分支                               |
| git push \[remote\] --force/-f      | 强行推送当前分支到远程仓库，即使有冲突，⚠️ 很危险！                |
| git push \[remote\] --all           | 推送所有分支到远程仓库                                             |
| git push –u                         | 参数`–u`表示与远程分支建立关联，第一次执行的时候用，后面就不需要了 |
| git remote rm \[remote-name\]       | 删除远程仓库                                                       |
| git pull --rebase                   | 使用 rebase 的模式进行合并                                         |

# 错误

## git init 报错

当我们在一个目录下初始化 git 时 可能会出现这个报错，

```javascript
$ git init
warning: templates not found in /home/ja/share/git-core/templates
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
Initialized empty Git repository in /tmp/new/.git/
```

**解决：** 执行`git config --global init.defaultBranch master` 命令，设置默认分支为 master 级别就不会再报错了

```javascript
git config --global init.defaultBranch master
```

## git add .报错

git add .报错 `warning: adding embedded git repository\:xxxxxxxxxx`

执行- \$ git add .命令时出现出现这个报错

```bash
warning: adding embedded git repository:xxxxxxxxxx
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint: git submodule add <url>xxxxxxxxxx
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint: git rm --cached   xxxx
hint:
hint: See "git help submodule" for more information.
```

**原因：** 使用 `git add .` 时，出现上述错误。是因为在当前 `git` 仓库中同时包含有另一个`git`仓库。如当前仓库目录下的子文件夹内又是一个仓库。

**解决：** 删除子文件夹的.git 文件， 重新执行`git add .`

## `git remote add`时报错：

```
git remote add origin git@gitee.com:liaoxuefeng/learngit.git
fatal: remote origin already exists.
```

这说明本地库已经关联了一个名叫`origin`的远程库，可以用`git remote rm <name>`命令已有的远程库。

```
git remote -v
origin	git@github.com:michaelliao/learngit.git (fetch)
origin	git@github.com:michaelliao/learngit.git (push)
```

可以看到，本地库已经关联了`origin`的远程库，并且，该远程库指向 GitHub。我们可以删除已有的 GitHub 远程库再关联 Gitee 的远程库

```
git remote rm origin
git remote add origin 仓库地址
```

## git 上传报错

### 第一个问题

上传步骤：\
`git add .`\
`git commit -m "提示消息"`\
`git push origin master`

出错：\
`! [rejected] master -> master (fetch first) error: failed to push some refs to ' 。。。'`

出现这个问题是因为 github 中的 README.md 文件不在本地代码目录中，可以通过如下命令进行代码合并

`git pull --rebase origin master`

### 第二个问题

`! [remote rejected] master -> master (pre-receive hook declined)`

在推送代码时报错如上，网上搜到的方法说是项目的 setting 中 master 是受保护的项目，所以开发者无法推送，解决方法是修改 protected 的设置，或者新建一个分支，推送到自己的分支上

[解决办法的文章](https://www.cnblogs.com/cppeterpan/p/7289266.html)

## git push 报错

gitee 第一次提交代码提交不上去，到 push 这一步老是遇到

```javascript
  ! \[remote rejected\] master -> master (hook declined)
error: failed to push some refs to
```

这种情况，老是提不上去。那是因为。你的邮箱设置，**不公开我的邮箱**把这个勾上了，取消勾选就行了。这样导致找不到你的远程地址。所以推不上去

