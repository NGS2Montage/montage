define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/mechanismItem.html",
	"../widget/Dialog","./mechanism","dojo/dom-construct",'dojo/on'
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template,
	Dialog,Mechanism,domConstruct,on
){

	return declare([WidgetBase,Templated], {
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
			this.textNode.innerHTML = this.mechanism.text;
		},

		remove: function(){
			console.log("Delete this mechanism");
			on.emit(this.domNode, "RemoveMechanism", {
				   bubbles: true,
				   cancelable: true,
				   mechanism: this.mechanism
    		})
		},

		edit: function(){
			console.log("Edit Mechanism");
    		var dlg = new Dialog({title: "Edit Mechanism"});
    		var mechanism = new Mechanism({mechanism: this.mechanism});
    		domConstruct.place(mechanism.domNode,dlg.containerNode);
    		on(mechanism.domNode, "UpdateMechanism", lang.hitch(this,function(evt){
    			evt.stopPropagation();
    			evt.preventDefault();
    			this.set("mechanism", evt.mechanism);
    			
    			on.emit(this.domNode, "UpdateMechanism", {
				   bubbles: true,
				   cancelable: true,
				   mechanism: evt.mechanism
    			})
    		}))

    		dlg.show();
    		mechanism.startup();
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.mechanism) { this.render(); }

			this._started=true;
		}
	});
});
