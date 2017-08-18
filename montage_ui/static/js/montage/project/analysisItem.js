define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/analysisItem.html"
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template
){

	return declare([WidgetBase,Templated], {
		templateString: Template,
		analysis: null,
		_setAnalysisAttr: function(val){
			this.analysis= val;
			console.log("Analysis Data: ", val);

			if (this._started){
				this.render();
			}
		},
		render: function(){
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.analysis) { this.render(); }
		}
	});
});
