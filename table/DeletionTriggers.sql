USE C43;

DELIMITER $$
DROP TRIGGER IF EXISTS rowDeletionAT $$
CREATE TRIGGER rowDeletionAT
BEFORE DELETE
ON AssetType
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Assets Ass
			where OLD.at_id = Ass.ATID) > 0) THEN -- Abort when trying to remove this record
		 CALL cannot_delete_error;
  END IF;
END
$$

DELIMITER ;

DELIMITER $$
DROP TRIGGER IF EXISTS rowDeletionA $$
CREATE TRIGGER rowDeletionA
BEFORE DELETE
ON PurchaseOrder
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Assets Ass
			where OLD.po_id = Ass.POID) > 0) THEN -- Abort when trying to remove this record
		 CALL cannot_delete_error;
  END IF;
END
$$

DELIMITER ;

DELIMITER $$
DROP TRIGGER IF EXISTS rowDeletionS $$
CREATE TRIGGER rowDeletionS
BEFORE DELETE
ON Supplier
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from PurchaseOrder PO
			where OLD.s_id = PO.SupplierID) > 0) THEN -- Abort when trying to remove this record
		 CALL cannot_delete_error;
  END IF;
END
$$

DELIMITER ;

DELIMITER $$
DROP TRIGGER IF EXISTS rowDeletionCo $$
CREATE TRIGGER rowDeletionCo
BEFORE DELETE
ON Company
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Supplier Supp
			where OLD.co_id = Supp.CompanyID) > 0) THEN -- Abort when trying to remove this record
		 CALL cannot_delete_error;
  END IF;
END $$

DELIMITER ;

DELIMITER $$
DROP TRIGGER IF EXISTS rowDeletionCi $$
CREATE TRIGGER rowDeletionCi
BEFORE DELETE
ON City
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Supplier Supp
			where OLD.c_id = Supp.CityID) > 0) or
	((select count(*) 
			from Company Comp
			where OLD.c_id = Comp.CityID) > 0)  THEN -- Abort when trying to remove this record
				 CALL cannot_delete_error;
  END IF;
END
$$

DELIMITER ;