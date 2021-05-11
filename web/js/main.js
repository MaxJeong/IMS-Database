// catch simple errors
"use strict";

// declare splat-app namespace if it doesn't already exist
var splat = splat || {};

// Define Backbone router
splat.AppRouter = Backbone.Router.extend({

    // Map "URL paths" to "router functions"
    routes: {
        "": "home",
        "about": "about",
        "sql": "sqlLoad",
        "custom_sql":"sql_custom",
        "search":"search"
    },

    // When an instance of an AppRouter is declared, create a Header view
    initialize: function() {
        // instantiate a Header view
        this.headerView = new splat.Header();  
        // insert the rendered Header view element into the document DOM
        $('.header').html(this.headerView.render().el);
        //create collection and retreive values
        splat.collection = new splat.Movies();
        splat.collection.fetch();
    },

    search: function(){
        if (!this.searchView) {
            this.searchView = new splat.Search();
        };

        //highlights item in headerView
        this.headerView.selectMenuItem('.search');
        // insert the rendered Home view element into the document DOM
        $('#content').html(this.searchView.render().el);

    },

    sql_custom: function () {

        if (!this.sqlCustomView) {
            this.sqlCustomView = new splat.customSql();
        };

        //highlights item in headerView
        this.headerView.selectMenuItem('.sql-custom');
        // insert the rendered Home view element into the document DOM
        $('#content').html(this.sqlCustomView.render().el);

      
    },

        sqlLoad: function(blah) {
        // If the sql view doesn't exist, instantiate one
        if (!this.sqlView) {
            this.sqlView = new splat.Sql();
        };

        //highlights item in headerView
        this.headerView.selectMenuItem('.sql-menu');
        if (blah){
            blah = blah.replace("'","");
            window.location.href = "tpl/Sql.php?"+blah;
        };
        
        // insert the rendered Home view element into the document DOM
        $('#content').html(this.sqlView.render().el);
    },

    //load home view, and select the nav bar
    home: function() {
	// If the Home view doesn't exist, instantiate one
        if (!this.homeView) {
            this.homeView = new splat.Home();
        };

        //highlights item in headerView
        this.headerView.selectMenuItem('.home-menu');
	    // insert the rendered Home view element into the document DOM
        $('#content').html(this.homeView.render().el);
    },

    //load about and select about button
    about: function() {
        //check if already created
        if (!this.aboutView) {
            this.aboutView = new splat.About();
        };
        //highlights item in headerView        
        this.headerView.selectMenuItem('.about-menu');
    // insert the rendered Home view element into the document DOM
        $('#content').html(this.aboutView.render().el);
    }
    
});

// Load HTML templates for Home, Header, About views, and when
// template loading is complete, instantiate a Backbone router
// with history.
splat.utils.loadTemplates(['Home', 'Header', 'About','Sql','customSql','Search'], function() {
    splat.app = new splat.AppRouter();
    Backbone.history.start();
    // console.log('asdfasdf');
});
