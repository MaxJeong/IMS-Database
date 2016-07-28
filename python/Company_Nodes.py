#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ActiveCompanies(Leaf):
	"""docstring for ActiveCompanies"""
	def __init__(self):
		super(ActiveCompanies, self).__init__("List Active Companies")

	def execute(self):
		results = get_all_active_companies()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

class ListCompanies(Leaf):
	def __init__(self):
		super(ListCompanies, self).__init__("List Companies")

	def execute(self):
		results = get_all_companies()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		
class GetCompany(Leaf):
	"""docstring for GetCompany"""
	def __init__(self):
		super(GetCompany, self).__init__("Get Company")
	
	def execute(self):
		Company = get_input("Enter the Company ID you want:",int)
		results = get_all_rows("Company" ,[Company])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.Company = Company
		
class UpdateCompany(GetCompany):
	"""docstring for UpdateCompany"""
	def __init__(self):
		super(GetCompany, self).__init__("Update Company")
	
	def execute(self):
		super(UpdateCompany, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			name = get_input("Name:",str)
			division = get_input("Division:",str)
			c = get_input("Customer Company? (Y/N):",str)
			customer = (c == "Y" or c == "y")
			a = get_input("Active?:",str)
			active = (a == "Y" or a == "y")
			city = get_input("City ID:",int)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("Company", [self.Company, name, division, active, customer, city])
				print("Company - " + str(self.Company) + " has been updated.")

class RemoveCompany(GetCompany):
	"""docstring for RemoveCompany"""
	def __init__(self):
		super(GetCompany, self).__init__("Delete Company")
	
	def execute(self):
		super(RemoveCompany, self).execute()
		
		s = get_input("Do you wish to delete this Company?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("Company", [self.Company])
			print("Company - " + str(self.Company) + " has been deleted.")
			
class InsertCompany(Leaf):
	"""docstring for InsertCompany"""
	def __init__(self):
		super(InsertCompany, self).__init__("Insert Company")
	
	def execute(self):
		name = get_input("Name:",str)
		division = get_input("Division:",str)
		c = get_input("Customer Company? (Y/N):",str)
		customer = (c == "Y" or c == "y")
		a = get_input("Active?:",str)
		active = (a == "Y" or a == "y")
		city = get_input("City ID:",int)
		s = get_input("Do you wish to create your new Company?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("Company", [None,  name, division, active, customer, city])
			print("A new Company has been created")