import numpy as np
import matplotlib.pyplot as plt

print(np.linspace(0,5,10))

# 在任何绘图之前，我们需要一个Figure对象，可以理解成我们需要一张画板才能开始绘图。
fig = plt.figure(
    figsize=(10,6), # figsize=(19,3) 寬X高 determines the size of the figure in inches
                   # The default figure size is (6.4, 4.8) inches
    dpi=90, # Dots per inches (dpi), default 100
            # e.g. 6.4 inches * 100 dpi = 640 pixels
    facecolor="bisque", # background color
) 

# 在拥有Figure对象之后，在作画前我们还需要轴，没有轴的话就没有绘图基准，所以需要添加Axes。
# 也可以理解成为真正可以作画的纸。
ax = fig.add_subplot(336) # 添加Axes，add_subplot(上下切幾塊，左右切幾塊，左上到右下第幾塊)
ax.set(xlim=[0.5,4.5], ylim=[-2,8], title='An Example Axes 1',
       ylabel='Y-Axis', xlabel='X-Axis')

ax2 = fig.add_subplot(331)
ax2.set(xlim=[0,5], ylim=[0,5], yticks=np.linspace(0,5,6), title='An Example Axes 2',
       ylabel='Y-Axis', xlabel='X-Axis')
# 畫點點
ax2.plot(
    [0,1,2  ,3,4,5], # x軸 (0~5共六個點)
    [1,3,4.6,3,1,2], # y軸 (亂寫六個點)
    'ro--',          # format, { r:redline, o:circlemarker', --:dashed_line_style, ... }
    linewidth=2,
)

ax3 = fig.add_subplot(338)
ax3.set(xlim=[0,5], ylim=[0,5], yticks=np.linspace(0,5,6), title='An Example Axes 3',
       ylabel='Y-Axis', xlabel='X-Axis')
# 畫柱狀
ax3.bar(
    [0,1,2  ,3,4], # x軸 (0,4共4個點)
    [1,3,4.6,3,1], # y軸 (亂寫0個點)
    color='lightblue', 
    align='edge',
)                                      

plt.show()

