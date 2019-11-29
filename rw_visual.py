# coding=gbk
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# ֻҪ�����ڻ״̬���Ͳ��ϵ�ģ���������
while True:
	
	# ����һ��RandomWalkʵ��������������ĵ㶼���Ƴ���
	rw = RandomWalk(50000)
	rw.fill_walk()
	
	# ���û�ͼ���ڵĳߴ�
	plt.figure(figsize=(10, 6))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
		edgecolor='none', s=1)
	plt.show()
	
	keep_running = input('Make another walk?(y/n): ')
	if keep_running == 'n':
		break
