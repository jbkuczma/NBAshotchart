import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc
from os import path, remove
from random import randint

class Grapher():

	def __init__(self, playerShotData):
		self.playerShotData = playerShotData

	def getShotCoordinates(self):
		xCoordinates = []
		yCoordinates = []
		shotStatus = []

		for shot in self.playerShotData:
			shotStatus.append(shot[10])
			xCoordinates.append(shot[17])
			yCoordinates.append(shot[18])

		return xCoordinates, yCoordinates, shotStatus

	'''
	shoutout to Savvas Tjortjoglou for this awesome tutorial on how to draw the court
	http://savvastjortjoglou.com/nba-shot-sharts.html
	'''
	def drawCourt(self, ax=None, color='black', lw=2, outerLines=False):
		if ax is None:
			ax = plt.gca()
			# ax.set_axis_bgcolor('#FAFAFA')

		hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
		backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
		outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color, fill=False)
		inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color, fill=False)
		top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180, linewidth=lw, color=color, fill=False)
		bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color, linestyle='dashed')
		restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw, color=color)
		corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw, color=color)
		corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
		three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)
		center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
		center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)
		court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw, bottom_free_throw, restricted, corner_three_a, corner_three_b, three_arc, center_outer_arc, center_inner_arc]
		if outerLines:
			outerLines = Rectangle((-250, -47.5), 500, 470, linewidth=lw, color=color, fill=False)
		court_elements.append(outerLines)
		for element in court_elements:
			ax.add_patch(element)
		return ax

	def makeGraph(self, xCoordinates, yCoordinates, madeX, madeY, missedX, missedY):

		fileName = 'static/jimmybutler.png'
		# cmap=plt.cm.gist_heat_r color=cmap(.2), cmap=cmap
		cmap=plt.cm.Blues
		sns.set(style='white')
		s = sns.jointplot(np.array(xCoordinates), np.array(yCoordinates), stat_func=None,  kind='hex', space=0, color="#4CB391")

		s.fig.set_size_inches(12,11)
		ax = s.ax_joint
		self.drawCourt(ax, outerLines=True)
		ax.set_xlim(-250,250)
		ax.set_ylim(422.5, -47.5)
		ax.set_xlabel('')
		ax.set_ylabel('')
		ax.tick_params(labelbottom='off', labelleft='off', labelright='off')

		# plot shots over hexagons
		ax2 = ax.twinx()
		sns.regplot(np.array(madeX), np.array(madeY), ax=ax2, fit_reg=False, color='#5E81BA', scatter_kws={'s':40})
		sns.regplot(np.array(missedX), np.array(missedY), ax=ax2, fit_reg=False, marker='x', color='red', scatter_kws={'s':80})
		# sns.regplot(np.array(xCoordinates), np.array(yCoordinates), ax=ax2, fit_reg=False)
		ax2.set_xlim(-250,250)
		ax2.set_ylim(422.5, -47.5)
		ax2.set_xlabel('')
		ax2.set_ylabel('')
		ax2.tick_params(labelbottom='off', labelleft='off', labelright='off')

		title = '{} shots made \n {} shots attempted'.format(len(madeX), len(xCoordinates))
		# ax.set_title(title, y=0.15, fontsize=24)
		# ax.set_title(title, y=1.13, x=0.16, fontsize=24)
		ax.set_title(title, y=0.01, x=0.81, fontsize=24)

		

		# plt.figure(figsize=(12,11))
		# plt.xlim(-250,250)
		# plt.ylim(422.5, -47.5)
		# s = sns.jointplot(np.array(xCoordinates), np.array(yCoordinates), stat_func=None, kind='hex', space=0, color=cmap(0.2), cmap=cmap)
		# s.fig.set_size_inches(12,11)
		# ax = s.ax_joint
		# ax.set_xlim(-250,250)
		# ax.set_ylim(422.5, -47.5)
		
		# plt.scatter(xCoordinates, yCoordinates)
		# need to calculate gridSize
		# gridSize = self.getGridSize(xCoordinates, yCoordinates) mincnt=1 plt.cm.Blues
		# gridSize = 25
		# plt.hexbin(xCoordinates, yCoordinates, mincnt=1, cmap=plt.cm.YlOrRd, gridsize=gridSize)
		
		# cb = plt.colorbar()
		# cb.set_label('Shots taken')

		# plt.scatter(xCoordinates, yCoordinates)

		# self.drawCourt(plt, outerLines=True)
		plt.savefig(fileName, transparent=True)
		# plt.savefig(fileName, transparent=True)
		# plt.savefig(fileName, facecolor=f.get_facecolor())
		return fileName


		