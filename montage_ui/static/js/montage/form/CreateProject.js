define([
  "dojo/_base/declare", "./base", "dojo/on", "dojo/dom-construct",
  "dojo/dom-class", "dojo/text!./template/CreateProject.html",
  "dojo/request","dijit/form/ValidationTextBox","dojo/topic","dojo/_base/lang",
  "dijit/form/CheckBox","dijit/form/Select","dijit/form/Button","dojo/query",
  "dojo/when",'dojo/request'
], function(
  declare, FormBase, on, domConstruct,
  domClass, Template,
  Request,ValidationTextBox, Topic,lang,
  CheckBox,Select,Button,Query,
  when,request
){
  return declare([FormBase], {
    templateString: Template,
    availableTests: null,

    constructor: function(){
      this.store = window.App.store.project;
    },

    startup: function(){
      if (this._started) { return; }
      this.inherited(arguments);
    },

    onSubmit: function(evt){
      var _self = this;
      var values;
      var newProject = {};
      evt.preventDefault();
      evt.stopPropagation();
      if (this.validate()){
        values = this.getValues();
        this.showMessage('working');
        console.log('Form is Valid!', values);
        newProject = {
          'description': values.description,
          'team': 1,
          'project_state': 1,
          'investigations': []
        };
        //console.log(newProject);
        //console.log(document.cookie);
        //get cookie
        var name = 'csrftoken=';
        var cookieToken = '';
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) === ' ') {
            c = c.substring(1);
          }
          if (c.indexOf(name) === 0) {
            cookieToken = c.substring(name.length, c.length);
          }
        }
        request('/api/projects/', {
          method: 'post',
          // mode: 'cors',
          headers: {'X-CSRFTOKEN': cookieToken,
            'Accept': 'application/json',
            'Content-Type': 'application/json'},
          data: JSON.stringify(newProject)
        })
        .then((data) => {
          console.log(data);
        });

        when(this.store.add(values), function(){
          _self.showMessage('complete');

          on.emit(_self.domNode, 'DialogAction', {
            bubbles: true,
            cancelable: true,
            action: 'close'
          });

          Topic.publish('/refreshProjects');
        }, function(err){
          _self.showMessage('error', 'Error: ' + err);
        });
      } else {
        console.log("Form is incomplete");
      }
    },
    onCancel: function(){
      console.log("CreateProject onCancel()");
      this.inherited(arguments);
    }
  });
});
