// dojo/_base/declare and dijit/Dialog are loaded from CDN
define([ "dojo/_base/declare", "dijit/Dialog" ], function(declare, Dialog){
	// declare our custom class
	return declare(null, {
		constructor: function(){
		},
		
		mytest1: function(str){
			console.log(str);
		}

	});
});