Use C43;
Drop Table IF EXISTS `Assets`;

Drop Table IF EXISTS `PurchaseOrder`;

Drop Table IF EXISTS `Supplier`;

Drop Table IF EXISTS `Company`;

Drop Table IF EXISTS `City`;

Drop Table IF EXISTS `AssetType`;

Create Table IF NOT EXISTS City(
	c_id int Primary Key AUTO_INCREMENT,
	City varchar(40),
	Province varchar(40),
	Country varchar(40)
) ENGINE = INNODB;


Create Table IF NOT EXISTS Company(
	co_id int Primary Key AUTO_INCREMENT,
	Name varchar(60) Not Null,
	CompanyDivision varchar(20),
	Active boolean,
	Customer boolean,
	CityID int,
    foreign key(CityID) references City(c_id)
) ENGINE = INNODB;


Create Table IF NOT EXISTS Supplier(
	s_id int Primary Key AUTO_INCREMENT,
	CompanyID int,
	Address varchar(60),
	Phone char(30),
	Email varchar(60),
	PostalCode char(8),
	Contact varchar(60),
	CityID int,
    foreign key(CityID) references City(c_id),
    foreign key(CompanyID) references Company(co_id)
) ENGINE = INNODB;


Create Table IF NOT EXISTS PurchaseOrder(
	po_id int Primary Key AUTO_INCREMENT, 
	Quantity int,
	Price real,
	PurchaseDate DATE,
 	Name varchar(60) Not Null , 
 	Description varchar(600),
    SupplierID int,
    foreign key(SupplierID) references Supplier(s_id)
) ENGINE = INNODB;

Create Table IF NOT EXISTS AssetType(
	at_id int Primary Key AUTO_INCREMENT,
	TypeName varchar(60) Not Null,
	SubType varchar(60) Not Null,
	DepreciationRate real DEFAULT 0.00,
	DepreciationInterval real DEFAULT 0.00
) ENGINE = INNODB;


Create Table IF NOT EXISTS Assets(
	a_id int Primary Key AUTO_INCREMENT, 
	ATID int,
 	Name varchar(60) Not Null , 
 	InitalCost real DEFAULT 0.00, 
    CurrentValue real DEFAULT 0.00,
 	ArrivalDate DATETIME,
 	POID int,
    foreign key(POID) REFERENCES PurchaseOrder(po_id),
    foreign key(ATID) REFERENCES AssetType(at_id)
) ENGINE = INNODB;


/*

Create Table IF NOT EXISTS Account(
	ac_id int Primary Key AUTO_INCREMENT,
	Credit boolean,
	AccountNumber int,
	Value real,
	ExpiryDate DATE,
	Active char,
	Code int,
	CompanyID int,
	Description varchar(600)
) ENGINE = INNODB;
Create Table IF NOT EXISTS Transaction(
	t_id int Primary Key AUTO_INCREMENT,
	DateOfPurchase DATE,
	Value real,
	AccountID int,
	DebitOrCredit boolean,
	foreign key(POID) REFERENCES PurchaseOrder(po_id)
) ENGINE = INNODB; */

