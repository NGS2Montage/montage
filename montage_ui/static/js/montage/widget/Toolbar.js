define([
    "dojo/_base/declare", "dijit/_Widget","dojo/on","dojo/_base/lang",
    "dojo/dom-construct","dojo/dom-attr","dojo/dom-class"
], function(
	declare,Widget,on,lang,
	domConstruct,domAttr,domClass
){

	return declare([Widget],{
		baseClass: "Toolbar",
		constructor: function(){
			this._actions={};
		},

		postCreate: function(){
			this.inherited(arguments);
			on(this.domNode,"I:click", lang.hitch(this,function(evt){
				evt.preventDefault();
				evt.stopPropagation();
				var rel = domAttr.get(evt.target,"rel")
				if (this._actions[rel] && this._actions[rel].action && !this._actions[rel].disabled){
					this._actions[rel].action();
				}
			}))
		},
		addAction: function(id,action){
 			this._actions[id] = action;
 			var button = domConstruct.create("i", {"class": action.icon + (action.disabled?" disabled":""), rel: id});
 			domConstruct.place(button,this.domNode,"last");
 			this._actions[id].button = button;
		},

		disable: function(id){
			if (this._actions[id] && !this._actions[id].disabled){
				domClass.add(this._actions[id].button,"disabled")
				this._actions[id].disabled=true;
			}
		},

		enable: function(id){
			if (this._actions[id] && this._actions[id].disabled){
				domClass.remove(this._actions[id].button,"disabled")
				this._actions[id].disabled=false;
			}
		}
	});
});
