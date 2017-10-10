define([
  "dojo/_base/declare", "dojo/_base/lang",
  "dojo/when", "dojo/store/util/QueryResults", "./memory", 'dojo/request'
], function(
  declare, lang,
  when, QueryResults, Memory, request
){
  var _lastId = 6;
  //var projectArr = [];
  request('/api/projects').then(function(data){
    projectArr = data;
    //console.log(projectArr);
  });

  return declare([Memory], {
    data: [
      {id: 1, name: "Some Project1","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(),state: "ready" },
      {id: 2, name: "Some Project2","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "ready"},
      {id: 3, name: "Some Project3","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: false, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(),state: "complete"},
      {id: 4, name: "Some Project4","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "published"},
      {id: 5, name: "Some Project5","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "complete"},
      {id: 6, name: "Some Project6","description": "Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "complete"}
    ],
    //data: JSON.stringify(projectArr),

    add: function(obj){
      obj.id = ++_lastId;
      obj.isActiveFlag = true;
      obj.createdBy = "dmachi";
      obj.modifiedBy = "dmachi";
      obj.createdOn = new Date();
      obj.lastModified = new Date();
      obj.state = "ready";

      return this.inherited(arguments);
    }
  });
});
