define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane"
], function(declare,BorderContainer,ContentPane){

        return declare([BorderContainer], {
		startup: function(){
			this.projectHeader = new ContentPane({content: "Projects", region: "top"});
			this.addChild(this.projectHeader);
			this.investigationView = new ContentPane({content: '<a class="ApplicationNavLink" href="/project/TestProject">Test Project</a>', region: "center"});
			this.addChild(this.investigationView);
			this.inherited(arguments);
		}
	})
});
