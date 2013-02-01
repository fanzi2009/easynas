define(["dojo/request","dojo/_base/event","dojo/query","dojo/dom-style","dijit/registry","dojo/dom","dojo/dom-form"], function(request,dEvent,query,domStyle,registry,dom,domForm){
    cancelDialog = function(dialog_id) {
		registry.byId(dialog_id).hide();
    }
	return cancelDialog;
});
