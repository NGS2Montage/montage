var profile = {      
	basePath: "./", 
	layerOptimize: false, /* "closure", */
	cssOptimize:"comments.keepLines",
	releaseDir: "./release",
	stripConsole: "none", /* "all",*/
/*	mini: true, */
	hasReport: true,
	selectorEngine: "lite",
	staticHasFeatures:{
		"dojo-firebug": false,
		"dojo-debug-messages":true,
		'dojo-trace-api':false,
		'dojo-log-api':true,
		"async": true
	},
	plugins: {
		"xstyle/css": "xstyle/build/amd-css"
	},

	packages:[ 
		{ 
			name: "dojo", 
			location: "./dojo" 
		}, 
		{ 
			name: "dijit", 
			location: "./dijit" 
		},
		{ 
			name: "dojox", 
			location: "./dojox" 
		},
		{ 
			name: "morisky", 
			location: "./morisky"
		},
		{ 
			name: "dgrid", 
			location: "./dgrid"
		},
		{ 
			name: "put-selector", 
			location: "./put-selector"
		},
		{ 
			name: "xstyle", 
			location: "./xstyle"
		},
		{ 
			name: "dbind", 
			location: "./dbind"
		},
		{ 
			name: "rql", 
			location: "./rql"
		}

	], 

	layers: {             
		"morisky/layer/core": { 
			include: [ 
				"put-selector/put",
				"dijit/_base",
				"dijit/form/ComboButton",
				"dijit/form/RadioButton",
				"dijit/form/TextBox",
				"dijit/form/Button",
				"dijit/layout/TabContainer",
				"dijit/layout/BorderContainer",
				"dijit/CheckedMenuItem",
				"dijit/form/TextBox",
				"morisky/app/base",
				"morisky/util/jsonrpc",
				"morisky/widget/CreateAssessment",
				"morisky/widget/AssessmentExecutor",
				"morisky/widget/CreateOrganization",
				"morisky/widget/AssessmentGrid",
				"morisky/widget/CreateTest"
			]
		}
	}
};

