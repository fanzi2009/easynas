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
		},

    formSubmit = function(item, e, url, callback, attrs) {
        dEvent.stop(e); // prevent the default submit
        if(!attrs) {
            attrs = {};
        }
        var qry = query('.saved', item.domNode)[0];
        if(qry) domStyle.set(qry, 'display', 'none');

        query('input[type=button],input[type=submit]', item.domNode).forEach(
          function(inputElem){
               if(inputElem.type == 'submit') {
                   var dj = registry.getEnclosingWidget(inputElem);
                   if(dj) {
                       if(dj.isInstanceOf(dojox.form.BusyButton)) {
                           dj.busyLabel = 'Please wait...';
                       } else {
                           domAttr.set(dj.domNode, "oldlabel", dj.get('label'));
                           dj.set('label', gettext('Please wait...'));
                       }
                   }
               }
               registry.getEnclosingWidget(inputElem).set('disabled',true);
           }
        );

        var rnode = getDialog(item);
        if(!rnode) rnode = registry.getEnclosingWidget(item.domNode.parentNode);
        if(!rnode) rnode = registry.byId("edit_dialog");

        var loadOk = function(data) {

            try {
                var json = JSON.parse(data);
                // TODO, workaound for firefox, it does parse html as JSON!!!
                if(json.error != true && json.error != false) {
                    throw "not json"
                }

                try {
                    rnode.hide();
                } catch(err2) {
                    query('input[type=button],input[type=submit]', item.domNode).forEach(
                      function(inputElem){
                           registry.getEnclosingWidget(inputElem).set('disabled',false);
                       }
                    );
                    var sbtn = registry.getEnclosingWidget(query('input[type=submit]', item.domNode)[0]);
                    if(domAttr.has(sbtn.domNode, "oldlabel")) {
                        sbtn.set('label', domAttr.get(sbtn.domNode, "oldlabel"));
                    } else {
                        sbtn.set('label', 'Save');
                    }
                    if(sbtn.isInstanceOf(BusyButton)) sbtn.resetTimeout();
                }
                if(json.error == false){
                    query('ul[class=errorlist]', rnode.domNode).forEach(function(i) { i.parentNode.removeChild(i); });
                }

                setMessage(json.message);
                if(json.events) {
                    for(i=0;json.events.length>i;i++){
                        try {
                            eval(json.events[i]);
                        } catch (e) {
                            console.log(e);
                        }
                    }
                }
            } catch(err) {

                rnode.set('content', data);
                try {
                    if(callback) callback();
                    var qry = query('#success', rnode.domNode);
                    if(qry.length>0)
                        dFx.fadeOut({node: rnode, onEnd: function() { rnode.hide(); }}).play();
                } catch(err) {}
            }
        };
		

	});
});
