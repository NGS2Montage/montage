define([
        "dojo/_base/declare", "dojo/_base/lang",
        "dojo/when", "dojo/store/util/QueryResults", "./memory"
], function(
	declare, lang,
	when, QueryResults, Memory
){
        return declare([Memory], {
		data: [
			{
				id: 1, 
				project: 1,
				status: "completed",
				theories: [],
				hypothesis: [],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741483596),
				lastModified: new Date(1499741483596),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 2, 
				project: 1,
				status: "completed",
				theories: [],
				hypothesis: [],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741644657),
				lastModified: new Date(1499741644657),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 3, 
				project: 1,
				status: "editable",
				theories: [],
				hypothesis: [],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741755713),
				lastModified: new Date(1499741755713),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			}
		]
	});

});
