#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ListAssets(Leaf):
	"""docstring for Assets"""
	def __init__(self):
		super(ListAssets, self).__init__("List Assets")

	def execute(self):
		results = get_all_Assets()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

class SearchAssets(Leaf):
	"""docstring for SearchAssets"""
	def __init__(self):
		super(SearchAssets, self).__init__("Search Assets")
	
	def execute(self):
		s = get_input("Enter some keyword to search by",str)
		results = search_Assets(s)
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

class GetAsset(Leaf):
	"""docstring for GetAsset"""
	def __init__(self):
		super(GetAsset, self).__init__("Get Asset")
	
	def execute(self):
		asset = get_input("Enter the asset ID you want:",int)
		results = get_all_rows("Asset" ,[asset])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.asset = asset
		
class UpdateAsset(GetAsset):
	"""docstring for UpdateAsset"""
	def __init__(self):
		super(GetAsset, self).__init__("Update Asset")
	
	def execute(self):
		super(UpdateAsset, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			name = get_input("Name:",str)
			currentVal = get_input("Current Value:",float)
			Day = get_input("Arrival Day:",int)
			Month = get_input("Arrival Month:",int)
			Year = get_input("Arrival Year:",int)
			arrival = datetime.datetime(Year, Month, Day)
			PO = get_input("Purchase Order ID:",int)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("Asset", [self.asset, name, currentVal, arrival, PO])
				print("Asset - " + str(self.asset) + " has been updated.")

class RemoveAsset(GetAsset):
	"""docstring for RemoveAsset"""
	def __init__(self):
		super(GetAsset, self).__init__("Delete Asset")
	
	def execute(self):
		super(RemoveAsset, self).execute()
		
		s = get_input("Do you wish to delete this asset?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("Asset", [self.asset])
			print("Asset - " + str(self.asset) + " has been deleted.")
			
class InsertAsset(Leaf):
	"""docstring for InsertAsset"""
	def __init__(self):
		super(InsertAsset, self).__init__("Insert Asset")
	
	def execute(self):
		name = get_input("Name:",str)
		currentVal = get_input("Current Value:",float)
		Day = get_input("Arrival Day:",int)
		Month = get_input("Arrival Month:",int)
		Year = get_input("Arrival Year:",int)
		arrival = datetime.datetime(Year, Month, Day)
		PO = get_input("Purchase Order ID:",int)
		s = get_input("Do you wish to create your new Asset?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("Asset", [None,name, currentVal, arrival, PO])
			print("A new asset has been created")