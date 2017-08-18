define([
        "dojo/_base/declare", "./base", "dojo/on","dojo/dom-construct",
        "dojo/dom-class","dojo/text!./template/CreateProject.html",
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
		availableTests: null,

		constructor: function(){
			this.store = window.App.store.project;
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

				   	when(this.store.add(values), function(){
				   		_self.showMessage("complete");

				        on.emit(_self.domNode, "DialogAction", {
				        	bubbles: true,
					   		cancelable: true,
					   		action: "close"
					   	});

					   	Topic.publish("/refreshProjects");

				   	}, function(err){
			        	_self.showMessage("error", "Error: " + err);
			        });
			}else{
			        console.log("Form is incomplete");
			}
		},
		onCancel: function(){
			console.log("CreateProject onCancel()");
			this.inherited(arguments);

		}
	});

});
