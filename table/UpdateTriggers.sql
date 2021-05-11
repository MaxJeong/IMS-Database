USE C43;

DELIMITER $$

CREATE TRIGGER rowUpdateA
BEFORE update
ON Assets
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from PurchaseOrder PO
			where NEW.POID = PO.po_id) = 0) OR
		((select count(*) 
			from AssetType AssT
			where AssT.at_id = NEW.ATID) = 0) THEN -- Abort when trying to insert this record
		 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Error';
  END IF;
END
$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER rowUpdateP
BEFORE UPDATE
ON PurchaseOrder
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Supplier Supp
			where New.SupplierID = Supp.s_id) = 0) THEN -- Abort when trying to insert this record
		 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Error';
  END IF;
END
$$

DELIMITER $$

CREATE TRIGGER rowUpdateS
BEFORE UPDATE
ON Supplier
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from Company Co
			where Co.co_id = NEW.CompanyID) = 0) OR
	((select count(*) 
			from City Cit
			where Cit.c_id = NEW.CityID) = 0) THEN -- Abort when trying to insert this record
		 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Error';
  END IF;
END
$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER rowUpdateCo
BEFORE UPDATE
ON Company
FOR EACH ROW
BEGIN
  IF ((select count(*) 
			from City Cit
			where Cit.c_id = NEW.CityID) = 0)  THEN -- Abort when trying to remove this record
				 SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Update Error';
  END IF;
END
$$

DELIMITER ;