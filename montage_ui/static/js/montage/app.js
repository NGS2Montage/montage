define([
        "dojo/_base/declare", "RouterApp/app",
	"dojo/_base/lang","montage/store/project",
	"montage/store/investigation","montage/store/observation", "montage/widget/Dialog"
], function(
	declare, RouterApp,
	lang,ProjectStore,
	InvestigationStore,ObservationStore, Dialog

){

    return declare([RouterApp], {

		setupRoutes: function(){
			console.log("Register Montage Routes...");
			this.registerRoute("\/$", lang.hitch(this,"rootRouteHandler"));
			this.registerRoute("\/project(\/.*)", lang.hitch(this,"projectRouteHandler"));
			this.registerRoute("\/viewer(\/.*)", lang.hitch(this,"viewerRouteHandler"));
			this.registerRoute("\/data(\/.*)", lang.hitch(this,"dataRouteHandler"));
			this.registerRoute("\/page/(.*)", lang.hitch(this,"pageRouteHandler"));
		},

		setupStores: function(){
			this.addStore("project", new ProjectStore({}));
			this.addStore("investigation", new InvestigationStore({}));
			this.addStore("observation", new ObservationStore({}));
		},

		rootRouteHandler: function(params){
			var newState = {path: params.newPath}
			newState.widgetClass="dijit/layout/ContentPane";
			newState.widgetParams = {href: "/content/home"};
			newState.requireAuth=false;
			this.set("state",newState);
		},
		pageRouteHandler: function(params){
			var newState = {path: params.newPath}
			newState.widgetClass="dijit/layout/ContentPane";
			var parts = params.newPath.split("/");
			console.log("Parts: ", parts);
			var page = parts[2];
	
			newState.widgetParams = {href: "/content/" + page};
			newState.requireAuth=false;
			this.set("state",newState);
		},
		
		
		projectRouteHandler: function(params){
			var newState = {path: params.newPath}
			var parts = params.newPath.split("/");
			console.log("Parts: ", parts);
			var project_id = parts[2];
	
			console.log("project_id: ", project_id);
	
			if (project_id) {	
				newState.widgetClass="montage/project/viewer";
				newState.project_id = project_id;
			}else{
				newState.widgetClass="montage/project/grid";
			}

			newState.requireAuth=false;
			this.set("state",newState);
		},

		viewerRouteHandler: function(params){
			var newState = {path: params.newPath}
			//newState.widgetClass="montage/viewer";
			newState.widgetClass="dijit/layout/ContentPane";
			newState.widgetParams = {content: "Viewer Viewer"};
			newState.requireAuth=false;
			this.set("state",newState);
		},

		dataRouteHandler: function(params){
			var newState = {path: params.newPath}
			newState.widgetClass="montage/workspace/explorer";
			//newState.widgetClass="dijit/layout/ContentPane";
			//newState.widgetParams = {content: "Data Viewer"};
			newState.requireAuth=false;
			this.set("state",newState);
		},

		createDialog: function(params){
			console.log("Create Montage Dialog");
 			return new Dialog(params);
 		}
    	
    })
});
