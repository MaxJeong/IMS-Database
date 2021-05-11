USE C43;

Create OR replace view `V_PurchaseOrderDetails` As

Select PO.po_id AS ID,
		PO.Description,
        PO.Name,
        PO.Price,
        PO.PurchaseDate,
        PO.Quantity,
        Supp.Address,
        Supp.Contact,
        Supp.Phone,
        Supp.Email,
        Supp.PostalCode,
        Comp.Name AS Company,
        Comp.CompanyDivision AS Division,
        Comp.Active,
        Comp.Customer AS Customer,
        Cit.City,
        Cit.Province,
        Cit.Country
from 
	PurchaseOrder PO inner join 
    Supplier Supp
		on Supp.s_id = PO.SupplierID
        inner join
	Company Comp
		on Supp.CompanyID = Comp.co_id
		inner join
	City Cit
		on Comp.CityID = Cit.c_id;
		
Create OR REPLACE view `V_SupplierDetails` As

Select Supp.s_id AS Id,
        Supp.Address,
        Supp.Contact,
        Supp.Phone,
        Supp.Email,
        Supp.PostalCode,
        Comp.Name AS Company,
        Comp.CompanyDivision AS Division,
        Comp.Active,
        Comp.Customer AS Customer,
        Cit.City,
        Cit.Province,
        Cit.Country
from  
    Supplier Supp
        inner join
	Company Comp
		on Supp.CompanyID = Comp.co_id
		inner join
	City Cit
		on Comp.CityID = Cit.c_id;

Create OR REPLACE view `V_AssetDetails` As

Select Ass.a_id As ID,
		Ass.Name,
		Ass.ArrivalDate,
        Ass.InitalCost,
        Ass.CurrentValue,
        ATyp.at_id AS ATID,
        ATyp.DepreciationRate AS Rate,
        ATyp.DepreciationInterval AS 'Interval',
        ATyp.TypeName As 'Type',
        ATyp.SubType AS 'SubType',
		Pos.ID AS POID,
        Pos.Company,
        Pos.Division,
        Pos.PurchaseDate,
        Pos.Name As PurchaseOrder,
        Pos.Description
from  
    Assets Ass
        inner join
	AssetType ATyp 
		On ATyp.at_id = Ass.ATID
        inner join
	V_PurchaseOrderDetails Pos
		on Ass.POID = Pos.ID;
    USE C43;    
Create OR REPLACE view `V_PendingPurchaseOrders` As

Select  PO.ID,
		PO.Description,
        PO.Name,
        PO.Price,
        PO.PurchaseDate,
        PO.Quantity,
        PO.Address,
        PO.Contact,
        PO.Phone,
        PO.Email,
        PO.PostalCode,
        PO.Company,
        PO.Division,
        PO.Active,
        PO.Customer,
        PO.City,
        PO.Province,
        PO.Country,
        Count(Ass.ID) As 'ArrivedCount'
From  
	V_AssetDetails Ass
	inner join 
		V_PurchaseOrderDetails PO on
			Ass.POID = PO.ID
Group by PO.ID
HAVING Count(Ass.ID) < PO.Quantity;