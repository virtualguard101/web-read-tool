# 学习通网页阅读时长类课程小助手

基于**python-pyautogui**实现的学习通阅读时长类刷课小助手

## 背景

起因是学校的的某阅读类通识选修课竟要求在其他课程或考试几乎全满的前提下要求选修该课程的**大学牲**在一个月内搞定学习通上**6x280**分钟的阅读任务（占比**60%**，各个模块满分**10分**，每个模块**150min-179**方可得到可怜的**6分**），~~对于我这种文盲，所谓的“经典”是不可能看的~~，本人不希望自己的时间被所谓的“经典阅读”所支配，故出此下策。**阅读本应是学生自己的事情，学生的时间应由他们自己管理，学生的未来应由他们自己投资，本应如此**。~~你们这么在意这个学分系统干什么啊？它会把学生的付出给异化调的懂吗？~~

另外，有人可能会有疑问，阅读这种任务直接挂着网页刷时长不行吗？还真不太行。

本人亲测，十分钟内，在不使用脚本的情况下滑动网页1分钟，其余9分钟挂机闲置，时长积分只加了1，与使用脚本的效果相去甚远。

至少在我这的情况是这样的，积分的界面如下，仅供参考：

![grade-demo](https://github.com/virtualguard101/web-read-tool/blob/main/demo0.png?raw=true)

## 原理 & 用法

原理和用法很简单，课程的主要任务是刷阅读时长。将阅读过程简化，省略知识从网页进入你脑子的“人机交互”过程，你在阅读/刷时长时无非就是一个在阅读界面划来划去的过程。

那我用`pyautogui`让计算机在阅读网页上自己划来划去不就可以了☝🤓

废话不多说，下面讲具体用法：

首先克隆仓库
```bash
git clone https://github.com/virtualguard101/web-read-tool.git
cd web-read-tool
```

安装依赖库
```bash
pip install -r requirements.txt
```

随后准备好你在学习通上需要刷阅读时长的课程的任意一个阅读界面，在终端运行命令
```bash
python lesson_brush.py
```

由于添加了`shebang`，使用liunx的同志也可以在给脚本添加权限后直接执行：
```bash
chmod +x lesson_brush.py
./lesson_brush.py
```

按照终端提示输入想要运行的时长，随后快速切回阅读界面，看着界面自己来回滚动即可，觉得无聊，也可以把电脑晾在一旁做自己的事

想要终止运行，按下`super`+`D`切到桌面后唤出终端`ctrl`+`C`即可

## 注意事项

本项目为作者即兴发挥，当前十分简陋，仅仅只由一个脚本与一个日志文件构成（日志由脚本生成，主要作用是记录运行每次脚本运行的时长，方便计算刷课总时长）

在使用工具的时候请不要关闭命令窗口，否则程序会停止运行

在运行脚本时务必保证当前页面为需要刷时长的阅读界面，这个工具没那么高级，**不支持后台运行**

另外在一个阅读界面运行一段时间后，最好切换到另一个，否则可能出现刷课无效的情况

由于是即兴发挥，本项目不作定期更新，有建议或是bug请移步`issue`，也希望各路大佬能够提交`PR`，随缘解决。没办法，大学生活过于“充实”了。

## 版本信息

### v0.0.0
初始化项目功能
### v0.0.1
修复时长记录的逻辑错误

## 声明

**README中的背景介绍为项目背景演绎，切勿当真**

**本项目仅供学习参考, 不能用于非法用途，请在下载后24h内删除。**
