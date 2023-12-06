# Git的使用

## git指令

- git init  #初始化仓库
- git clone #拷贝一份远程仓库，也就是下载一个项目。
- git add # 添加文件到暂存区
- git status  # 查看仓库当前的状态，显示有变更的文- 件。
- git diff    # 比较文件的不同，即暂存区和工作区的差异。
- git commit  # 提交暂存区到本地仓库。
- git reset   # 回退版本。
- git rm  # 将文件从暂存区和工作区中删除。
- git mv  # 移动或重命名工作区文件。
- git checkout    # 分支切换。
- git switch  # 更清晰地切换分支。
- git restore # 恢复或撤销文件的更改。
- git log # 查看历史提交记录
- git blame file  # 以列表形式查看指定文件的历史修改记录
- [git remote](#git-remote)  # 远程仓库操作
- git fetch   # 从远程获取代码库
- git pull    # 下载远程代码并合并
- git push    # 上传远程代码并合并

## 基础流程

初始化仓库

 ```bash
 git init
 ```

配置账号

```sh
git config --global user.email"710341720@qq.com"
git config --global user.name "laidaJ"
```

添加文件到暂存区

 ```sh
 git add README.md
 ```

暂存区内容添加到仓库

```sh
git commit -m README.md
```

提交

```sh
git push -u orign master
```

## git指令详细介绍

### git init

git init 命令用于在目录中创建新的 Git 仓库。

在目录中执行 `git init` 就可以创建一个 Git 仓库了

现在你可以看到在你的项目中生成了 .git 这个子目录，这就是你的 Git 仓库了，所有有关你的此项目的所有内容和元数据都存放在这里

### git clone

git clone 是一个用于克隆（clone）远程 Git 仓库到本地的命令。

 `git clone [url]`

如果你想要一个不一样的名字， 你可以在该命令后加上你想要的名称

### git add

git add 命令可将该文件的修改添加到暂存区

```sh
# 添加一个或多个文件到暂存区：
git add [file1] [file2] ...
# 添加指定目录到暂存区，包括子目录：
git add [dir]
# 添加当前目录下的所有文件到暂存区：
git add .
```

### git status

`git status` 是一个用于查看 Git 仓库当前状态的命令

git status 命令会显示以下信息：

- 当前分支的名称。
- 当前分支与远程分支的关系（例如，是否是最新的）。
- 未暂存的修改：显示已修改但尚未使用 git add 添加到暂存区的文件列表。
- 未跟踪的文件：显示尚未纳入版本控制的新文件列表。

通常我们使用 -s 参数来获得简短的输出结果 `git status -s`

### git diff

`git diff` 命令比较文件的不同，即比较文件在暂存区和工作区的差异

git diff 有两个主要的应用场景。

- 尚未缓存的改动：git diff
- 查看已缓存的改动： git diff --cached
- 查看已缓存的与未缓存的所有改动：git diff HEAD
- 显示摘要而非整个 diff：git diff --stat

### git commit

git commit 命令将暂存区内容添加到本地仓库中

```sh
# 提交暂存区到本地仓库中:
git commit -m [message]
[message] 可以是一些备注信息。
# 提交暂存区的指定文件到仓库区：
git commit [file1] [file2] ... -m [message]
-a 参数设置修改文件后不需要执行 git add 命令，直接来提交
git commit -a
```

设置提交代码时的用户信息

```sh
开始前我们需要先设置提交的用户信息，包括用户名和邮箱：
git config --global user.name 'runoob'
git config --global user.email test@runoob.com
如果去掉 --global 参数只对当前仓库有效。
```

### git reset

git reset 命令用于回退版本，可以指定退回某一次提交的版本

```sh
git reset [--soft | --mixed | --hard] [HEAD]
# --mixed 为默认，可以不用带该参数，用于重置暂存区的文件与上一次的提交(commit)保持一致，工作区文件内容保持不变。
git reset  [HEAD]
```

### git rm

git rm 命令用于删除文件

```sh
# 将文件从暂存区和工作区中删除：
git rm <file>
如果删除之前修改过并且已经放到暂存区域的话，则必须要用强制删除选项 -f。

如果想把文件从暂存区域移除，但仍然希望保留在当前工作目录中，换句话说，仅是从跟踪清单中删除，使用 --cached 选项即可：
git rm --cached <file>
```

### git mv

git mv 命令用于移动或重命名一个文件、目录或软连接

`git mv [file] [newfile]`

### git checkout

git checkout 命令用于在不同的分支之间切换、恢复文件、创建新分支等操作
>注意：git checkout 命令在 Git 2.23 版本后引入了 git switch 和 git restore 命令，分别用于分支切换和文件恢复，以提供更清晰的语义和错误检查。如果你使用较新的 Git 版本，可以考虑使用这些命令代替 git checkout。

切换分支：

以下命令允许你从当前分支切换到指定的分支

```sh
git checkout <branch-name>
# 例如将你的工作目录切换到主分支:

git checkout -b <new-branch-name>
# 创建一个名为 <new-branch-name> 的新分支并切换到它

git checkout -
# 快速切换回前一个分支，无需记住分支名称
```

### git switch

git switch 命令用于更清晰地切换分支

```sh
# 以下命令允许你从当前分支切换到指定的分支 <branch-name>:
git switch <branch-name>
# 以下命令用于创建一个新分支 <new-branch-name> 并立即切换到新创建的分支:
git switch -c <new-branch-name>
# 以下命令可以让你快速切换回前一个分支，无需记住分支名称:
git switch -
# 以下命令可以让你列出可用的本地分支和标签，以便快速选择要切换的目标：
git branch
```

### git restore

git restore 命令用于恢复或撤销文件的更改

```sh
# 以下命令可以将指定文件 <file> 恢复到最新的提交状态，丢弃所有未提交的更改：
git restore <file>
# 以下命令将还原所有未提交的更改，包括工作目录和暂存区的更改：
git restore .
# 如果你想将文件 <file> 恢复到特定提交 <commit> 的状态，可以使用以下命令：
git restore --source=<commit> <file>
# 以下命令允许你以交互方式选择要还原或保留的更改：
git restore -i
```

### git branch

```sh
git branch  # 查看本地分支
git branch  -r  # 查看远程分支 -r表示remote
git branch -a   # 查看所有分支
git branch -v   # 查看一个分支的最后一次提交
git branch --merged # 查看哪些分支已经合并到当前分支
git branch --no-merged # 查看所有未合并工作的分支

git branch master   # 创建了个叫master的分支
git checkout master #切换到了master这个分支
git checkout -b master  #创建master同时切换到这个分支
```

  ```bash
  git branch -M main
  git remote add origin https://github.com/laidaJ/studycode.git
  git push -u origin master
  ```

### git remote

git remote 命令用于用于管理 Git 仓库中的远程仓库。

```sh
git remote：    # 列出当前仓库中已配置的远程仓库。
git remote -v： # 列出当前仓库中已配置的远程仓库，并显示它们的 URL。
git remote add <remote_name> <remote_url>： #添加一个新的远程仓库。指定一个远程仓库的名称和 URL，将其添加到当前仓库中。
git remote rename <old_name> <new_name>：   # 将已配置的远程仓库重命名。
git remote remove <remote_name>：   # 从当前仓库中删除指定的远程仓库。
git remote set-url <remote_name> <new_url>：    # 修改指定远程仓库的 URL。
git remote show <remote_name>： # 显示指定远程仓库的详细信息，包括 URL 和跟踪分支。
```

### git fetch

`git fetch` 命令用于从远程获取代码库。

该命令执行完后需要执行 `git merge` 远程分支到你所在的分支。

假设你配置好了一个远程仓库，并且你想要提取更新的数据，你可以首先执行:

```sh
git fetch [alias]
# 以上命令告诉 Git 去获取它有你没有的数据，然后你可以执行：
git merge [alias]/[branch]
# 以上命令将服务器上的任何更新（假设有人这时候推送到服务器了）合并到你的当前分支
```

接下来我们在 Github 上点击 README.md 并在线修改它:

然后我们在本地更新修改。

```sh
# 获取自己仓库
git fetch origin
# 获取原始仓库,首先配置原始仓库地址
git remote add upstream git@github.com:xxx/xxx.git
git fetch upstream
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:tianqixin/runoob-git-test
   0205aab..febd8ed  master     -> origin/master
以上信息"0205aab..febd8ed master -> origin/master" 说明 master 分支已被更新，我们可以使用以下# 命令将更新同步到本地：
git merge origin/master
git merge upstream/master
```

## 第一次修改内容
