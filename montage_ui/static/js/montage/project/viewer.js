define([
        "dojo/_base/declare", "dijit/layout/BorderContainer","dijit/layout/ContentPane",
	"dojo/when","dojo/_base/lang","dojo/string","dojo/text!./template/ProjectOverviewPanel.html",
	"dijit/layout/TabContainer","dojo/query","dojo/on","dojo/dom-class","dojo/dom-attr","./investigation",
	"../form/observation","../widget/Dialog","./observations","../widget/Toolbar","dojo/dom-construct"
], function(
	declare,BorderContainer,ContentPane,
	when,lang,dojoString,POPTemplate,
	TabContainer,Query,on,domClass,domAttr,Investigation,
	Observation,Dialog,Observations,Toolbar,domConstruct
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
				this.observationsView.set("projectId", project.id);
				this.investigationToolbar.enable("addObservation")
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
				this.investigationView.set("investigation",investigation) 
			}
	
		},

		getInvestigations: function(){
			return when(this.investigationStore.query({project: this.project.id},{sort: [{attribute: "createdOn",descending: true}]}), lang.hitch(this,function(results){
				if (results.length>0) {
					this.set("currentInvestigation", results[0]);
					this.set("investigations", results);
				}else{
					return when(this.investigationStore.add({project: this.project.id}), lang.hitch(this,function(I){
						console.log("Investigation I: ", I)
						return when(this.investigationStore.get(I), lang.hitch(this,function(inv){
							this.set("currentInvestigation", inv)
							this.set("investigations", [inv]);
						}))
					}))
				}
			}));	
		},

		showDialog: function(widget, title){
			var dlg = new Dialog({title: title});

			domConstruct.empty(dlg.containerNode);
			domConstruct.place(widget.domNode,dlg.containerNode,"first");
			widget.startup();
			dlg.show()
		},
		
		startup: function(){
			var headerContent = (this.project&&this.project.name)?dojoString.substitute(POPTemplate,this.project):""	
		//	var headerContent = "Header Content";
			this.projectHeader = new ContentPane({content: headerContent, region: "top"});
	

		
			var investigationContent = (this.investigations && this.investigations[0])?this.investigations[0]:{};	

			var tb = this.investigationToolbar = new Toolbar({region: "top", style: "border: 0px;margin:0px;padding:2px;"});

			tb.addAction("addObservation", {
				icon: "icon fa-2x icon-comment",
				disabled: true,
				action: lang.hitch(this,function(){
					var w = new Observation({projectId: this.project.id})
					this.showDialog(w,"Add Observation");
				})
			})

			tb.addAction("play", {
				icon: "icon fa-2x icon-play",
				disabled: true,
				action: function(){
					console.log("Play");
				}
			})

			// this.investigationButtons = new ContentPane({region: "top", style: "border:0px;margin:0px;padding:2px;", "class":"InvestigationButtons",content: '<i rel=\'montage/form/observation:{\"projectId\":' + this.project.id + ',\"title\":\"Add Observation\"}\' class="icon fa-2x icon-comment ApplicationDialogButton"></i><i rel="playInvestigation" class="icon fa-2x icon-play"></i>'});
			// on(this.investigationButtons.domNode, "I:click", lang.hitch(this,function(evt){
			// 	console.log("CLICK")
			// 	var target = evt.target;
			// 	var rel = domAttr.get(target,"rel")
			// 	switch(rel){
			// 		case "addComment":
			// 			break;
			// 		case "playInvestigation":
			// 			break;
			// 		default: 
			// 			console.log("Eh? " + rel);
			// 	}

			// }));
			this.investigationView = new Investigation({region: "center",investigation: this.investigation?this.investigation:null });
			console.log("InvestigationView: ", this.investigationView)

			this.addChild(this.projectHeader);
			this.addChild(this.investigationToolbar);
			this.addChild(this.investigationView);
			this.sidePanelTabContainer = new TabContainer({style: "width: 200px;",region: "right", splitter:true});
			this.investigationsList = new ContentPane({title: "Investigations", region: "right", class:"InvestigationsList"});
			this.sidePanelTabContainer.addChild(this.investigationsList);
			this.observationsView= new Observations({style: "margin:0px;padding:0px;border:0px;", title: "Observations", projectId: this.project?this.project.id:"", region: "right" });
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
				this.investigationToolbar.enable("addObservation")
			}
		}
	})
});
