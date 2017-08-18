define([
        "dojo/_base/declare", "dojo/_base/lang",
        "dojo/when", "dojo/store/util/QueryResults", "./memory"
], function(
	declare, lang,
	when, QueryResults, Memory
){
	var _lastId=1;
        return declare([Memory], {
		data: [
			{
				id: 1, 
				project: 1,
				text: " Some Comment",
				createdOn: new Date(1499741483596),
				createdBy: "dmachi"	
			}
		],

		add: function(obj){
			obj.id = ++_lastId;
			obj.createdBy="dmachi";
			obj.modifiedBy="dmachi"
			obj.createdOn=new Date()
			obj.lastModified=new Date()
			return this.inherited(arguments);
		}
	});

});
