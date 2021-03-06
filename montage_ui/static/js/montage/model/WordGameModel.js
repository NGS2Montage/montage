define([
  "dojo/_base/declare", "../form/base", "dojo/on","dojo/dom-construct",
  "dojo/dom-class","dojo/text!./template/WordGameModel.html",
  "dojo/request","dijit/form/ValidationTextBox","dojo/topic","dojo/_base/lang",
  "dijit/form/CheckBox","dijit/form/Select","dijit/form/Button","dojo/query",
  "dojo/when","dojo/dom-construct"
], function(
  declare, FormBase, on, domConstruct,
  domClass, Template,
  Request,ValidationTextBox, Topic,lang,
  CheckBox,Select,Button,Query,
  when,domConstruct


){

  return declare([FormBase], {
    templateString: Template,
    model: null,
    entropySource:"",
    _setModelAttr: function(val){
      this.model = val;
      if (this.model.params){
        this.setValues(this.model.params);
      }else{

      }
    },
    constructor: function(){
      this.store = window.App.store.observation;
    },

    //TODO on activate get random seed and set this.entropySource =

    startup: function(){
      if (this._started) { return; }
      this.inherited(arguments);
      this.validate();

    },


    onSubmit: function(evt){
      var _self = this;

      evt.preventDefault();
      evt.stopPropagation();

      if(this.validate()){

        var values = this.getValues();
        this.showMessage("working");
        console.log("Form is Valid!", values)

        this.model.params = values;;


        on.emit(this.domNode, "UpdateModel", {
          bubbles: true,
          cancelable: true,
          model: this.model
        })

        on.emit(this.domNode, "DialogAction", {
          bubbles: true,
          cancelable: true,
          action: "close"
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
