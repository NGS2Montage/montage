define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/experimentItem.html"
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template
){

	return declare([WidgetBase,Templated], {
		templateString: Template,
		experiment: null,
		_setExperimentAttr: function(val){
			this.experiment= val;
			console.log("Experiment Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.experiment) { this.render(); }
		}
	});
});
