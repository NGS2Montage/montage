define([
        "dojo/_base/declare", "dijit/_Widget"
], function(declare,WidgetBase ){

        return declare([WidgetBase], {
		postCreate: function(){
			this.domNode.innerHTML="Workspace Explorer"
		}
	})
});
