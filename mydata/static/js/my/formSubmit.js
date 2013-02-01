define(["dojo/request","dojo/_base/event","dojo/query","dojo/dom-style","dijit/registry","dojo/dom","dojo/dom-form"], function(request,dEvent,query,domStyle,registry,dom,domForm){
    formSubmit = function(dialog_id) {

		registry.byId("basicStandby1").show();

		request.post("/storage/wizard", {
			data: domForm.toObject("formNode"),
			timeout: 2000
		}).then(function(response){
			if(response == "OK")
			{
				registry.byId(dialog_id).hide();
			}else
			{
				registry.byId("basicStandby1").hide();

				dom.byId('error_msg').innerHTML = response;
			}
		});
    }
	return formSubmit;
});
