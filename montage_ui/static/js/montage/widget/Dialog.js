define([
    "dojo/_base/declare", "dijit/Dialog","dojo/on","dojo/_base/lang"
], function(
	declare,Dialog,on,lang
){

	return declare([Dialog],{
		foo: true,
		startup: function(){
			this.inherited(arguments);

			on(this.domNode, "DialogAction", lang.hitch(this, function(evt){
				console.log("Dialog Action Event: ", evt);

				switch(evt.action){
					case "close":
						this.hide();
						break;
					case "refresh":
						this.resize();
						break;
					default:
						console.warn("Unknown DialogAction Event: " + evt.action);
						break;
				}
			}));

		}

	});
});
