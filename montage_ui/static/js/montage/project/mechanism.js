define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin","dijit/_WidgetsInTemplateMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/mechanism.html","dojo/on"
], function(
	declare,WidgetBase,Templated,WidgetsInTemplate,
	when,lang,dojoString,Template,on
){

	return declare([WidgetBase,Templated,WidgetsInTemplate], {
		templateString: Template,
		mechanism: null,
		_setMechanismAttr: function(val){
			this.mechanism= val;
			console.log("Mechanism Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
			console.log("Set Mechanism Text: ", this.mechanism.text);
			this.textWidget.set("value",this.mechanism.text); 
		},

		save: function(){
			var save = {}
			if (!this.mechanism){ this.mechanism = save};
			Object.keys(this.mechanism).forEach(function(key){
					save[key] = this.mechanism[key];
			},this)

			save.text = this.textWidget.get("value");

			console.log("Save Mechanism");
    		on.emit(this.domNode, "UpdateMechanism", {
				   bubbles: true,
				   cancelable: true,
				   mechanism: save
			})

			on.emit(this.domNode, "DialogAction", {
			    bubbles: true,
    			cancelable: true,
				action: "close"
			});
		},

		cancel: function(){
			console.log("Cancel");
			on.emit(this.domNode, "DialogAction", {
				    bubbles: true,
    				cancelable: true,
			  		action: "close"
			});
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.mechanism) { this.render(); }

			this._started=true;
		}
	});
});
