define([
        "dojo/_base/declare", "dojo/_base/lang",
        "dojo/when", "dojo/store/util/QueryResults", "./memory"
], function(
	declare, lang,
	when, QueryResults, Memory
){
        return declare([Memory], {
		data: [
			{id: 1, name: "Some Project1","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(),state: "ready" },
			{id: 2, name: "Some Project2","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "ready"},
			{id: 3, name: "Some Project3","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: false, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(),state: "complete"},
			{id: 4, name: "Some Project4","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "published"},
			{id: 5, name: "Some Project5","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "complete"},
			{id: 6, name: "Some Project6","description":"Donec ullamcorper nulla non metus auctor fringilla. Curabitur blandit tempus porttitor. Morbi leo risus, porta ac consectetur ac, vestibulum at eros.",isActiveFlag: true, createdBy: "dmachi",modifiedBy: "dmachi", createdOn: new Date(),lastModified: new Date(), state: "complete"}
		]
	});

});
