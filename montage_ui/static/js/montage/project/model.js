define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin","dijit/_WidgetsInTemplateMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/model.html","dojo/on"
], function(
	declare,WidgetBase,Templated,WidgetsInTemplate,
	when,lang,dojoString,Template,on
){

	return declare([WidgetBase,Templated,WidgetsInTemplate], {
		templateString: Template,
		model: null,
		_setModelAttr: function(val){
			this.model= val;
			console.log("Model Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
			console.log("Set Model Text: ", this.model.text);
			this.textWidget.set("value",this.model.text); 
		},

		save: function(){
			var save = {params: {}}
			if (!this.model){ 
				this.model = save
			};
			Object.keys(this.model).forEach(function(key){
					save[key] = this.model[key];
			},this)

			save.type = this.modelType.get("value");

			console.log("Save Model");
    		on.emit(this.domNode, "UpdateModel", {
				   bubbles: true,
				   cancelable: true,
				   model: save
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
			if (this.model) { this.render(); }

			this._started=true;
		}
	});
});
