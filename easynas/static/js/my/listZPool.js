define(["my/commonDialog"], function(commonDialog){
    createZPool = function(nodes) {
        commonDialog({
            id: "list_zpool_dialog",
            style: "max-width: 650px;min-height:200px;max-height:500px;background-color:white;overflow:auto;",
            name: "Create ZPool",
            url: "/easynas/storage/dialog/list_zpool",
            nodes: nodes,
			onLoad: function()
			{
				var registry = require("dojo/store/JsonRest");
				var store = new JsonRest({
					target: "/easynas/zpools"
				});
				store.remove(3);

			}

        });
    }
	return createZPool;
});