define([
  "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin","dijit/_WidgetsInTemplateMixin",
  "dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/hypothesis.html","dojo/on"
], function(
  declare,WidgetBase,Templated,WidgetsInTemplate,
  when,lang,dojoString,Template,on
){
  return declare([WidgetBase,Templated,WidgetsInTemplate], {
    templateString: Template,
    hypothesis: null,
    _setHypothesisAttr: function(val){
      this.hypothesis = val;
      console.log("Hypothesis Data: ", val);
      if (this._started){
        this.render();
      }
    },
    render: function(){
      console.log("Set Hypothesis Text: ", this.hypothesis.text);
      this.textWidget.set("value",this.hypothesis.text);
    },

    save: function(){
      var save = {};
      if (!this.hypothesis){
        this.hypothesis = save;
      }
      Object.keys(this.hypothesis).forEach(function(key){
        save[key] = this.hypothesis[key];
      },this);
      save.text = this.textWidget.get("value");

      console.log("Save Hypothesis");
      on.emit(this.domNode, "UpdateHypothesis", {
        bubbles: true,
        cancelable: true,
        hypothesis: save
      });
      on.emit(this.domNode, "DialogAction", {
        bubbles: true,
        cancelable: true,
        action: "close"
      });
    },

    cancel: function(){
      console.log("Cancel");
      on.emit(this.domNode, "DialogAction", {
        bubbles: true,
        cancelable: true,
        action: "close"
      });
    },

    startup: function(){
      if (this._started){ return; }
      this.inherited(arguments);
      if (this.hypothesis) { this.render(); }
      this._started = true;
    }
  });
});
