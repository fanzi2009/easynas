define(["my/commonDialog"], function(commonDialog){
    createZPool = function(nodes) {
        commonDialog({
            id: "create_zpool_dialog",
            style: "max-width: 650px;min-height:200px;max-height:500px;background-color:white;overflow:auto;",
            name: "Create ZPool",
            url: "/easynas/storage/dialog/create_zpool",
            nodes: nodes
            });
    }
	return createZPool;
});