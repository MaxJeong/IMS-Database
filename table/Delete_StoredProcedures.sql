use C43;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remAsset` $$
Create Procedure remAsset
(IN id int)
Begin
	if id > 0 AND (NOT (id IS NULL)) AND ((select count(*) from Assets ass where ass.a_id = id) > 0) THen
		DELETE FROM Assets WHERE Assets.a_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remSupplier` $$
Create Procedure remSupplier
(IN id int)
Begin
	if 	id > 0 AND 
		(NOT (id IS NULL)) AND 
		((select count(*) 
        from Supplier sup
			inner join PurchaseOrder PO 
				on PO.SupplierID = sup.id where sup.s_id = id) = 0)
	THen
		DELETE FROM Supplier WHERE Supplier.s_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remPurchaseOrder` $$
Create Procedure remPurchaseOrder
(IN id int)
Begin
	if 	id > 0 AND 
		(NOT (id IS NULL)) AND 
        ((select count(*) 
			from PurchaseOrder PO
				inner join Assets ass
					on PO.po_id = ass.POID
			where PO.po_id = id) = 0)
	THen
		DELETE FROM PurchaseOrder WHERE PurchaseOrder.po_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remCompany` $$
Create Procedure remCompany
(IN id int)
Begin
	if 	id > 0 AND 
		(NOT (id IS NULL)) AND 
        ((select count(*) 
			from Company Comp
				inner join Supplier supp
					on Comp.co_id = supp.CompanyID
			where Comp.co_id = id) = 0)
	THen
		DELETE FROM Company WHERE Company.co_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remCity` $$
Create Procedure remCity
(IN id int)
Begin
	if 	id > 0 AND 
		(NOT (id IS NULL)) AND 
        ((select count(*) 
			from City Ci
				inner join Company comp
					on Ci.c_id = comp.co_id
			where Ci.c_id = id) = 0) AND
		((select count(*) 
			from City Ci
				inner join Supplier supp
					on supp.s_id = Ci.c_id
			where Ci.c_id = id) = 0)
	THen
		DELETE FROM City WHERE City.c_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `remAssetType` $$
Create Procedure remAssetType
(IN id int)
Begin
	if 	id > 0 AND 
		(NOT (id IS NULL)) AND 
        ((select count(*) 
			from AssetType ATyp
				inner join Assets Ass
					on ATyp.at_id = Ass.ATID
			where ATyp.at_id = id) = 0)
	THen
		DELETE FROM AssetType WHERE AssetType.at_id = id;
	END IF;
End $$

DELIMITER ;