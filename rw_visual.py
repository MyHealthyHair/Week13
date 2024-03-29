# coding=gbk
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
	
	# 创建一个RandomWalk实例，并将其包含的点都绘制出来
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# 设置绘图窗口的尺寸
	plt.figure(figsize=(10, 6))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=1)
	plt.show()
	
	keep_running = input('Make another walk?(y/n): ')
	if keep_running == 'n':
		break
