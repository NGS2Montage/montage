define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin","dijit/_WidgetsInTemplateMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/theory.html","dojo/on"
], function(
	declare,WidgetBase,Templated,WidgetsInTemplate,
	when,lang,dojoString,Template,on
){

	return declare([WidgetBase,Templated,WidgetsInTemplate], {
		templateString: Template,
		theory: null,
		_setTheoryAttr: function(val){
			this.theory= val;
			console.log("Theory Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
			console.log("Set Theory Text: ", this.theory.text);
			this.textWidget.set("value",this.theory.text); 
		},

		save: function(){
			var save = {}
			if (!this.theory){ this.theory = save};
			Object.keys(this.theory).forEach(function(key){
					save[key] = this.theory[key];
			},this)

			save.text = this.textWidget.get("value");

			console.log("Save Theory");
    		on.emit(this.domNode, "UpdateTheory", {
				   bubbles: true,
				   cancelable: true,
				   theory: save
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
			if (this.theory) { this.render(); }

			this._started=true;
		}
	});
});
