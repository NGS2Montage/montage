
var proj = {};
/* eslint-disable */
var updateProj = function(projid){
  console.log(projid);
  fetch('/api/projects/' + projid + '/')
  .then((resp) => resp.json())
  .then((data) => {
    proj = data;
    console.log(proj);
    var upf = document.getElementsByClassName('updateProjForm');
    upf[0].style.display = 'block';
    upf[0].innerHTML = '<h2>Update Project</h2><form><label>Name</label><input class="updateprojinputs" name="projname" value="' + proj.name + '"><br><label>Description</label><input class="updateprojinputs" name ="projdesc" value ="' + proj.description +
    '"><button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="putProj()">Update</button>' +
    '<button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="cancelProj()">Cancel</button></form>';
    upf[0].scrollIntoView();
  });
};

var cancelProj = function(){
  var upf = document.getElementsByClassName('updateProjForm');
  upf[0].style.display = 'none';
  document.body.scrollTop = document.documentElement.scrollTop = 0;
};
/* eslint-enable */
var getCookieToken = function(){
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
  return cookieToken;
};
/* eslint-disable */
var putProj = function(){
  var inputs = document.getElementsByClassName('updateprojinputs');
  console.log(inputs);
  var bodyData = {'name': inputs[0].value, 'description': inputs[1].value, 'team': 1, 'investigations': [], 'project_state': 1 };
  var cookieToken = getCookieToken();
  var fetchData = {
    method: 'PUT',
    credentials: 'same-origin',
    body: JSON.stringify(bodyData),
    headers: {'X-CSRFTOKEN': cookieToken,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
};
console.log('trying to put project');
console.log(fetchData);
fetch('/api/projects/' + proj.id + '/', fetchData)
.then((data) => {
  console.log(data);
  location.reload();
});
};

var createObs = function(projid, projname){
  console.log(projid);
  console.log(projname);
  var upf = document.getElementsByClassName('updateProjForm');
  upf[0].style.display = 'block';
  upf[0].innerHTML = '<h2>Make Observation for ' + projname + '</h2><form>' +
  '<textarea rows="4" cols="50" class="obscom" name="obscom" value="">Enter comments</textarea>' +
  '<button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="postObs(' + projid + ')">Submit</button>' +
  '<button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="cancelProj()">Cancel</button></form>';
  upf[0].scrollIntoView();
};

var postObs = function(projid){
  var comments = document.getElementsByClassName('obscom');
  var bodyData = {'comment': comments[0].value, 'project': projid };
  var cookieToken = getCookieToken();
  var fetchData = {
    method: 'POST',
    credentials: 'same-origin',
    body: JSON.stringify(bodyData),
    headers: {'X-CSRFTOKEN': cookieToken,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }
};
fetch('/api/observations/', fetchData)
.then((data) => {
  console.log(data);
  cancelProj();
});
};

var viewObs = function(projid, projname){
  console.log(projid);
  console.log(projname);
  var upf = document.getElementsByClassName('updateProjForm');
  upf[0].style.display = 'block';
  upf[0].style.margin = 'auto';
  upf[0].innerHTML = '<h2>Current Observations for ' + projname + '</h2>';
  fetch('/api/observations/?project=' + projid)
  .then((resp) => resp.json())
  .then((data) => {
    console.log(data);
    upf[0].innerHTML += '<textarea rows="6" cols="50">' + JSON.stringify(data) + '</textarea>';
    upf[0].scrollIntoView();
  })
  .catch((error) => {
    console.log(error);
  });
};

var createInvs = function(projid, projname){
  console.log(projid);
  console.log(projname);
  var upf = document.getElementsByClassName('updateProjForm');
  upf[0].style.display = 'block';
  upf[0].innerHTML = '<h2>Create Investigations for ' + projname + '</h2><form>' +
  '<label>Name </label><input class="invsname" name="invsname" value="">' +
  '<button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="postInvs(' + projid + ')">Submit</button>' +
  '<button style="cursor:pointer; cursor:hand;" onmouseout="this.style.backgroundColor=&apos;#f2f2f2&apos;" onmouseover="this.style.backgroundColor=&apos;#99ddff&apos;" type="button" onclick="cancelProj()">Cancel</button></form>';
  upf[0].scrollIntoView();
};

var postInvs = function(projid){
  var name = document.getElementsByClassName('invsname');
  var bodyData = {'name': name[0].value, 'project': projid, 'investigation_status': 1,
  "analysis": [],
  "experiments": [],
  "hypotheses": [],
  "mechanisms": [],
  "models": [],
  "theories": []
};
var cookieToken = getCookieToken();
var fetchData = {
  method: 'POST',
  credentials: 'same-origin',
  body: JSON.stringify(bodyData),
  headers: {'X-CSRFTOKEN': cookieToken,
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}
};
fetch('/api/investigations/', fetchData)
.then((data) => {
  console.log(data);
  cancelProj();
});
};

var viewInvs = function(projid, projname){
  console.log(projid);
  console.log(projname);
  var upf = document.getElementsByClassName('updateProjForm');
  upf[0].style.display = 'block';
  upf[0].style.margin = 'auto';
  upf[0].innerHTML = '<h2>Current Investigations for ' + projname + '</h2>';
  fetch('/api/investigations/?project=' + projid)
  .then((resp) => resp.json())
  .then((data) => {
    console.log(data);
    upf[0].innerHTML += '<textarea rows="6" cols="50">' + JSON.stringify(data) + '</textarea>';
    upf[0].scrollIntoView();
  })
  .catch((error) => {
    console.log(error);
  });
};
/* eslint-enable */