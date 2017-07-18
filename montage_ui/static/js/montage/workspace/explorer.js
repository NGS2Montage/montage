define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane"
], function(declare,BorderContainer,ContentPane){

        return declare([BorderContainer], {
		startup: function(){
			this.dataHeader = new ContentPane({content: "Data Header", region: "top"});
			this.addChild(this.dataHeader);
			this.folderGrid = new ContentPane({content: "Data Folder Grid", region: "center"});
			this.addChild(this.folderGrid);
			this.itemDetail= new ContentPane({content: "Detail Panel", splitter:true, region: "right", style: "width:250px;"});
			this.addChild(this.itemDetail);
			this.actionBar = new ContentPane({content: "", region: "right", style: "width:40px;"});
			this.addChild(this.actionBar);
			this.inherited(arguments);
		}
	})
});
