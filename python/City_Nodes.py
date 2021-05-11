#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ListCities(Leaf):
	"""docstring for Cities"""
	def __init__(self):
		super(ListCities, self).__init__("List Cities")

	def execute(self):
		results = get_all_cites()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

class GetCity(Leaf):
	"""docstring for GetCity"""
	def __init__(self):
		super(GetCity, self).__init__("Get City")
	
	def execute(self):
		City = get_input("Enter the City ID you want:",int)
		results = get_all_rows("City" ,[City])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.City = City
		
class UpdateCity(GetCity):
	"""docstring for UpdateCity"""
	def __init__(self):
		super(GetCity, self).__init__("Update City")
	
	def execute(self):
		super(UpdateCity, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			citName = get_input("City:",str)
			Province = get_input("Province:",str)
			Country = get_input("Country:",str)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("City", [self.City, citName, Province, Country])
				print("City - " + str(self.City) + " has been updated.")

class RemoveCity(GetCity):
	"""docstring for RemoveCity"""
	def __init__(self):
		super(GetCity, self).__init__("Delete City")
	
	def execute(self):
		super(RemoveCity, self).execute()
		
		s = get_input("Do you wish to delete this City?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("City", [self.City])
			print("City - " + str(self.City) + " has been deleted.")
			
class InsertCity(Leaf):
	"""docstring for InsertCity"""
	def __init__(self):
		super(InsertCity, self).__init__("Insert City")
	
	def execute(self):
		citName = get_input("City:",str)
		Province = get_input("Province:",str)
		Country = get_input("Country:",str)
		s = get_input("Do you wish to create your new City?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("City", [None, citName, Province, Country])
			print("A new City has been created")