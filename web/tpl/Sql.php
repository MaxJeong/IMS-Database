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
    if (isset($_REQUEST['entity']) and isset($_REQUEST['id'])  ){
        $id = $_REQUEST['id'];
        $entity = $_REQUEST['entity'];
        $query = "CALL $entity('$id')";
    }else{

        if (isset($_REQUEST['table'])){
            if ($_REQUEST['table'] === "Supplier"){
                $table = "Search_Suppliers";
                $entity = "remSupplier";
            }
            if ($_REQUEST['table'] === "POD"){
                $table = "Search_PODetail";
                $entity = "remPurchaseOrder";
            }
            if ($_REQUEST['table'] === "Assets"){
                $table = "Search_Assets";
                $entity = "remAssets";
            }
            $key = $_REQUEST['keyword'];
            $update = TRUE;
            $delete = TRUE;

            $query = "CALL $table('$key')";
            print_r($query);
        }else{
            if (isset($_REQUEST['query'])){
                $query = $_REQUEST['query'];
                print_r($query);
            }else{
                $query = "Select * from Assets";
                // $query = ""
            }
            
        }
    }

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
    if (!isset($_REQUEST['delete'])){
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
        <form name="<?=$row[0]?>" action="Sql.php" method="POST" >
        <tr>
            <?php
            foreach ($row as $val) {
                ?>
                    <td> <input type="text" value="<?=$val?>">  </td>
                <?php
            }


            ?>
            <?php
            if ($update or $delete){
                ?>
                <td> 
                    <input type="hidden" value="<?=$row[0]?>" name="id">
                    <input type="hidden" value="<?=$entity?>" name="entity">
                <?php
                if ($update){ ?>
                    <!-- <input type="submit" value="Save" name ="save"> -->
                <?php }
                if ($delete){ ?>
                    <input type="submit" value="Delete" name = "delete">
                <?php } ?>

                </td>
                <?php
            }
            ?>
        </tr>
        </form>
        <?php
        }
     ?>

    </table>

<?php

    }
    ?>
