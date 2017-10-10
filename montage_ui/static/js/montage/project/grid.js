define([
  "dojo/_base/declare", "dijit/layout/BorderContainer", "dijit/layout/ContentPane",
  "dojo/when", "dojo/_base/lang", "dojo/string", "dojo/text!./template/ProjectOverviewPanel.html",
  "dojo/topic", 'dojo/request'
], function(
  declare, BorderContainer, ContentPane,
  when, lang, dojoString, POPTemplate,
  Topic, request
){
  //var projectsArr = [];
  return declare([BorderContainer], {
    store: window.App.store.project,
    startup: function(){
      this.projectHeader = new ContentPane({content: '<table style="width:100%"><tr><td>Projects</td><td></td><td style="text-align:right;"><a class="ApplicationDialogButton" href rel="montage/form/CreateProject:Create New Project">Create New Project</a></td></tr></table>', region: "top"});
      this.addChild(this.projectHeader);
      this.projectsView = new ContentPane({content: '', region: "center"});
      this.addChild(this.projectsView);
      this.inherited(arguments);
      this.projectsArr = [];
      Topic.subscribe("/refreshProjects", lang.hitch(this, "refresh"));
      //this.refresh();
      this.getProjects(this.projectsView);
    },
    refresh: function(){
      when(this.getProjects(this.projectsView), lang.hitch(this, function(results){
        //var out = [];
        //console.log(results);
        // results.forEach(function(p){
        //   //console.log("Project: ", p);
        //   out.push(dojoString.substitute(POPTemplate, p));
        // });

        //this.projectsView.set("content", projectArr.join(""));
      }));
    },
    getProjects: function(pview){
      var projectArr = [];
      request('/api/projects').then((data) => {
        //this.projectsArr = data;
        projectArr = JSON.parse(data);
        //this.projectsView.set("content", projectArr.join(""));
        console.log(projectArr);
        var projecthtml = '';
        for (var i = 0; i < projectArr.length; i++){
          projecthtml += '<p>Description: <a style="color:#0000ff; text-decoration:underline" href="/project/' + projectArr[i].id + '">' + projectArr[i].description + '<a></p>';
          //console.log(projectArr[i]);
        }
        pview.set("content", projecthtml);
        //return projectArr;
      });
      //var proj = this.store.query({}, {sort: [{attribute: "lastModified", descending: true}]} );
      //console.log(proj);
      //return proj;
    }
  });
});
