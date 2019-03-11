python2.7到2020年1.1后就要淘汰了。

显示：`defaults write com.apple.finder AppleShowAllFiles -bool true ` 

隐藏：`defaults write com.apple.finder AppleShowAllFiles -bool false`


## 0. 准备工作：anaconda升级

其实去年已经装了一次python3了。

``` 
conda list
conda info -e               #(or --envs)
conda update conda
conda update python
conda create --name python35 python=3.5.1
```

### 升级pip

查看pip版本：
`pip show pip`

升级pip：
`pip install --upgrade pip`

## 1. 在anaconda中切换python2和python3  

为了在anaconda中同时能使用py2 py3  

```
source activate python35
python -V                  #(or --version)
conda deactivate python35
```

激活后升级，可升级对应到版本。例如，在python3被激活的情况下升级python，会由python3.5升级到python3.7。python2同理。

后来发现，`conda deactivate python35`这句话没有用。但是关了终端再重新打开，就回到python2了。

## 2. 在ipython中切换python2和python3  

发现以上操作只是在anaconda中管理两个版本，并没有在ipython中切换。


终端输入：

```
which ipython
这里会列出当前ipython路径
cat 上面这个路径
会展示ipython配置文件，其中头部会告诉你用了哪个路径的python版本
```

下一步修改文件。不是在终端了，是找到这个文件，进行修改。

修改未成功，原因是python35下的bin文件夹里，没有python.app这个文件。python3.7等，系统会显示无法解析二进制文件。

放弃修改这个文件。

另外找了个招，重新安装和配置了python内核。
[IPython3 notebook 成功配置Python2和Python3内核（Kernel）](http://www.mamicode.com/info-detail-2246203.html)

>> 
安装python 内核
  python2:  
 `sudo pip2 install ipykernel`
  python3:  
 `sudo pip3 install ipykernel`
>> 
配置python内核
  python 2:
  `sudo ipython2 kernel install --name python2 `
  python 3:
  `sudo ipython3 kernel install --name python3`
>> 
启动ipython notebook
  `sudo ipython notebook`


## 3. 使用python2 和 python3

### 3.1 运行python2:  

1. 终端直接输入 `python`
2. 终端输入： `ipython `
3. 运行 `jupyter notebook`, new python2 或者运行 `ipython notebook`，同样效果。

以上均成功。即在本机使用python2是完全正常的。  

重新安装和配置了后，以上失效。现在系统默认py3。。。。。

### 3.2 运行python3:  

1. 终端直接输入`python3`.此时运行的是python3.5.1，应该是去年安装的版本，不是从anaconda里升级的3.7版本。用which找出了它的安装位置：`which python3`。确实位置不同。
2. 运行 `jupyter notebook`, new python3 或者运行 `ipython notebook`，同样效果。











