define([
        "dojo/_base/declare", "dojo/_base/lang",
        "dojo/when", "dojo/store/util/QueryResults", "./memory"
], function(
	declare, lang,
	when, QueryResults, Memory
){
		var _lastId=7;
        return declare([Memory], {
		data: [
			{
				id: 1, 
				project: 1,
				status: "completed",
				theories: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				hypotheses: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				mechanisms: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
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
				theories: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				hypotheses: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				mechanisms: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
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
				theories: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				hypotheses: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				},
				{
					referenceId: null,
					text: "Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nulla vitae elit libero, a pharetra augue. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec sed odio dui. Praesent commodo cursus magna, vel scelerisque nisl consectetur et."
				}],
				mechanisms: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				models: [{
					type: "intersim-im-11-1",
					params: {
						"networkFile": "https://rafter.bi.vt.edu/volumesvc/.....",
						"fixedRandomSeed": 14,
						"maximumNumTimeStepsPerRun": 100,
						"numRunsPerSimulation": 20
					},
					state: "ready",
					instance: {}
				}],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741755713),
				lastModified: new Date(1499741755713),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 4, 
				project: 3,
				status: "completed",
				theories: [],
				hypotheses: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				},
				{
					referenceId: null,
					text: "Donec ullamcorper nulla non metus auctor fringilla. Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Maecenas faucibus mollis interdum. Vestibulum id ligula porta felis euismod semper. Maecenas sed diam eget risus varius blandit sit amet non magna. Nulla vitae elit libero, a pharetra augue. Donec sed odio dui. Maecenas faucibus mollis interdum. Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Duis mollis, est non commodo luctus, nisi erat porttitor ligula, eget lacinia odio sem nec elit. Nulla vitae elit libero, a pharetra augue. Curabitur blandit tempus porttitor. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Nullam quis risus eget urna mollis ornare vel eu leo. Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo. Donec sed odio dui. Aenean lacinia bibendum nulla sed consectetur."
				}],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741755713),
				lastModified: new Date(1499741755713),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 5, 
				project: 4,
				status: "completed",
				theories: [],
				hypotheses: [],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741755713),
				lastModified: new Date(1499741755713),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 6, 
				project: 5,
				status: "completed",
				theories: [{
					referenceId: null,
					text: "Vestibulum id ligula porta felis euismod semper. Cras mattis consectetur purus sit amet fermentum. Nullam quis risus eget urna mollis ornare vel eu leo."
				}],
				hypotheses: [],
				mechanisms: [],
				models: [],
				experiments: [],
				analysis: [],
				confirmatory: false,
				createdOn: new Date(1499741755713),
				lastModified: new Date(1499741755713),
				createdBy: "dmachi",
				modifiedBy: "dmachi"	
			},
			{
				id: 7, 
				project: 6,
				status: "completed",
				theories: [],
				hypotheses: [],
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
		],

		add: function(obj){
			obj.id = ++_lastId;
			obj.createdBy="dmachi";
			obj.modifiedBy="dmachi"
			obj.createdOn=new Date()
			obj.lastModified=new Date()
			obj.status="editable";
			obj.theories = [];
			obj.hypotheses = [];
			obj.mechanisms = [];
			obj.models = [];
			obj.experiments = [];
			obj.analysis = [];
			obj.confirmatory = false;

			console.log("Add Investigation: ", obj);
			return this.inherited(arguments);

		}
	});

});
