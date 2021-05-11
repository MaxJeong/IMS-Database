#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ListAssetTypes(Leaf):
	"""docstring for ListAssetTypes"""
	def __init__(self):
		super(ListAssetTypes, self).__init__("List Asset Types")

	def execute(self):
		results = get_all_assetTypes()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)


class GetAssetType(Leaf):
	"""docstring for GetAssetType"""
	def __init__(self):
		super(GetAssetType, self).__init__("Get Asset Type")
	
	def execute(self):
		asset = get_input("Enter the asset Type ID you want:",int)
		results = get_all_rows("AssetType" ,[asset])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.asset = asset
		
class UpdateAssetType(GetAssetType):
	"""docstring for UpdateAsset"""
	def __init__(self):
		super(GetAssetType, self).__init__("Update Asset Type")
	
	def execute(self):
		super(UpdateAssetType, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			name = get_input("Name:",str)
			subType = get_input("SubType:",str)
			rate = get_input("Depreciation Rate:",float)
			interval = get_input("Depreciation Interval (months)",float)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("AssetType", [self.asset, name, subType, rate , interval])
				print("Asset - " + str(self.asset) + " has been updated.")

class RemoveAssetType(GetAssetType):
	"""docstring for RemoveAsset"""
	def __init__(self):
		super(GetAssetType, self).__init__("Delete Asset Type")
	
	def execute(self):
		super(RemoveAssetType, self).execute()
		
		s = get_input("Do you wish to delete this asset?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("AssetType", [self.asset])
			print("Asset Type - " + str(self.asset) + " has been deleted.")
			
class InsertAssetType(Leaf):
	"""docstring for InsertAsset"""
	def __init__(self):
		super(InsertAssetType, self).__init__("Insert Asset Type")
	
	def execute(self):
		name = get_input("Name:",str)
		subType = get_input("SubType:",str)
		rate = get_input("Depreciation Rate:",float)
		interval = get_input("Depreciation Interval (months)",float)
		s = get_input("Do you wish to create your new Asset Type?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("AssetType", [None,name, subType, rate , interval])
			print("A new asset Type has been created")