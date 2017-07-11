define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/ProjectOverviewPanel.html",
	"dijit/layout/TabContainer","dojo/query","dojo/on","dojo/dom-class","dojo/dom-attr"
], function(
	declare,BorderContainer,ContentPane,
	when,lang,dojoString,POPTemplate,
	TabContainer,Query,on,domClass,domAttr
){

        return declare([BorderContainer], {
		state: null,
		project: null,
		investigations: null,
		currentInvestigation: null,
		projectStore: window.App.store.project,
		investigationStore: window.App.store.investigation,
		_setStateAttr: function(state){
			this.state=state;
			console.log("Project Viewer setState: ", state);
			if (state.project_id){
				this.getProject(state.project_id);
			}
		},

		getProject: function(id){
			console.log("getProject()");
			return when(this.projectStore.get(id), lang.hitch(this,function(project){
				console.log("Project: ", project);
				this.set("project", project);		
			}));
		},

		_setProjectAttr: function(project){
			this.project=project;
			if (this._started){
				this.projectHeader.set("content",dojoString.substitute(POPTemplate,project));
			}

			this.getInvestigations();
		},

		_setInvestigationsAttr: function(investigations){
			this.investigations = investigations;
			console.log("set investigations: ", investigations);
			if (this._started){
				console.log("Render Investigations List", investigations);
				var out=[]
				investigations.forEach(function(investigation,index){
					var classes= (investigation.id == this.currentInvestigation.id)?"SelectedInvestigation":"";
					out.push('<div rel="' +index+ '"  class="InvestigationListButton ' +classes + '"><span>' + investigation.id +"</span>" + '&nbsp;<span>' + investigation.status+ '<br>' + investigation.lastModified + '</div>');
				},this);
				console.log("Set InvestigationsList: ", out.join(""));
				this.investigationsList.set("content", out.join(""));
			}
		},

		_setCurrentInvestigationAttr: function(investigation){
			this.currentInvestigation = investigation;
			if (this._started){
				this.investigationView.set("content", "<pre>" + JSON.stringify(investigation,null,4) + "</pre>")
			}
	
		},

		getInvestigations: function(){
			return when(this.investigationStore.query({project: this.project.id},{sort: [{attribute: "createdOn",descending: true}]}), lang.hitch(this,function(results){
				this.set("currentInvestigation", results[0]);
				this.set("investigations", results);
			}));	
		},
		
		startup: function(){
			var headerContent = (this.project&&this.project.name)?dojoString.substitute(POPTemplate,this.project):""	
		//	var headerContent = "Header Content";
			this.projectHeader = new ContentPane({content: headerContent, region: "top"});
			this.addChild(this.projectHeader);

		
			var investigationContent = (this.investigations && this.investigations[0])?this.investigations[0]:{};	
			this.investigationView = new ContentPane({content: "<pre>"+JSON.stringify(investigationContent,null,4) + "</pre>", region: "center" });
			this.addChild(this.investigationView);
			this.sidePanelTabContainer = new TabContainer({style: "width: 200px;",region: "right", splitter:true});
			this.investigationsList = new ContentPane({title: "Investigations", region: "right", class:"InvestigationsList"});
			this.sidePanelTabContainer.addChild(this.investigationsList);
			this.observationsView= new ContentPane({title: "Observations", region: "right" });
			this.sidePanelTabContainer.addChild(this.observationsView);
			this.addChild(this.sidePanelTabContainer);

			console.log("Check for Investigations: ", this.investigations);

			this.inherited(arguments);

			on(this.investigationsList.containerNode, ".InvestigationListButton:click", lang.hitch(this, function(evt){
				console.log("evt.target", evt.target);
				var target = evt.target;
				while (!domClass.contains(target,"InvestigationListButton")) {
					target=target.parentNode;
				}
				var idx = domAttr.get(target,"rel");
				var investigation = this.investigations[idx];
				this.set("currentInvestigation", investigation);
				Query(".InvestigationListButton",this.investigationsList.containerNode).forEach(function(node){
					domClass.remove(node, "SelectedInvestigation")
				});
				domClass.add(target, "SelectedInvestigation");
			
			}))



			if (this.investigations) {
				console.log("Found Investigations: ", this.investigations.length);	
				this.set("investigations", this.investigations);
				this.set("currentInvestigation", this.investigations[0]);
			}
		}
	})
});
