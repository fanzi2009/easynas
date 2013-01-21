// dojo/_base/declare and dijit/Dialog are loaded from CDN
define([ "dojo/_base/declare", "dijit/Dialog","dojo/_base/lang" ], function(declare, Dialog, lang){
	// declare our custom class
	return declare(null, {
		constructor: function(){
		},
		
		mytest1: function(str){
			console.log(str);
		},

		myDialog : function(){

		},

		commonDialog : function(attrs) {
			canceled = false;
			dialog = new Dialog({
				id: attrs.id,
				title: attrs.name,
				href: attrs.url,
				parseOnLoad: true,
				closable: true,
				style: attrs.style,
				onHide: function() {
					setTimeout(lang.hitch(this, function() {
						this.destroyRecursive();
					}), 200);

					refreshTabs(attrs.nodes);
				},
				onLoad: function() {
					processStack();
					//this.layout(); // dojo 1.7
					this._position(); // dojo 1.8
				}
			});
			if(attrs.onLoad) {
				f = lang.hitch(dialog, attrs.onLoad);
				f();
			}
			dialog.show();
		},

		volumeWizard : function(name, url, nodes) {
			this.commonDialog({
				id: "wizard_dialog",
				style: "max-width: 650px;min-height:200px;max-height:500px;background-color:white;overflow:auto;",
				name: name,
				url: url,
				nodes: nodes
				});
		}

	});
});