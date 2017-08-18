define([
        "dojo/_base/declare", "./base", "dojo/on","dojo/dom-construct",
        "dojo/dom-class","dojo/text!./template/observation.html",
        "dojo/request","dijit/form/ValidationTextBox","dojo/topic","dojo/_base/lang",
		"dijit/form/CheckBox","dijit/form/Select","dijit/form/Button","dojo/query",
		"dojo/when"
], function(
	declare, FormBase, on, domConstruct,
	domClass, Template,
	Request,ValidationTextBox, Topic,lang,
	CheckBox,Select,Button,Query,
	when


){

	return declare([FormBase], {
		templateString: Template,
		projectId: null,

		constructor: function(){
			this.store = window.App.store.observation;
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

					if (!this.projectId){
						console.warn("No Project ID for Add Observation()");
						return;
					}

			        var values = this.getValues();
			        this.showMessage("working");
			        console.log("Form is Valid!", values)

			        console.log("Add Observation: ", values)
			        values.project = this.projectId

				   	when(this.store.add(values), function(){
				   		_self.showMessage("complete");

				        on.emit(_self.domNode, "DialogAction", {
				        	bubbles: true,
					   		cancelable: true,
					   		action: "close"
					   	});

					   	Topic.publish("/refreshObservations");

				   	}, function(err){
			        	_self.showMessage("error", "Error: " + err);
			        });
			}else{
			        console.log("Form is incomplete");
			}
		},
		onCancel: function(){
			console.log("Add Observation onCancel()");
			this.inherited(arguments);

		}
	});

});
