define([
        "dojo/_base/declare", "RouterApp/app",
	"dojo/_base/lang"
], function(
	declare, RouterApp,
	lang
){

        return declare([RouterApp], {
		setupRoutes: function(){
			console.log("Register Montage Routes...");
			this.registerRoute("\/$", lang.hitch(this,"rootRouteHandler"));
			this.registerRoute("\/project(\/.*)", lang.hitch(this,"projectRouteHandler"));
			this.registerRoute("\/viewer(\/.*)", lang.hitch(this,"viewerRouteHandler"));
			this.registerRoute("\/data(\/.*)", lang.hitch(this,"dataRouteHandler"));
		},

		rootRouteHandler: function(params){
			var newState = {href: params.newPath}
			newState.widgetClass="dijit/layout/ContentPane";
			newState.widgetParams = {href: "/content/home"};
			newState.requireAuth=false;
			this.set("state",newState);
		},
		
		projectRouteHandler: function(params){
			var newState = {href: params.newPath}
			newState.widgetClass="montage/project/viewer";
			//newState.widgetClass="dijit/layout/ContentPane";
			//newState.widgetParams = {content: "Project Viewer"};
			newState.requireAuth=false;
			this.set("state",newState);
		},

		viewerRouteHandler: function(params){
			var newState = {href: params.newPath}
			//newState.widgetClass="montage/viewer";
			newState.widgetClass="dijit/layout/ContentPane";
			newState.widgetParams = {content: "Viewer Viewer"};
			newState.requireAuth=false;
			this.set("state",newState);
		},

		dataRouteHandler: function(params){
			var newState = {href: params.newPath}
			newState.widgetClass="montage/workspace/explorer";
			//newState.widgetClass="dijit/layout/ContentPane";
			//newState.widgetParams = {content: "Data Viewer"};
			newState.requireAuth=false;
			this.set("state",newState);
		}
    	
    	})

});
