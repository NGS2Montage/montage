define([
  "dojo/_base/declare", "dijit/layout/BorderContainer", "dijit/layout/ContentPane",
  "dojo/when", "dojo/_base/lang", "dojo/string", "dojo/text!./template/ProjectOverviewPanel.html",
  "dojo/topic"
], function(
  declare, BorderContainer, ContentPane,
  when, lang, dojoString, POPTemplate,
  Topic
){
  return declare([BorderContainer], {
    store: window.App.store.project,
    startup: function(){
      this.projectHeader = new ContentPane({content: '<table style="width:100%"><tr><td>Projects</td><td></td><td style="text-align:right;"><a class="ApplicationDialogButton" href rel="montage/form/CreateProject:Create New Project">Create New Project</a></td></tr></table>', region: "top"});
      this.addChild(this.projectHeader);
      this.projectsView = new ContentPane({content: '', region: "center"});
      this.addChild(this.projectsView);
      this.inherited(arguments);
      Topic.subscribe("/refreshProjects", lang.hitch(this, "refresh"));
      this.refresh();
    },
    refresh: function(){
      when(this.getProjects(), lang.hitch(this, function(results){
        var out = [];
        results.forEach(function(p){
          //console.log("Project: ", p);
          out.push(dojoString.substitute(POPTemplate, p));
        });
        this.projectsView.set("content", out.join(""));
      }));
    },
    getProjects: function(){
      return this.store.query({}, {sort: [{attribute: "lastModified", descending: true}]} );
    }
  });
});
