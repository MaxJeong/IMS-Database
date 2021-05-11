#!/usr/bin/python
import sys
from SQL_StoredProcedures import *

def get_all_cites():
    return call_storedProc('All_getCities', [])

def get_all_Suppliers():
    return call_storedProc('All_getSuppliers', [])

def get_all_purchase_orders():
    return call_storedProc('All_getPODetail', [])

def get_all_active_companies():
    ''' Returns  '''
    return call_storedProc('All_getActiveCompanies', [])

def get_all_companies():
    return call_storedProc('All_getCompanies', [])

def get_all_Assets():
    ''' Returns  '''
    return call_storedProc('All_getAssets', [])

def get_all_assetTypes():
    ''' Returns  '''
    return call_storedProc('All_getAssetTypes', [])

def search_Assets(keyword):
    return call_storedProc("Search_Assets",[keyword])

def search_Suppliers(keyword):
    return call_storedProc("Search_Suppliers",[keyword])

def search_PurchaseOrders(keyword):
    return call_storedProc("Search_PODetail",[keyword])

def get_input(prompt,convert):
    '''prompt is a message for the user
    convert will be applied to input,then returned
    Need to implement limit checking
    '''
    print (prompt)
    s = ""
    if (sys.version_info > (3,0)):
        s = input()
    else:
        s = raw_input()
    return convert(s)

def get_all_rows(entity, args):
    if entity == "Asset":
        return call_storedProc('getAsset', args)
    elif entity == "City":
        return call_storedProc('getCity', args)
    elif entity == "Company":
        return call_storedProc('getCompany', args)
    elif entity == "Purchase":
        return call_storedProc('getPurchaseOrder', args)
    elif entity == "Supplier":
        return call_storedProc('getSupplier', args)
    elif entity == "AssetType":
        return call_storedProc('getAssetType', args)    


def input_Row(entity, args):
    if entity == "Asset":
        return exec_storedProc('setAsset', args)
    elif entity == "City":
        return exec_storedProc('setCity', args)
    elif entity == "Company":
        return exec_storedProc('setCompany', args)
    elif entity == "Purchase":
        return exec_storedProc('setPurchaseOrder', args)
    elif entity == "Supplier":
        return exec_storedProc('setSupplier', args)
    elif entity == "AssetType":
        return exec_storedProc('setAssetType', args)    

def delete_entity(entity, args):
    if entity == "Asset":
        return exec_storedProc('remAsset', args)
    elif entity == "City":
        return exec_storedProc('remCity', args)
    elif entity == "Company":
        return exec_storedProc('remCompany', args)
    elif entity == "Purchase":
        return exec_storedProc('remPurchaseOrder', args)
    elif entity == "Supplier":
        return exec_storedProc('remSupplier', args)
    elif entity == "AssetType":
        return exec_storedProc('remAssetType', args)    