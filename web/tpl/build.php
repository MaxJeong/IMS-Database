<?php
// $var = $_GET[''];
// print_r($_REQUEST);
if ($_REQUEST['table'] === "Supplier"){
	$table = "Search_Suppliers";
}
if ($_REQUEST['table'] === "POD"){
	$table = "Search_PODetail";
}
if ($_REQUEST['table'] === "Assets"){
	$table = "Search_Assets";
}
$key = $_REQUEST['keyword'];

$query = "CALL $table($key)";
// print_r($query);

// $url = 'Sql.php';
// $data = array('query' => '$query');

// // use key 'http' even if you send the request to https://...
// $options = array(
//     'http' => array(
//         'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
//         'method'  => 'POST',
//         'content' => http_build_query($data)
//     )
// );
// $context  = stream_context_create($options);
// $result = file_get_contents($url, false, $context);
// if ($result === FALSE) { /* Handle error */ }

// var_dump($result);
// 		));
?>