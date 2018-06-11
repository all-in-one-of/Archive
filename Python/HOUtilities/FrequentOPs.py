'''
########################################################################
# Frequent OPs
# by Vishang Shah (vishangshah.com)
# IMPORTANT : This tool is tested and works only with Houdini 14.
#
# Description : Provides an interface for quick access to frequently used OPs
#
# Usage : Copy the parent folder HOUtilities to [your houdini 14.0 installation]\houdini\python2.7libs\
#
To Do : Move list of OP names to an external XML or JSON file.
To Do : Provide functionality to users to create/modify this OP names list in Houdini itself.
To Do : Preferences. To set prefered colors for OPs as well as layout presets for SOPs, DOPs etc...
To Do : Not having to select any OP for the creation of new one.
To Do : Context specific layout to separate SOP and VOPSOP OPs.
#
########################################################################
'''

# Import libraries
import os
import sys

import hou

from PySide.QtCore import *
from PySide.QtGui import *
from PySide import QtWebKit
from functools import partial

from . import Color
reload(Color)

# Reload

# HDAManager
class FrequentOPs(QFrame):
	def __init__(self, parent=None):
		super(FrequentOPs, self).__init__(parent)

		# all HDAs in current houdini file
		self.opNames = []

		# UI vars
		self.ui_button_width    = 120
		self.ui_button_height   = 40

		# Main Layout
		self.mainLayout = QHBoxLayout()
		self.setLayout(self.mainLayout)


		self.refreshOpNames()


	def listOpNames(self):
		'''
		Define list of OPs to be added.
		OPs are separated into columns by "-" separator.
		'''
		self.opNames = []
		self.opNames.append("null")
		self.opNames.append("group")
		self.opNames.append("merge")
		self.opNames.append("xform")
		self.opNames.append("-")
		self.opNames.append("curve")
		self.opNames.append("grid")
		self.opNames.append("box")
		self.opNames.append("sphere")
		self.opNames.append("-")
		self.opNames.append("resample")
		self.opNames.append("carve")
		self.opNames.append("facet")
		self.opNames.append("-")
		self.opNames.append("pointwrangle")
		self.opNames.append("attribwrangle")
		self.opNames.append("attribcreate")
		self.opNames.append("vopsop")


	def refreshOpNames(self):
		'''
		Refresh HDAs
		'''
		self.listOpNames()
		#columnLayout = QtGui.QVBoxLayout()
		columns = []

		for i in range(0, len(self.opNames)):
			if(self.opNames[i] == "-"):
				#self.mainLayout.addStretch(1)
				columnLayout = QVBoxLayout()
				columnLayout.setAlignment(Qt.AlignTop)
				columns.append(columnLayout)
			else:
				if(i == 0):
					columnLayout = QVBoxLayout()
					columnLayout.setAlignment(Qt.AlignTop)
					columns.append(columnLayout)
				op = self.opNames[i]
				btnOp = QPushButton(op)
				btnOp.setMaximumWidth(self.ui_button_width)
				btnOp.setMinimumHeight(self.ui_button_height)
				btnOp.setMaximumHeight(self.ui_button_height)
				#if i < 4:  
					#btnOp.setStyleSheet('QPushButton {background-color: blue; color: yellow}')
				btnOp.clicked.connect(partial(self.create_sop, op))
				columnLayout.addWidget(btnOp)#, (1, 0), (2,2))

		for column in columns:
			self.mainLayout.addLayout(column)
			#self.mainLayout.addStretch(0)


	def create_sop(self, opName = "null"):
		currentSel = hou.selectedNodes()
		if len(currentSel) == 1:
			current = currentSel[0]
			parentNode = hou.node(current.path()).parent()

			#newNode = parentNode.createNode(opName)
			newNode = current.createOutputNode(opName)

			newNode.setName(opName, True)

			if(opName == "null"):
				newNode.setColor(Color.Black)
			else:
				newNode.setColor(Color.Default)

			newNode.setCurrent(True, True)

			'''
			try:
				newNode.setFirstInput(hou.node(current.path()))
			except:
				pass
			'''

			newNode.moveToGoodPosition()

			newNode.setDisplayFlag(True)
			newNode.setRenderFlag(True)


