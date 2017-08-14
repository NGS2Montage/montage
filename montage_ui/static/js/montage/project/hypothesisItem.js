define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/hypothesisItem.html",
	"../widget/Dialog","./hypothesis","dojo/dom-construct",'dojo/on'
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template,
	Dialog,Hypothesis,domConstruct,on
){

	return declare([WidgetBase,Templated], {
		templateString: Template,
		hypothesis: null,
		_setHypothesisAttr: function(val){
			this.hypothesis= val;
			console.log("Hypothesis Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
			this.textNode.innerHTML = this.hypothesis.text;
		},

		remove: function(){
			console.log("Delete this hypothesis");
			on.emit(this.domNode, "RemoveHypothesis", {
				   bubbles: true,
				   cancelable: true,
				   hypothesis: this.hypothesis
    		})
		},

		edit: function(){
			console.log("Edit Hypothesis");
			    		console.log("Add Hypothesis");
    		var dlg = new Dialog({title: "Add Hypothesis"});
    		var hypothesis = new Hypothesis({hypothesis: this.hypothesis});
    		domConstruct.place(hypothesis.domNode,dlg.containerNode);
    		on(hypothesis.domNode, "UpdateHypothesis", lang.hitch(this,function(evt){
    			evt.stopPropagation();
    			evt.preventDefault();
    			this.set("hypothesis", evt.hypothesis);
    			
    			on.emit(this.domNode, "UpdateHypothesis", {
				   bubbles: true,
				   cancelable: true,
				   hypothesis: evt.hypothesis
    			})
    		}))

    		dlg.show();
    		hypothesis.startup();
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.hypothesis) { this.render(); }

			this._started=true;
		}
	});
});
