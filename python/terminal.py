from Input_Data import *
from TerminalTree import *
import mysql.connector
import sys
from Asset_Nodes import *
from Supplier_Nodes import *
from PurchaseOrder_Nodes import *
from Company_Nodes import *
from City_Nodes import *
from AssetType_Nodes import *

if __name__ == '__main__':
    
    active = ActiveCompanies()
    
    delCity = RemoveCity()
    updateCity = UpdateCity()
    getCity = GetCity()
    insCity = InsertCity()    
    citySingleton = Node("Edit Cities",[getCity,updateCity,insCity,delCity])    
    
    listPurchases = ListPurchases()
    listAssets = ListAssets()
    listSuppliers = ListSuppliers()
    listCities = ListCities()
    listCompanies = ListCompanies()
    listAssetTypes = ListAssetTypes()
    
    searchAssets = SearchAssets()
    searchSupplier = SearchSupplier()
    searchPurchases = SearchPurchases()
    
    delCompany = RemoveCompany()
    updateCompany = UpdateCompany()
    getCompany = GetCompany()
    insCompany = InsertCompany()    
    companySingleton = Node("Edit Companies",[getCompany,updateCompany,insCompany,delCompany])    
    
    delPurchase = RemovePurchaseOrder()
    updatePurchase = UpdatePurchaseOrder()
    getPurchase = GetPurchaseOrder()
    insPurchase = InsertPurchaseOrder()
    purchaseSingleton = Node("Edit Purchase Orders",[getPurchase,updatePurchase,insPurchase,delPurchase])    
    
    delSupplier = RemoveSupplier()
    updateSupplier = UpdateSupplier()
    getSupplier = GetSupplier()
    insSupplier = InsertSupplier()
    supplierSingleton = Node("Edit Suppliers",[getSupplier, updateSupplier, insSupplier, delSupplier])    
   
    delAsset = RemoveAsset()
    updateAsset = UpdateAsset()
    getAsset = GetAsset()
    insAsset = InsertAsset()
    assetSingleton = Node("Edit Assets",[getAsset,updateAsset,insAsset,delAsset])
    
    delAssetType = RemoveAssetType()
    updateAssetType = UpdateAssetType()
    getAssetType = GetAssetType()
    insAssetType = InsertAssetType()
    assetTypeSingleton = Node("Edit Asset Types",[getAssetType,updateAssetType,insAssetType,delAssetType])    
    
    city = Node("Cities", [listCities,citySingleton])
    company = Node("Companies", [listCompanies, active,companySingleton])
    purchase = Node("Purchases",[listPurchases,searchPurchases,purchaseSingleton])
    suppiler = Node("Suppilers",[listSuppliers,searchSupplier, supplierSingleton])
    asset = Node("Assets",[listAssets,searchAssets,assetSingleton])
    assettype = Node("Asset Types",[listAssetTypes,assetTypeSingleton])
    main = Node("Main menu",[asset,assettype,suppiler,purchase,company,city])
    curr = main

    while True:
        if (isinstance(curr,Node) ):
            'Only nodes have options to display and choose '
            # print (curr.get_description())
            print (curr.get_options())
            choice = get_input("Select one",int)
            curr = curr.select(choice-1)
        
        else:
            'Leafs execute their job and return to their parent'
            curr.execute()
            curr = curr.parent
        # print curr.execute()
        # print curr