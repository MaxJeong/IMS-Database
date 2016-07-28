#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ListSuppliers(Leaf):
	"""docstring for Assets"""
	def __init__(self):
		super(ListSuppliers, self).__init__("List Supplier")

	def execute(self):
		results = get_all_Suppliers()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

class SearchSupplier(Leaf):
	"""docstring for SearchSupplier"""
	def __init__(self):
		super(SearchSupplier, self).__init__("Search Suppliers")
	
	def execute(self):
		s = get_input("Enter some keyword to search by",str)
		results = search_Suppliers(s)
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		
class GetSupplier(Leaf):
	"""docstring for GetSupplier"""
	def __init__(self):
		super(GetSupplier, self).__init__("Get Supplier")
	
	def execute(self):
		Supplier = get_input("Enter the Supplier ID you want:",int)
		results = get_all_rows("Supplier" ,[Supplier])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.Supplier = Supplier
		
class UpdateSupplier(GetSupplier):
	"""docstring for UpdateSupplier"""
	def __init__(self):
		super(GetSupplier, self).__init__("Update Supplier")
	
	def execute(self):
		super(UpdateSupplier, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			comp = get_input("Company ID:",int)
			contact = get_input("Person of Contact:",str)
			postCode = get_input("Postal Code:",str)
			email = get_input("Email:",str)
			phone = get_input("Phone#:",str)
			address = get_input("Address(<street><number><appt>):",str)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("Supplier", [self.Supplier, comp, contact, postCode, email, phone, address])
				print("Supplier - " + str(self.Supplier) + " has been updated.")

class RemoveSupplier(GetSupplier):
	"""docstring for RemoveSupplier"""
	def __init__(self):
		super(GetSupplier, self).__init__("Delete Supplier")
	
	def execute(self):
		super(RemoveSupplier, self).execute()
		
		s = get_input("Do you wish to delete this Supplier?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("Supplier", [self.Supplier])
			print("Supplier - " + str(self.Supplier) + " has been deleted.")
			
class InsertSupplier(Leaf):
	"""docstring for InsertSupplier"""
	def __init__(self):
		super(InsertSupplier, self).__init__("Insert Supplier")
	
	def execute(self):
		comp = get_input("Company ID:",int)
		contact = get_input("Person of Contact:",str)
		postCode = get_input("Postal Code:",str)
		email = get_input("Email:",str)
		phone = get_input("Phone#:",str)
		address = get_input("Address(<street><number><appt>):",str)
		s = get_input("Do you wish to create your new Supplier?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("Supplier", [None, comp, contact, postCode, email, phone, address])
			print("A new Supplier has been created")