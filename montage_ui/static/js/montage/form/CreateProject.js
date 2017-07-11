define([
        "dojo/_base/declare", "./base", "dojo/on","dojo/dom-construct",
        "dojo/dom-class","dojo/text!./template/CreateProject.html",
        "dojo/request","dijit/form/ValidationTextBox","dojo/topic","dojo/_base/lang",
		"dijit/form/CheckBox","dijit/form/Select","dijit/form/Button","dojo/query"
], function(
	declare, FormBase, on, domConstruct,
	domClass, Template,
	Request,ValidationTextBox, Topic,lang,
	CheckBox,Select,Button,Query


){

	return declare([FormBase], {
		templateString: Template,
		availableTests: null,

		constructor: function(){
		},

		startup: function(){
			if (this._started) { return; }
			this.inherited(arguments);

		},


        onSubmit: function(evt){
			var _self = this;

			evt.preventDefault();
			evt.stopPropagation();

			if(this.validate()){

			        var values = this.getValues();
			        this.showMessage("working");
			        console.log("Form is Valid!", values)
				return;
			        Request.post("/assessment/", {
			        	headers: {
			        		"content-type": "application/json",
			        		"accept": "application/json"
			        	},
			        	data: JSON.stringify(values)
			        }).then(
			        	function(results){
			        		_self.showMessage("complete");
			        		Topic.publish("/refreshAssessments");
			        		on.emit(_self.domNode, "dialogAction", {action: "close", bubbles: true});

			        	},
			        	function(err){
			        		_self.showMessage("error", "Error: " + err);
			        	}
			        )
			}else{
			        console.log("Form is incomplete");
			}
		}
	});

});
