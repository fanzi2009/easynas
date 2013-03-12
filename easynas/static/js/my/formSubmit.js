define(["dojo/request","dojo/_base/event","dojo/query","dojo/dom-style","dijit/registry","dojo/dom","dojo/dom-form","dojo/store/JsonRest"], function(request,dEvent,query,domStyle,registry,dom,domForm,JsonRest){
    formSubmit = function(dialog_id) {
		myJson = {}
		myJson['volume_name'] = domForm.fieldToObject("id_volume_name");
		disks = domForm.fieldToObject("id_disks");
		myJson['disks'] = domForm.fieldToObject("id_disks").join(',');

		registry.byId("basicStandby1").show();
		registry.byId(dialog_id).hide();

		var store = new JsonRest({
		    target: "/easynas/zpools"
		});

		store.put(myJson);
		location.reload();
    }
	return formSubmit;
});