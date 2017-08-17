define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane",
	"dojo/when","dojo/_base/lang","dojo/string",
	"dojo/topic"
], function(
	declare,BorderContainer,ContentPane,
	when,lang,dojoString,
	Topic
){

        return declare([BorderContainer], {
		store: window.App.store.observation,
		projectId: null,
		_setProjectIdAttr: function(val){
			this.projectId = val;
			if (this._started){
				this.refresh();
			}
		},

		observationTemplate: '<div class="ObservationItem"><div class="meta">${createdBy} &nbsp; - &nbsp; ${createdOn}</div><div class="text">${text}</div></div>',
		startup: function(){
//			this.projectHeader = new ContentPane({content: '<table style="width:100%"><tr><td>Projects</td><td></td><td style="text-align:right;"><a class="ApplicationDialogButton" href rel="montage/form/CreateProject:Create New Project">Create New Project</a></td></tr></table>', region: "top"});
//			this.addChild(this.projectHeader);
			this.observationsView= new ContentPane({style: "margin:0px;padding:0px;border:0px;",content: '', region: "center"});
			this.addChild(this.observationsView);
			this.inherited(arguments);
			Topic.subscribe("/refreshObservations", lang.hitch(this, "refresh"));
			this.refresh();
		},

		refresh: function(){

			when(this.getObservations(), lang.hitch(this,function(results){
				var out = [];
				results.forEach(function(p){
					out.push(dojoString.substitute(this.observationTemplate,p));
				},this)

				this.observationsView.set("content", out.join(""));
			}));
		},

		getObservations: function(){
			return this.store.query({project: this.projectId}, {sort:[{attribute: "lastModified", descending: true}]} );
		}
	})
});
