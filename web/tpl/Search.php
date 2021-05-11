
<div class = "about-hero">
	Search by keyword in:
	<form  action="tpl/Sql.php" method="POST" >

		<select name="table">
			<option  value="POD" >Purchase Order Details</option>
			<option value="Assets" >Asset Details</option>
			<option selected="selected" value="Supplier" >Suppiler Details</option>
		</select>

		<input type="text" name="keyword">
	</form>
</div>