// catch simple errors
"use strict";

// declare splat-app namespace, if it doesn't already exist
var splat = splat || {};

splat.utils = {

    // Asynchronously load templates located in separate .html files using
    // jQuery "deferred" mechanism, an implementation of Promises.  Note we
    // depend on template file names matching corresponding View file names,
    // e.g. Home.html and home.js which defines Backbone View "Home".
    /*
     * @param {[String]} views:  filenames of templates to be loaded
     * @param {function} callback:  callback function invoked when file is loaded
     */
    loadTemplates: function(views, callback) {

	// Array of deferred actions to keep track of template load status
        var deferreds = [];

	// Process each template-file in views array
        /*
         * @param {[integer]} index:  position of view template within views array
         * @param {[String]} view:  root name (w/o .html) of view template file
         */
        $.each(views, function(index, view) {
	    // If an associated Backbone view is defined, set its template function
            if (splat[view]) {

		// Push task of retrieving template file into deferred array.
		// Task performs "get" request to load the template, then passes
		// resulting template data to anonymous function to process it.
	        /*
	         * @param {String} data:  HTML from template file as String
	         */
                deferreds.push($.get('tpl/' + view + '.php', function(data) {
	    	    // Set template function on associated Backbone view.
                    splat[view].prototype.template = _.template(data);
                }));

	    // No Backbone view file is defined; cannot set template function.
            } else {
                console.log(view + " not found");
            }
        });

	// When all deferred template-loads have completed,
	// invoke callback function.
        $.when.apply(null, deferreds).done(callback);
    },

    showNotice:function(alertType, message){
        var legal = ['danger','success','info'];

        var notify = $("#notification");

        console.log(notify);
        if ($.inArray(alertType,legal) && message){
            var alert = 'alert-'+alertType;
            console.log(alert);
            notify.html(message);
            notify.removeClass();
            notify.addClass(alert);
            notify.show();
            notify.fadeOut(5000);
            
            console.log('notification set');
        }else{
            console.log('improper status');
        }

    },
    
    hideNotice:function(){

    },

    //item is jquery object, msg is string
    showValidationNotice:function(item,msg){
        //item append, dive with 'msg'
        console.log(item.parent());
        console.log(item);
        var name = item.attr('name') + 'valid';
        var super_msg = $.parseHTML("<div id = "+name +" class= 'error' >" +msg+"</div>");
        $(item.parent()).addClass('color-change');
        $(item).addClass('border-change');
        console.log(item.parent());
        console.log(item);
        item.parent().append(super_msg);
    },

    hideValidationNotice:function(item){
        var name = '#' + item.attr('name') + 'valid';
        // console.log('name',name);
        // console.log('jquery',$(name));
        $(item.parent()).removeClass('color-change');
        $(item).removeClass('border-change');
        $(name).remove();
    },

};