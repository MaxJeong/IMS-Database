#!/usr/bin/python
import SQL_StoredProcedures
from Input_Data import *
from TerminalTree import *
import sys
import datetime

class ListPurchases(Leaf):
	
	def __init__(self):
		super(ListPurchases, self).__init__("List Purchase orders")
		
	def execute(self):
		results = get_all_purchase_orders()
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)	

class SearchPurchases(Leaf):
	"""docstring for SearchPurchases"""
	def __init__(self):
		super(SearchPurchases, self).__init__("Search purchases made")
	
	def execute(self):
		s = get_input("Enter some keyword to search by",str)
		results = search_PurchaseOrders(s)
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)

		
class GetPurchaseOrder(Leaf):
	"""docstring for GetPurchaseOrder"""
	def __init__(self):
		super(GetPurchaseOrder, self).__init__("Get Purchase Order")
	
	def execute(self):
		PurchaseOrder = get_input("Enter the PurchaseOrder ID you want:",int)
		results = get_all_rows("Purchase" ,[PurchaseOrder])
		column = results[0]
		values = results[1]
		temp = ""
		for i in column:
			temp = temp + i[0]+","
		print (temp)
		comps = " \n ".join(", ".join(map(str,val)) for val in values)
		print (comps)
		self.PurchaseOrder = PurchaseOrder
		
class UpdatePurchaseOrder(GetPurchaseOrder):
	"""docstring for UpdatePurchaseOrder"""
	def __init__(self):
		super(GetPurchaseOrder, self).__init__("Update Purchase Order")
	
	def execute(self):
		super(UpdatePurchaseOrder, self).execute()
		
		s = get_input("Do you wish to continue?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			name = get_input("Name:",str)
			price = get_input("Price:",float)
			Day = get_input("Purchase Day:",int)
			Month = get_input("Purchase Month:",int)
			Year = get_input("Purchase Year:",int)
			pDate = datetime.datetime(Year, Month, Day)
			descript = get_input("Description:",str)
			quant = get_input("Items Purchased:",int)
			supp = get_input("Supplier ID:",int)
			s = get_input("Do you wish to save your changes?(Y/N) ",str)
			flag = (s == "Y" or s == "y")		
			if (flag):
				input_Row("Purchase", [self.PurchaseOrder, name, price, pDate, descript, quant, supp])
				print("PurchaseOrder - " + str(self.PurchaseOrder) + " has been updated.")

class RemovePurchaseOrder(GetPurchaseOrder):
	"""docstring for RemovePurchaseOrder"""
	def __init__(self):
		super(GetPurchaseOrder, self).__init__("Delete Purchase Order")
	
	def execute(self):
		super(RemovePurchaseOrder, self).execute()
		
		s = get_input("Do you wish to delete this PurchaseOrder?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			delete_entity("Purchase", [self.PurchaseOrder])
			print("PurchaseOrder - " + str(self.PurchaseOrder) + " has been deleted.")
			
class InsertPurchaseOrder(Leaf):
	"""docstring for InsertPurchaseOrder"""
	def __init__(self):
		super(InsertPurchaseOrder, self).__init__("Insert Purchase Order")
	
	def execute(self):
		name = get_input("Name:",str)
		price = get_input("Price:",float)
		Day = get_input("Purchase Day:",int)
		Month = get_input("Purchase Month:",int)
		Year = get_input("Purchase Year:",int)
		pDate = datetime.datetime(Year, Month, Day)
		descript = get_input("Description:",str)
		quant = get_input("Items Purchased:",int)
		supp = get_input("Supplier ID:",int)
		s = get_input("Do you wish to create your new PurchaseOrder?(Y/N) ",str)
		flag = (s == "Y" or s == "y")		
		if (flag):
			input_Row("Purchase", [None, name, price, pDate, descript, quant, supp])
			print("A new PurchaseOrder has been created")