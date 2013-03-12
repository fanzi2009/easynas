define(["dijit/Dialog","dojo/_base/lang", "dojo/request"], function(Dialog,lang,request){
    commonDialog = function(attrs) {
        canceled = false;

		dialog = new Dialog({
			id: attrs.id,
			title: attrs.name,
			//parseOnLoad: true,
			href: attrs.url,
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

    };
	return commonDialog;
});