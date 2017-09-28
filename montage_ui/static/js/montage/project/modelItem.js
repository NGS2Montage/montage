define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/modelItem.html",
	"../widget/Dialog","dojo/_base/Deferred","dojo/dom-construct","dojo/on","dojo/dom-class"
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template,
	Dialog, Deferred,domConstruct,on,domClass
){

	return declare([WidgetBase,Templated], {
		templateString: Template,
		model: null,
		_setModelAttr: function(val){
			this.model= val;
			console.log("Model Data: ", val);

			if (this._started){
				this.render();
			}
		},
		getConstructor: function(cls){
			var def = new Deferred();
			require([cls], function(ctor){
			        def.resolve(ctor);
			});
			return def.promise;
		},

		edit: function(){
			when(this.getConstructor("montage/model/" + this.model.type), lang.hitch(this, function(ctor){
				var dlg = new Dialog({title: "Edit Model: " + this.model.type});
    			var model = new ctor({model: this.model});
    			domConstruct.place(model.domNode,dlg.containerNode);

    			on(model.domNode, "UpdateModel", lang.hitch(this,function(evt){
    				console.log("UpdateModel: ", evt);
	    			evt.stopPropagation();
	    			evt.preventDefault();
	    			this.set("model", evt.model);

	    			on.emit(this.domNode, "UpdateModel", {
					   bubbles: true,
					   cancelable: true,
					   model: evt.model
	    			})
	    		}))

    			dlg.show();
    			model.startup();
			}))
		},
		remove: function(){},
		render: function(){

			domClass.remove(this.statusNode)
			switch(this.model.state){
				case "ready":
					domClass.add(this.statusNode, "icon-check-circle icon fa-2x ready");

					break;
				case "incomplete":
					domClass.add(this.statusNode, "icon-exclamation-circle icon fa-2x incomplete");
					break;
				default: {
					domClass.add(this.statusNode, "icon fa-2x icon-warning " + this.model.state);
					break;
				}
			}

			domConstruct.empty(this.containerNode);
			when(this.getConstructor("dojo/text!montage/model/template/" + this.model.type + "-item.html"), lang.hitch(this,function(template){
				console.log("template: ", template);
				this.containerNode.innerHTML=dojoString.substitute(template,this.model);
			}));
		},

		startup: function(){
			if (this._started){ return; }
			this.inherited(arguments);
			if (this.model) { this.render(); }
		}
	});
});
