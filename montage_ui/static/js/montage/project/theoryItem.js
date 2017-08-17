define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/theoryItem.html",
	"../widget/Dialog","./theory","dojo/dom-construct",'dojo/on'
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template,
	Dialog,Theory,domConstruct,on
){

	return declare([WidgetBase,Templated], {
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
			this.textNode.innerHTML = this.theory.text;
		},

		remove: function(){
			console.log("Delete this theory");
			on.emit(this.domNode, "RemoveTheory", {
				   bubbles: true,
				   cancelable: true,
				   theory: this.theory
    		})
		},

		edit: function(){
			console.log("Edit Theory");
    		var dlg = new Dialog({title: "Edit Theory"});
    		var theory = new Theory({theory: this.theory});
    		domConstruct.place(theory.domNode,dlg.containerNode);
    		on(theory.domNode, "UpdateTheory", lang.hitch(this,function(evt){
    			evt.stopPropagation();
    			evt.preventDefault();
    			this.set("theory", evt.theory);
    			
    			on.emit(this.domNode, "UpdateTheory", {
				   bubbles: true,
				   cancelable: true,
				   theory: evt.theory
    			})
    		}))

    		dlg.show();
    		theory.startup();
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.theory) { this.render(); }

			this._started=true;
		}
	});
});
