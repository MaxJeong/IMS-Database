#!/usr/bin/python

import mysql.connector

""" Here to call and retrieve information from the stored procedure"""
# def call_storedProc(storedproc):
#     cnx = mysql.connector.connect(user='Ryan', password='!bsodjaja9112',
#                               host='159.203.19.40', database='C43')
#     cursor = cnx.cursor()
    
#     result = cursor.callproc(storedproc)
#     cnx.commit()
#     return next(cursor.stored_results()).fetchall()

def call_storedProc(storedproc, args=[]):
    cnx = mysql.connector.connect(user='Ryan', password='!bsodjaja9112',
                              host='159.203.19.40', database='C43')
    cursor = cnx.cursor()
    columns = []
    result = cursor.callproc(storedproc, args)
    for item in cursor.stored_results():
        columns = item.description
        # for i in item:
        #     print (i)
    # for i in columns:
    #     print (i[0])

    cnx.commit()
    cnx.close()
    values = [columns,next(cursor.stored_results()).fetchall()]

    return values

""" Here to execute stored procedure with no return"""
def exec_storedProc(storedproc):
    cnx = mysql.connector.connect(user='Ryan', password='!bsodjaja9112',
                              host='159.203.19.40', database='C43')
    cursor = cnx.cursor()
    
    cursor.callproc(storedproc)
    cnx.commit()
    return ;

def exec_storedProc(storedproc, args):
    cnx = mysql.connector.connect(user='Ryan', password='!bsodjaja9112',
                                  host='159.203.19.40', database='C43')
    cursor = cnx.cursor()
        
    cursor.callproc(storedproc, args)
    cnx.commit()
    return;    