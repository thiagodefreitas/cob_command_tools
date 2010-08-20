#!/usr/bin/python

import rospy
from simple_script_server import *

class buttons:
	def __init__(self):
		self.sss = simple_script_server()
		self.panels = []
		self.CreatePanel()

	def CreatePanel(self):
		param_prefix = "/dashboard/buttons"
		if not rospy.has_param(param_prefix):
			rospy.logerr("parameter %s does not exist on ROS Parameter Server, aborting...",param_prefix)
			return False
		group_param = rospy.get_param(param_prefix)
		#print group_param
		group_param = self.SortDict(group_param)
		#print group_param
		
		for group in group_param:
			print group[0]
			buttons = []
			for button in group[1]:
				print button
				if button[1] == "move":
					buttons.append(self.CreateButton(button[0],self.sss.move,button[2],button[3]))
				elif button[1] == "trigger":
					buttons.append(self.CreateButton(button[0],self.sss.trigger,button[2],button[3]))
				elif button[1] == "mode":
					buttons.append(self.CreateButton(button[0],self.sss.set_operation_mode,button[2],button[3]))
				else:
					rospy.logerr("Function <<%s>> not known to dashboard",button[1])
					return False
			group = (group[0],buttons)
			self.panels.append(group)
	
	def CreateButton(self,button_name,function,component_name,parameter_name):
		#button = ([(button_name,function,(component_name,parameter_name)),])
		button = (button_name,function,(component_name,parameter_name,False))
		return button
		
	def SortDict(self,dictionary):
		keys = sorted(dictionary.iterkeys())
		k=[]
		#print "keys = ", keys
		#for key in keys:
		#	print "values = ", dictionary[key]
		return [[key,dictionary[key]] for key in keys]
