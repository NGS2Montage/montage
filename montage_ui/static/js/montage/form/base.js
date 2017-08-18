define([
        "dojo/_base/declare", "dijit/_WidgetBase", "dojo/on",
        "dojo/dom-class", "dijit/_TemplatedMixin", "dijit/_WidgetsInTemplateMixin",
         "dijit/form/Form","dojo/topic"
], function(declare, WidgetBase, on,
                        domClass, Templated, WidgetsInTemplate,
                        FormMixin, Topic){
        return declare([WidgetBase, FormMixin, Templated, WidgetsInTemplate], {
                completeMessage: "Action Completed",
                workingMessage: "Submitting Form",
                errorMessage: "There was an error in your submission",

                showMessage: function(type,msg){
                    if (!type){
                        throw Error("Missing Message Type");
                    }

                    msg = msg || this[type + "Message"];

                    if (this.messageNode){
                        this.messageNode.innerHTML = msg;
                        domClass.remove(this.messageNode, "dijitHidden");
                    }
                },

                hideMessage: function(){
                    domClass.add(this.messageNode, "dijitHidden");

                },
		        validate: function(){
                        var valid = this.inherited(arguments);

                        if(valid){
                                this.saveButton.set("disabled", false)
                        }else{
                                this.saveButton.set("disabled", true);
                        }
                        return valid;
                },

                onSubmit: function(evt){
                        var _self = this;

                        evt.preventDefault();
                        evt.stopPropagation();

                        if(this.validate()){

                                var values = this.getValues();
                                console.log("Form is Valid!", values)
                                on.emit(this.domNode, "DialogAction", {
                                    bubbles: true,
                                    cancelable: true,
                                    action: "close"
                                });
                                // domClass.add(this.domNode, "Working");
                                // console.log("CREATING FOLDER: ", this.path + values.name, this.path);
                                // WorkspaceManager.createFolder(this.path + values.name).then(function(results){
                                //         console.log("RESULTS", results)
                                //         domClass.remove(_self.domNode, "Working");
                                //         console.log("create_workspace_folder results", results);
                                //         var path = "/" + ["workspace", results.path].join("/");
                                //         Topic.publish("/refreshWorkspace", {});
                                //         on.emit(_self.domNode, "dialogAction", {action: "close", navigate: path, bubbles: true});
                                // }, function(err){
                                //         console.log("Error:", err);
                                //         domClass.remove(_self.domNode, "Working");
                                //         domClass.add(_self.domNode, "Error");
                                //         _self.errorMessage.innerHTML = err;
                                // })
                        }else{
                                console.log("Form is incomplete");
                        }
                },

                onCancel: function(evt){
                        console.log("onCancel")
                        on.emit(this.domNode, "DialogAction", {
                            bubbles: true,
                            cancelable: true,
                            action: "close"
                        });
                }
        });
});
    
