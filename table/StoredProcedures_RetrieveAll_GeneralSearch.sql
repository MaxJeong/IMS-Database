use C43;

/********************************************************
Grab Information From Views Stored Procedures
********************************************************/
DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getPODetail` $$
Create Procedure All_getPODetail
()
Begin
	Select * from V_PurchaseOrderDetails;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getAssets` $$
Create Procedure All_getAssets
()
Begin
	Select * from V_AssetDetails;
End $$
Delimiter ;


DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getSuppliers` $$
Create Procedure All_getSuppliers
()
Begin
	Select * from V_SupplierDetails;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getCities` $$
Create Procedure All_getCities
()
Begin
	Select 
			C.c_id As ID,
			C.City As City,
			C.Province As Province,
			C.Country As Country
	From City C;
End $$

DELIMITER ;
USE C43;
DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getActiveCompanies` $$
Create Procedure All_getActiveCompanies
()
Begin
	Select 
			C.co_id As 'Company ID',
			C.Name As 'Company Name',
            C.CompanyDivision AS Division,
			Ci.City As 'City Name'
	From Company C inner join City Ci on C.CityID = Ci.c_id
    Where C.Active = 1;
End $$

DELIMITER ;

USE C43;
DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getCompanies` $$
Create Procedure All_getCompanies
()
Begin
    Select 
            C.co_id As 'Company ID',
            C.Name As 'Company Name',
            C.CompanyDivision AS Division,
            Ci.City As 'City Name'
    From Company C inner join City Ci on C.CityID = Ci.c_id
    Order By C.co_id ASC;
End $$

DELIMITER ;

USE C43;
DELIMITER $$
DROP PROCEDURE IF EXISTS `All_getAssetTypes` $$
Create Procedure All_getAssetTypes
()
Begin
    Select 
            ATyp.at_id As 'Asset Type ID',
            ATyp.TypeName As 'Name',
            ATyp.SubType AS SubType,
            ATyp.DepreciationRate,
            ATyp.DepreciationInterval
    From AssetType ATyp
    Order By ATyp.at_id ASC;
End $$

DELIMITER ;

/********************************************************
General Search Stored Procedures
********************************************************/

DELIMITER $$
DROP PROCEDURE IF EXISTS `Search_PODetail` $$
Create Procedure Search_PODetail
(IN search varchar(1024)) /* Typically users don't enter too many words/terms*/
Begin
	Select * from V_PurchaseOrderDetails Pos
    where 
		Pos.Name LIKE CONCAT('%', search , '%') or
        Pos.Description LIKE CONCAT('%', search , '%') or
        Pos.Company LIKE CONCAT('%', search , '%') or
        Pos.Division LIKE CONCAT('%', search , '%') or 
        Pos.City LIKE CONCAT('%', search , '%') or
        Pos.Province LIKE CONCAT('%', search , '%') or
        Pos.Country LIKE CONCAT('%', search , '%');
End $$

DELIMITER ;
USE C43;
DELIMITER $$
DROP PROCEDURE IF EXISTS `Search_Assets` $$
Create Procedure Search_Assets
(IN search varchar(1024))
Begin
	Select * from V_AssetDetails Ass
    where 
		Ass.Name LIKE CONCAT('%', search , '%') or
        Ass.Description LIKE CONCAT('%', search , '%') or
        Ass.Company LIKE CONCAT('%', search , '%') or
        Ass.Division LIKE CONCAT('%', search , '%') or 
        Ass.PurchaseOrder LIKE CONCAT('%', search , '%') or
        Ass.`Type` LIKE CONCAT('%', search , '%') or 
        Ass.SubType LIKE CONCAT('%', search , '%');
End $$

DELIMITER ;


DELIMITER $$
DROP PROCEDURE IF EXISTS `Search_Suppliers` $$
Create Procedure Search_Suppliers
(IN search varchar(1024))
Begin
	Select * from V_SupplierDetails Supp
    where 
        Supp.Company LIKE CONCAT('%', search , '%') or
        Supp.Division LIKE CONCAT('%', search , '%') or
        Supp.City LIKE CONCAT('%', search , '%') or
        Supp.Province LIKE CONCAT('%', search , '%') or
        Supp.Country LIKE CONCAT('%', search , '%') or
        Supp.Address LIKE CONCAT('%', search , '%');
End $$

DELIMITER ;