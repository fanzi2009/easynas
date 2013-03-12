define(["dojo/_base/event","dojo/query","dojo/dom-style","dijit/registry"], function(event,query,domStyle,registry){
    wizardcheckings = function(vol_change, first_load) {

        if(!registry.byId("wizarddisks")) return;
        var add = registry.byId("id_volume_add");
        var add_mode = false;
        if(add && add.get("value") != '') {
            add_mode = true;
        }
        var disks = registry.byId("wizarddisks");
        var d = disks.get('value');
        html.set(dom.byId("wizard_num_disks"), d.length + '');

        var zfs = query("input[name=volume_fstype]")[1].checked || add_mode;

        registry.byId("id_volume_name").set('disabled', add_mode);
        query("input[name=volume_fstype]").forEach(function(item, idx) {
            var wg = registry.getEnclosingWidget(item);
            if(wg && add_mode && domAttr.get(item, 'value') == 'ZFS') {
                wg.set('checked', true);
            }
        });

        if(vol_change == true) {
            var unselected = [];
            disks.invertSelection(null);
            var opts = disks.get("value");
            for(var i=0;i<opts.length;i++) {
                unselected.push(opts[i]);
            }
            disks.invertSelection(null);

            if(unselected.length > 0 && zfs == true && first_load != true) {

                var tab = dom.byId("disks_unselected");
                query("#disks_unselected tbody tr").orphan();
                var txt = "";
                var toappend = [];
                for(var i=0;i<unselected.length;i++) {
                    var tr = domConstruct.create("tr");
                    var td = domConstruct.create("td", {innerHTML: unselected[i]});
                    tr.appendChild(td);

                    var td = domConstruct.create("td");
                    var rad = new RadioButton({ checked: true, value: "none", name: "zpool_"+unselected[i]});
                    on(rad, 'click', function() {checkNumLog(unselected);});
                    td.appendChild(rad.domNode);
                    tr.appendChild(td);

                    var td = domConstruct.create("td");
                    var rad = new RadioButton({ value: "log", name: "zpool_"+unselected[i]});
                    on(rad, 'click', function() {checkNumLog(unselected);});
                    td.appendChild(rad.domNode);
                    tr.appendChild(td);

                    var td = domConstruct.create("td");
                    var rad = new RadioButton({ value: "cache", name: "zpool_"+unselected[i]});
                    on(rad, 'click', function() {checkNumLog(unselected);});
                    td.appendChild(rad.domNode);
                    tr.appendChild(td);

                    var td = domConstruct.create("td");
                    var rad = new RadioButton({ value: "spare", name: "zpool_"+unselected[i]});
                    on(rad, 'click', function() {checkNumLog(unselected);});
                    td.appendChild(rad.domNode);
                    tr.appendChild(td);

                    toappend.push(tr);
                }

                for(var i=0;i<toappend.length;i++) {
                    domConstruct.place(toappend[i], query("#disks_unselected tbody")[0]);
                }

               domStyle.set("zfsextra", "display", "");

            } else {
                if(zfs == true && first_load == true) {
                    domStyle.set("zfsextra", "display", "");
                } else {
                    query("#disks_unselected tbody tr").orphan();
                    domStyle.set("zfsextra", "display", "none");
                }
            }
        } else if(zfs == false) {
               domStyle.set("zfsextra", "display", "none");
        }

        var ufs = query("#fsopt input")[0].checked;
        var zfs = query("#fsopt input")[1].checked;
        if(d.length >= 2) {
            domStyle.set("grpopt", "display", "");
        } else {
            domStyle.set("grpopt", "display", "none");
            query("input[name=group_type]:checked").forEach(function(tag) {
                var dtag = registry.getEnclosingWidget(tag);
                if(dtag) dtag.set('checked', false);
            });
        }

        if(zfs) {
            domStyle.set('zfssectorsize', 'display', 'table-row');
            domStyle.set('zfsfulldiskencryption', 'display', 'table-row');
            domStyle.set('zfsdedup', 'display', 'table-row');
        } else {
            domStyle.set('zfssectorsize', 'display', 'none');
            domStyle.set('zfsfulldiskencryption', 'display', 'none');
            domStyle.set('zfsdedup', 'display', 'none');
        }

        if(ufs) {
            domStyle.set("ufspath", "display", "table-row");
            domStyle.set("ufspathen", "display", "table-row");
        } else {
            domStyle.set("ufspath", "display", "none");
            domStyle.set("ufspathen", "display", "none");
        }

        if(d.length >= 3 && zfs) {
            domStyle.set("grpraidz", "display", "block");
        } else {
            domStyle.set("grpraidz", "display", "none");
        }

        if(d.length >= 4 && zfs) {
            domStyle.set("grpraidz2", "display", "block");
        } else {
            domStyle.set("grpraidz2", "display", "none");
        }

        if(d.length >= 5 && zfs) {
            domStyle.set("grpraidz3", "display", "block");
        } else {
            domStyle.set("grpraidz3", "display", "none");
        }

        if(ufs && d.length-1 >= 2 && (((d.length-2)&(d.length-1)) == 0)) {
            if(ufs)
                domStyle.set("grpraid3", "display", "block");
        } else {
            domStyle.set("grpraid3", "display", "none");
        }
    }

	return wizardcheckings;
});