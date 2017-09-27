# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

import matplotlib
from matplotlib import style
from os import path
from matplotlib.font_manager import fontManager
import os

# 面向对象的绘图库

# figure 图形/图像、figsize宽度高度、dpi分辨率、前景色、边缘色
# subplot 绘制子图
# axes 轴，坐标轴，坐标轴的属性：xlabel、ylabel、title、xlim、ylime、legend、grid

# savefig() 保存图像/图表

# gcf 获得图表的figure对象， 获得gca表示师子图的Axes对象，gcf和gca保存当前图表和当前子图等信息


fig = plt.gcf()
axes = plt.gca()
print fig
print axes
axes.set_xlim(0,10)
axes.set_ylim(0,5)
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_title("stat chart")
axes.legend()
axes.grid(True)
fig.subplots_adjust(top=0.85, bottom=0.05, left=0.05, right=0.95) # 调整边距,wspace hspace 宽 高
# plt.show()


plt.figure(figsize=(4,3)) # 设置的默认的宽度和高度英寸* 像素80
x = np.arange(0,5,.1)
line = plt.plot(x,0.05*x*x)[0]
line.set_alpha(0.05)  # 设置透明度
print line.get_linewidth()
print plt.getp(line,"color")

lines = plt.plot(x,np.sin(x),x,np.cos(x))  
plt.setp(lines,color='r',linewidth=4.0) # setp配置对象的属性 设置线的颜色和线宽
#plt.show()


alllines = plt.getp(plt.gca(),"lines")
for l in alllines:
	print l

# 绘制子图

for idx, color in enumerate("rgbyck"):
	print idx,color
	plt.subplot(321+idx, axisbg=color)
# plt.show()


plt.figure(1)
plt.figure(2)
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)
x = np.linspace(0,3,100)

# sca() 设置当前的Axes对象，即指定当前子图
for i in xrange(5):
	plt.figure(1)
	plt.plot(x, np.exp(i*x/3))
	plt.sca(ax1)
	plt.plot(x,np.sin(i*x))
	plt.sca(ax2)
	plt.plot(x,np.cos(i*x))
# plt.show()

# 一次生成多个子图，返回图表对象和子图对象
fig, axes = plt.subplots(2,3)
[a,b,c],[d,e,f] = axes
print axes.shape
print a,b,c
print d,e,f

#plt.show()



# subplot2grid 表格布局 shape loc rowspan colspan
fig = plt.figure(figsize=(6,6)) # 图形的宽度和高度
ax1 = plt.subplot2grid((3,3),(0,0),colspan=2) # 表示表格形状的元组（行列）
ax2 = plt.subplot2grid((3,3),(0,2),rowspan=2)
ax3 = plt.subplot2grid((3,3),(1,0),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,1),colspan=2)
ax5 = plt.subplot2grid((3,3),(1,1))
#plt.show()




print path.abspath(matplotlib.get_configdir())# 用户配置路径
print path.abspath(matplotlib.matplotlib_fname()) # 配置文件的路径
print matplotlib.rc_params() # 配置文件 配置字典

print '-------'
print matplotlib.RcParams
print matplotlib.rcParams["lines.marker"]
plt.plot([1,2,3,2])

matplotlib.rcParams["lines.marker"]="o"
plt.plot([1,2,3,2])
print matplotlib.rcParams["lines.marker"]

matplotlib.rc("lines",marker="x",linewidth=2,color="red") # rc 配置标识符、线宽、颜色
# plt.show()

matplotlib.rcdefaults() # 恢复默认配置

matplotlib.rcParams.update(matplotlib.rc_params())  # 载入最新配置

# rcParams、rc和 rcdefaults

# 绘图样式

print style.available
# 切换样式

style.use("ggplot")

# 显示中文

print fontManager.ttflist[:6] # ttflist 系统字体列表
print fontManager.ttflist[0].name # 字体全路径
print fontManager.ttflist[1].fname # 字体名

# 打印字体

fig = plt.figure(figsize=(8,7))
ax = plt.subplot(111)
plt.subplots_adjust(0,0,1,1,0,0)

plt.xticks([])
plt.yticks([])
x, y = 0.5, 0.5
fonts = [font.name for font in fontManager.ttflist if path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
font =set(fonts)
dy = (1.0 - y) / (len(fonts) // 4 + (len(fonts)%4 != 0))
print dy
for font in fonts:
	t = ax.text(x, y + dy / 2, u"中文字体", transform=ax.transAxes)
	ax.text(x,y,font, {'fontsize':12}, transform=ax.transAxes)
	x += 0.25 
	if x >= 1.0: 
		y += dy 
		x = 0.05
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# plt.show()

# 直接修改配置字典，设置字体
plt.rcParams["font.family"] = "SimHei" 
plt.plot([1,2,3]) 
plt.show()


# Axes 容器


#绘图：画布、坐标轴/坐标系、子图
# 创建Figure对象，为Figure对象创建一个或多个Axes对象
# 调用Axes对象，创建Artist对象

fig = plt.figure()
fig.patch.set_color("g") # 设置背景色

ax = fig.add_axes([0.15,0.1,0.7,0.3])
ax.patch.set_facecolor("red") # 设置背景色为红色
line = ax.plot([1,2,3],[1,2,1])[0]
print line is ax.lines[0]
ax.set_xlabel("time")
print ax.get_xaxis().get_label().get_text()
#plt.show()

line = plt.plot([1,2,3,2,1],lw=4)[0]
line.set_alpha(0.5)
line.set(alpha=0.5,zorder=2)
plt.getp(fig.patch) # Artist 对象的所有属性名及对应的值
#plt.show()


fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor("green")

x, y = np.random.rand(2, 100) # 均匀分布
print np.random.rand(2, 100)
line = ax.plot(x, y, color="blue", linewidth=2)[0] 
line is ax.lines[0]
# plt.show()


rect = plt.Rectangle((1,1),width=5,height=12) 
ax.add_patch(rect)
print ax.get_xlim()
print ax.dataLim._get_bounds()
print ax.get_xlim()
ax.autoscale_view() # 自动调节显示范围
# plt.show()

fig, ax = plt.subplots()
t = ax.scatter(np.random.rand(20),np.random.rand(20))
plt.show()

#plt.show()


# Axis 容器 坐标轴上的刻度线、刻度文本、坐标网格、坐标轴标题等。刻度：主刻度、副刻度

fig, ax = plt.subplots()
axis = ax.xaxis
print axis.get_ticklocs() # 刻度位置列表
print axis.get_ticklabels() # 刻度标签列表

print [x.get_text() for x in axis.get_ticklabels()] # 刻度文本字符串

print axis.get_ticklines() # 获得主刻度线的列表
print axis.get_ticklines(minor=True) #获得副刻度线的列表

# 设置刻度线为绿色粗线，文本为 红色并且旋转45°
for label in axis.get_ticklabels():
	label.set_color("red")
	label.set_rotation(45)
	label.set_fontsize(16)

for line in axis.get_ticklines():
	line.set_color("green")
	line.set_markersize(25)
	line.set_markeredgewidth(3)

print axis.get_minor_locator()
print axis.get_major_locator()
#plt.show()


# transform() 将此坐标系中的坐标转换为窗口坐标系中的坐标














