use C43;

DELIMITER $$
DROP PROCEDURE IF EXISTS `supplierDeliveryRanking` $$
Create Procedure supplierDeliveryRanking
()
Begin
	Select Supp.Id,
		
        Supp.Address,
        Supp.Contact,
        Supp.Phone,
        Supp.Email,
        Supp.PostalCode,
        Supp.Company,
        Supp.Division,
        Supp.Active,
        Supp.Customer,
        Supp.City,
        Supp.Province,
        Supp.Country,
		avg((Ass.ArrivalDate,Ass.PurchaseDate) * 24*60*60) As AvgDelivTime,
        avg(Pend.Quantity - Pend.ArrivedCount) As AvgSuccess
    From V_SupplierDetails Supp
    inner join
		PurchaseOrder PO
        on PO.SupplierID = Supp.Id
		inner join V_AssetDetails Ass
			On PO.po_id = Ass.POID
		Left join V_PendingPurchaseOrders Pend
			ON Pend.ID = PO.po_id
	Group BY Supp.Id
    ORDER BY  AvgDelivTime, AvgSuccess
;
End $$