define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane"
], function(declare,BorderContainer,ContentPane){

        return declare([BorderContainer], {
		state: null,
		_setStateAttr: function(state){
			this.state=state;
			console.log("Project Viewer setState: ", state);
		},
		
		startup: function(){
			this.projectHeader = new ContentPane({content: "Project Header", region: "top"});
			this.addChild(this.projectHeader);
			this.investigationView = new ContentPane({content: "Investigation Details", region: "center"});
			this.addChild(this.investigationView);
			this.historySelector = new ContentPane({content: "Histories", region: "right", style: "width:175px;"});
			this.addChild(this.historySelector);
			this.inherited(arguments);
		}
	})
});
