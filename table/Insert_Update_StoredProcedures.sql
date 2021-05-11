use C43;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setPurchaseOrder` $$
Create Procedure setPurchaseOrder
(IN id int,
 IN nam varchar(60),
 IN price real,
 IN pdate DateTime,
 in descript varchar(600),
 IN quant int,
 IN supp int)
Begin
	if id <= 0 OR (id IS NULL) THen
		INSERT INTO PurchaseOrder (Name, Price, PurchaseDate, Description, Quantity, SupplierID) Values	(nam, price, pdate, descript, quant, supp);
    ELSE 
		Update PurchaseOrder P
        Set Name = nam, Price = price, PurchaseDate = pdate, Description =descript, Quantity = quant, SupplierID = supp
        WHERE po_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setAsset` $$
Create Procedure setAsset
(IN id int,
 IN nam varchar(60),
 IN price real,
 IN adate DateTime,
 IN po int,
 IN at_Id int)
Begin
	if id <= 0 OR (id IS NULL) THen
		INSERT INTO Assets (Name, InitalCost, CurrentValue, ArrivalDate, POID, ATID) 
			Values	(nam, price, price, adate, po, at_Id );
    ELSE 
		Update Assets A
        Set Name = nam, POID = po, ArrivalDate = adate, CurrentValue =price, ATID = at_Id
        WHERE a_id = id;
	END IF;
END $$
Delimiter ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setSupplier` $$
Create Procedure setSupplier
(IN id int,
 IN company int,
 IN contaxt varchar(120),
 IN postCode char(8),
 IN email varchar(80),
 IN phone varchar(18),
 IN address varchar(100))
Begin
	if id <= 0 OR (id IS NULL) Then
		INSERT INTO Supplier (CompanyID, Address, Phone, Email, PostalCode, Contact) Values	(company, address, phone, email, postCode, contaxt);
    ELSE 
		Update Supplier
        Set CompanyID = company, Address = address, Phone = phone, email =email, PostalCode = postCode, Contact = Contaxt
        WHERE s_id = id;
	END IF;
End $$

DELIMITER ;

USE C43;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setCity` $$
Create Procedure setCity
(IN id int,
 IN cty varchar(100),
 IN prov varchar(100),
 IN ctry varchar(100))
Begin
	if id <= 0 OR (id IS NULL) Then
		INSERT INTO City (City, Province, Country) Values(cty, prov, ctry);
    ELSE 
		Update City
        Set City = cty, Province = prov, Country = ctry
        WHERE c_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setCompany` $$
Create Procedure setCompany
(IN id int,
 IN nme varchar(60),
 IN division varchar(20),
 IN Active boolean,
 IN customer boolean,
 IN city int)
Begin
	if id <= 0 OR (id IS NULL) Then
		INSERT INTO Company (Name, CompanyDivision, Active, Customer, CityID) Values(nme, division, Active, customer, city);
    ELSE 
		Update Company
        Set Name = nme, CompanyDivision = division, Active = Active, Customer = customer, CityID = city
        WHERE co_id = id;
	END IF;
End $$

DELIMITER ;

DELIMITER $$
DROP PROCEDURE IF EXISTS `setAssetType` $$
Create Procedure setAssetType
(IN id int,
 IN nam varchar(60),
 IN subTyp varchar(60),
 IN rate real,
 IN intrvl real)
Begin
	if id <= 0 OR (id IS NULL) THen
		INSERT INTO AssetType (TypeName, SubType, DepreciationRate, DepreciationInterval) 
			Values	(nam, subTyp, rate, intrvl);
    ELSE 
		Update AssetType A
        Set TypeName = nam, SubType = subTyp, DepreciationRate = rate, DepreciationInterval = intrvl
        WHERE at_id = id;
	END IF;
END $$
Delimiter ;