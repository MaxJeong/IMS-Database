use C43;

DELIMITER $$
DROP PROCEDURE IF EXISTS `getPurchaseOrder` $$
Create Procedure getPurchaseOrder
(IN id int)
Begin
	Select * from V_PurchaseOrderDetails Pos
    where Pos.ID = id;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `getAsset` $$
Create Procedure getAsset
(IN id int)
Begin
	Select * from V_AssetDetails Ass
    where Ass.ID = id;
End $$
Delimiter ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `getSupplier` $$
Create Procedure getSupplier
(IN id int)
Begin
	Select * from V_SupplierDetails Supp
    where Supp.Id = id;
End $$

DELIMITER ;
USE C43;
DELIMITER $$
DROP PROCEDURE IF EXISTS `getCity` $$
Create Procedure getCity
(IN id int)
Begin
	Select C.c_id,
			C.City,
			C.Province,
			C.Country
	From City C
    where C.c_id = id;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `getCompany` $$
Create Procedure getCompany
(IN id int)
Begin
	Select C.co_id,
			C.Name,
			C.CompanyDivision,
			C.Active,
            C.Customer,
            C.CityID
	From Company C
    where C.co_id = id;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `getAssetType` $$
Create Procedure getAssetType
(IN id int)
Begin
	Select ATyp.at_id As 'ID',
		ATyp.TypeName As 'Name',
        ATyp.SubType As 'SubType',
        ATyp.DepreciationRate As 'Rate',
        ATyp.DepreciationInterval As 'Interval'
    from AssetType ATyp
    where ATyp.at_id = id;
End $$
Delimiter ;