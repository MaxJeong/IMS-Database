<!DOCTYPE html>
<html lang="en">
  <head>

    <!-- set charset to interpret file contents -->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- title displayed when browser tab is moused over -->
    <title>Information Management System</title>
    <!-- ensure proper rendering and touch zooming -->
    
    <!-- Bootstrap CSS definitions -->
    <link href="/css/bootstrap.css" rel="stylesheet">
    <!-- optional stylesheet theme included with Bootstrap -->
    <link href="/css/bootstrap-theme.css" rel="stylesheet">

    <link href="/css/style.css" rel="stylesheet">
    <!-- your own customized style rules -->
  </head>

  <body>
    <!-- HTML5 markup for view content, labelled with Bootstrap class names -->
    <header class="header"></header>

    <!-- full-width content container, spanning entire viewport -->
    <main class="container-fluid">  <!-- Sidebar -->
        
      <!-- row for use in Bootstrap grid layout -->
      <div class="row" id="mainrow">
          
          <div id="content">  <!-- implicitly a single column within row -->
            
          </div>
      </div>  <!-- row -->
    </main>  <!-- container-fluid -->

    <!-- load scripts last for better UI performance -->

    <footer class='footer'>
      <div class='container'>
        <p class="text-muted">Created by: Max Jeong</p>
      </div>
    </footer>

    <!-- library scripts you use -->
    <script src="js/lib/jquery-min.js"></script>
    <script src="js/lib/underscore-min.js"></script>
    <script src="js/lib/backbone-min.js"></script>
    <script src="js/lib/backbone.localStorage.js"></script>
    <script src="js/lib/bootstrap-min.js"></script>

    <script src="js/views/search.js"></script>
    <script src="js/views/customSql.js"></script>
    <script src="js/views/sql.js"></script>
    <script src="js/views/about.js"></script>
    <script src="js/views/header.js"></script>
    <script src="js/views/home.js"></script>

    <script src="js/models/movie.js"></script>
    <script src="js/collections/movies.js"></script>    
    <script src="js/views/movies.js"></script>
    
    <script src="js/views/details.js"></script>

    <!-- scripts you define -->
    <script src="js/utils.js"></script>
    <script src="js/main.js"></script>
  </body>
</html>
