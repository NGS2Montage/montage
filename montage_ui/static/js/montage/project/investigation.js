define([
    "dojo/_base/declare", "dijit/_WidgetBase","dijit/_TemplatedMixin",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/investigation.html","dojo/dom-construct","dojo/dom-class",
	"./hypothesisItem", "./theoryItem", "./mechanismItem","./modelItem",//"./experimentItem","./analysisItem"
	"dijit/form/Button", "dijit/form/SimpleTextarea",
	"../widget/Dialog","./hypothesis","dojo/on","./model",
	"./theory", "./mechanism"
], function(
	declare,WidgetBase,Templated,
	when,lang,dojoString,Template,domConstruct,domClass,
	HypothesisItem, TheoryItem,MechanismItem,ModelItem,//ExperimentItem,AnalysisItem
	Button,Textarea,
	Dialog,Hypothesis,on,Model,
	Theory,Mechanism
){

    return declare([WidgetBase,Templated], {
    	templateString: Template,
    	investigation: null,
    	constructor: function(){
    		this.hypothesesWidgets=[];
    		this.mechanismsWidgets=[];
    		this.theoriesWidgets=[];
    		this.modelsWidgets=[];

    	},
    	_setInvestigationAttr: function(val){
    		var prev = this.investigation;
    		this.investigation = val;
    		console.log("Investigation Data: ", val);

    		if (this._started){

    			if (prev && val && prev.status && (prev.status!=val.status)){
    				domClass.remove(this.domNode, prev.status)
    			}
    			this.render();
    		}
    	},

    	render: function(){
    		if (!this.investigation){
    			console.log("No Current Investigation, TODO Clear all items");
    			return;
    		}

			domClass.add(this.domNode,this.investigation.status)

    		var dts = [["hypotheses","hypothesis",HypothesisItem],["theories","theory",TheoryItem],["mechanisms", "mechanism",MechanismItem],["models","model",ModelItem]]

    		dts.forEach(function(dt){
    			var dtplural=dt[0];
    			var dtsing = dt[1];
    			var dtwidget = dt[2];
    			var dtcapital = dtsing[0].toUpperCase() + dtsing.slice(1);

	    		if (this.investigation[dtplural]){
	    			this.investigation[dtplural].forEach(function(t,index){
	    				if (!this[dtplural + "Widgets"][index]){
	    					var params = {}
	    					params[dtsing] = t;
	    					console.log("dtwidget: ", dtwidget);
		    				var hi = this[dtplural + "Widgets"][index] = new dtwidget(params).placeAt(this[dtplural + "Container"]);
		    				hi.startup();
		    				console.log("hi: ", hi);
		    				on(hi.domNode,"Update" + dtcapital, lang.hitch(this, function(evt){
		    					console.log("Investigation::Update " + dtcapital, evt[dtsing], " Index: ", index);
		    					this.investigation[dtplural][index]=evt[dtsing];
		    					this.render();
		    				}))

		    				console.log("dtcapital: ", dtcapital)

		    				on(hi.domNode,"Remove" + dtcapital, lang.hitch(this, function(evt){
		    					console.log("Remove Handler: ", dtcapital);
		    					this.investigation[dtplural].splice(index,1);
		    					this[dtplural + "Widgets"].forEach(function(w){ w.destroy() })
		    					this[dtplural + "Widgets"] = [];
		    					console.log("Investigation::Update" + dtcapital + ": ", evt[dtsing], " Index: ", index);
		    					this.render();

		    				}))
		    			}else{
		    				this[dtplural + "Widgets"][index].set(dtsing, t);
		    			}
	    			},this)


	    			while(this[dtplural + "Widgets"].length > this.investigation[dtplural].length){
	    				var toRemove = this[dtplural + "Widgets"].pop();
	    				toRemove.destroy();
	    			}
	    		}


    		}, this);
    	},

    	addHypothesis: function(){
    		console.log("Add Hypothesis");
    		var dlg = new Dialog({title: "Add Hypothesis"});
    		var hypothesis = new Hypothesis({});

			on(hypothesis.domNode,"UpdateHypothesis", lang.hitch(this, function(evt){
	    		console.log("Investigation::Add Hypothesis: ", evt.hypothesis);
	    		this.investigation.hypotheses.push(evt.hypothesis);
	    		this.render();
	    	}))

    		domConstruct.place(hypothesis.domNode,dlg.containerNode);
    		dlg.show();
    		hypothesis.startup();
    	},

    	addTheory: function(){
    		var dlg = new Dialog({title: "Add Theory"});
    		var theory = new Theory({});

			on(theory.domNode,"UpdateTheory", lang.hitch(this, function(evt){
	    		console.log("Investigation::Add Theory: ", evt.theory);
	    		this.investigation.theories.push(evt.theory);
	    		this.render();
	    	}))

    		domConstruct.place(theory.domNode,dlg.containerNode);
    		dlg.show();
    		theory.startup();
    	},

    	addMechanism: function(){
    		var dlg = new Dialog({title: "Add Mechanism"});
    		var mechanism = new Mechanism({});

			on(mechanism.domNode,"UpdateMechanism", lang.hitch(this, function(evt){
	    		console.log("Investigation::Add Mechanism: ", evt.mechanism);
	    		this.investigation.mechanisms.push(evt.mechanism);
	    		this.render();
	    	}))

    		domConstruct.place(mechanism.domNode,dlg.containerNode);
    		dlg.show();
    		mechanism.startup();
    	},

    	addModel: function(){
    		var dlg = new Dialog({title: "Add Model"});
    		var model = new Model({});

			on(model.domNode,"UpdateModel", lang.hitch(this, function(evt){
	    		console.log("Investigation::Add Mechanism: ", evt.model);
	    		this.investigation.models.push(evt.model);
	    		this.render();
	    	}))

    		domConstruct.place(model.domNode,dlg.containerNode);
    		dlg.show();
    		model.startup();
    	},

    	startup: function(){
    		if (this._started){ return; }
    		this.inherited(arguments);
    		if (this.investigation) {
    			this.render();
    		}
    	}
	})
});
