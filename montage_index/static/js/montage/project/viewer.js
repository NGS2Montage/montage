define([
        "dojo/_base/declare", "dijit/_Widget"
], function(declare,WidgetBase){

        return declare([WidgetBase], {
		content: "Project Viewer",
		postCreate: function(){
			this.domNode.innerHTML="Project Viewer"
		}
	})
});
