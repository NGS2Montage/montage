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
        var projecthtml = '<table class="table"><thead><tr><th>Project</th><th>Name</th><th>Description</th><th>Observations</th><th>Investigations</th></thead><tbody>';
        for (var i = 0; i < projectArr.length; i++){
          projecthtml += '<tr><td><button type="button" class="submitButton" onclick="updateProj(' + projectArr[i].id + ')">Update</button></td>' +
          '<td><a href="/project/' + projectArr[i].id + '">' + projectArr[i].name + '</a></td><td>' + projectArr[i].description +
          '</td><td><button class="submitButton" type="button" onclick="createObs(' + projectArr[i].id + ', &apos;' + projectArr[i].name + '&apos;)">Make</button>' +
          '<button type="button" class="submitButton" onclick="viewObs(' + projectArr[i].id + ', &apos;' + projectArr[i].name + '&apos;)">View</button></td>' +
          '<td><button class = "submitButton" onclick="createInvs(' + projectArr[i].id + ', &apos;' + projectArr[i].name + '&apos;)">Create</button>' +
          '<button class = "submitButton" onclick="viewInvs(' + projectArr[i].id + ', &apos;' + projectArr[i].name + '&apos;)">View</button></td></tr>';
          //console.log(projectArr[i]);
        }
        projecthtml += '</tdody></table>';
        pview.set("content", projecthtml);
        //document.body.innerHTML += '<div class="updateProj"></div>';
        //return projectArr;
      });
      //var proj = this.store.query({}, {sort: [{attribute: "lastModified", descending: true}]} );
      //console.log(proj);
      //return proj;
    }
    // updateProj: function(proj){
    //   console.log(proj);
    //   console.log(pview);
      //document.body.innerHTML += '<div class="updateProj"></div>';
      //var updateDiv = document.getElementsByClassName('updateProj');
      //console.log(updateDiv[0]);
    // }
  });
});
