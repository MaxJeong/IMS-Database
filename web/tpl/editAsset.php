<!DOCTYPE html>
<html lang="en">
  <head>

    <!-- set charset to interpret file contents -->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- title displayed when browser tab is moused over -->
    <title>Skytrin</title>
    <!-- ensure proper rendering and touch zooming -->
    
    <!-- Bootstrap CSS definitions -->
    
    <!-- your own customized style rules -->
		  
    <!-- library scripts you use -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
    
  </head>

 <body>
<a href="../index.php#search" style="background-color: green; padding: 5px; color: white;" value="HOME">HOME</a>
<?php
// ----------------------------------------------------------------------------------------------------
// - Display Errors
// ----------------------------------------------------------------------------------------------------
ini_set('display_errors', 'On');
ini_set('html_errors', 0);
// ----------------------------------------------------------------------------------------------------
// - Error Reporting
// ----------------------------------------------------------------------------------------------------
error_reporting(-1);
// ----------------------------------------------------------------------------------------------------
// - Shutdown Handler
// ----------------------------------------------------------------------------------------------------
function ShutdownHandler()
{
    if(@is_array($error = @error_get_last()))
    {
        return(@call_user_func_array('ErrorHandler', $error));
    };
    return(TRUE);
};
register_shutdown_function('ShutdownHandler');
// ----------------------------------------------------------------------------------------------------
// - Error Handler
// ----------------------------------------------------------------------------------------------------
function ErrorHandler($type, $message, $file, $line)
{
    $_ERRORS = Array(
        0x0001 => 'E_ERROR',
        0x0002 => 'E_WARNING',
        0x0004 => 'E_PARSE',
        0x0008 => 'E_NOTICE',
        0x0010 => 'E_CORE_ERROR',
        0x0020 => 'E_CORE_WARNING',
        0x0040 => 'E_COMPILE_ERROR',
        0x0080 => 'E_COMPILE_WARNING',
        0x0100 => 'E_USER_ERROR',
        0x0200 => 'E_USER_WARNING',
        0x0400 => 'E_USER_NOTICE',
        0x0800 => 'E_STRICT',
        0x1000 => 'E_RECOVERABLE_ERROR',
        0x2000 => 'E_DEPRECATED',
        0x4000 => 'E_USER_DEPRECATED'
    );
    if(!@is_string($name = @array_search($type, @array_flip($_ERRORS))))
    {
        $name = 'E_UNKNOWN';
    };
    return(print(@sprintf("%s Error in file \xBB%s\xAB at line %d: %s\n", $name, @basename($file), $line, $message)));
};
$old_error_handler = set_error_handler("ErrorHandler");
// other php code
?>
<!-- <form action="./tpl/table.php" method = "POST">
SQL:command:
<input type= "text" name="query">
<input type= "submit"> 
</form>
 -->

<?php
    // print_r($_REQUEST);
    $update = FALSE;
    $delete = FALSE;
	$idVal = htmlspecialchars($_GET["id"]);
	$table = "getAsset";
	$query ="Call $table('$idVal')";
	print_r($query);
    
    // echo (!isset($query)|| is_null($query))? "Select * from City" : $query;
    # code...
    include 'config.php';
    // $q = $_SERVER['QUERY_STRING'];
    // $q = $_GET['query'];
    // print_r($q);
    # connect to mysql database on mathlab server
    try {
        $conn = new PDO("mysql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        // echo "Connected successfully"; 
        }
    catch(PDOException $e)
        {
        echo "Connection failed: " . $e->getMessage();
        }
        # gets column names
    // $result = $conn->query($q);
    $result = $conn->query($query);
    for ($i = 0; $i<$result->columnCount();$i++){
        $col = $result->getColumnMeta($i);
        $columns[]=$col["name"];
    }
    ?>
    <table>
     <tr>
        <?php
            # print out column names
            foreach ($columns as $name ) {
                ?>
                    <td><?= $name?> </td>
                <?php
            }
        ?>
     </tr>

     <?php
        //require or double output shows up
        $r = $result->fetchAll(PDO::FETCH_NUM);
        foreach ($r as $row) {
            #generate table row
            // print_r($r);
            // print_r($row);
        ?>
        
        <tr>
            <?php
            foreach ($row as $val) {
                ?>
                    <td> <input type="text" value="<?=$val?>">  </td>
                <?php
            }
            ?>
            
        </tr>
        
		
        <?php
        }
     ?>

    </table>
	<a onclick="myAjax()" style="background-color: green; padding: 5px; color: white;" value="Save" name="save">Save</a>
	<script type="text/javascript">
	function myAjax() {
      $.ajax({
           type: "POST",
           url: 'ajax.php',
           data:{action:'call_this'},
           success:function(html) {
             alert(html);
           }

      });
 }
	</script>
	</body>
	</html>