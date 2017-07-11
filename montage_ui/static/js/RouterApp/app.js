define([
        "dojo/_base/declare", "dojo/parser","dojo/_base/lang",
        "dojo/topic", "dojo/on", "dojo/dom", "dojo/dom-class", "dojo/dom-attr",
        "dijit/registry", "dojo/request", "dijit/layout/ContentPane",
        "dojo/_base/Deferred","dojo/query","dojo/NodeList-dom",
        "dojo/ready", "dojo/parser", "rql/query", "dojo/_base/lang",
        "dijit/Dialog", "dojo/dom-construct","dojo/_base/window",
	"./router","dojo/Stateful","dojo/when"
	
], function(declare, parser,lang,
	Topic, on, dom, domClass, domAttr,
	Registry, xhr, ContentPane,
	Deferred,query,nodeListDom,
	Ready, Parser, rql, lang,
	Dialog, domConstruct,win,
	Router,Stateful,when
){

        return declare([Stateful], {
		panels: {},
		store: null,
		state: null,
		applicationContainer: null,
		applicationContainerID: "ApplicationContainer",
		constructor: function(opts){
			if(opts){
				for(var prop in opts){
					this[prop] = opts[prop]
				}
			}

			if (!this.store){
				this.store={};
			}

			Ready(this, lang.hitch(this,function(){
				query(".showOnLoad").removeClass("dijitHidden");
				console.log("Parse Widgets...")
				Parser.parse().then(lang.hitch(this,function(){
					console.log("Parse Complete.")
					this.startup();
				}));
			}));
    		},

    		startup: function(){
    			console.log("Application Startup()");
			this.watch("state",lang.hitch(this,"onStateChange"));
			console.log("Setup Stores...");
			this.setupStores();
			console.log("Add application routes...");
			this.setupRoutes();
			console.log("Start Router...");
			Router.startup();
			console.log("Setup Listeners...");
	                this.listen();
			console.log("Application Started.");
    		},

		setupStores: function(){

		},

		addStore: function(id,store){
			console.log("Adding Store: ", id);
			this.store[id]=store;
		},

		/* load/require a widget constructor */
                getConstructor: function(cls){
                        var def = new Deferred();
                        require([cls], function(ctor){
                                def.resolve(ctor);
                        });
                        return def.promise;
                },

                getApplicationContainer: function(){
                        if(this.applicationContainer){
                                return this.applicationContainer;
                        }
                        this.applicationContainer = Registry.byId(this.applicationContainerID);
                        return this.applicationContainer;
                },

                getCurrentContainer: function(){
                        var ac = this.getApplicationContainer();
                        var ch = ac.getChildren().filter(function(child){
                                return child.region == "center";
                        });
                        if(!ch || ch.length < 1){
                                console.warn("Unable to find current container");
                                return false;
                        }

                        return ch[0];
                },

		onStateChange: function(property,oldSstate,state){
			console.log("Application Root onStateChange: ", state);
			if (!state){
				console.warn("No State after state change");
				return;
			}

			var appContainer = this.getApplicationContainer();

                        if(state.widgetClass){
                                ctor = this.getConstructor(state.widgetClass)
                        }else{
                                ctor = ContentPane;
                        }

			if (state.requireAuth && (!window.App.user)){
				console.warn("This view requires an authenticated user");
				return;
			}

			when(ctor, lang.hitch(this,function(ctor){
				if (!ctor){
					console.warn("Unable to Load Widget: ", state.widgetClass);
					return;
				}

				var instance,cur;

				var cur = this.getCurrentContainer();

				if (cur instanceof ctor){
					instance=cur;
					instance.set("state", state);

					if (state.widgetParams && (typeof state.widgetParams == "object")){
						Object.keys(state.widgetParams).forEach(function(prop){
							instance.set(prop,state.widgetParams[prop]);
						},this);
					}
					return;
				}else{
					var opts = {
						region: "center",
						state: state
					}
					if (state.widgetParams && (typeof state.widgetParams == "object")){
						Object.keys(state.widgetParams).forEach(function(prop){
							opts[prop]=state.widgetParams[prop];
						},this);
					}
					instance = new ctor(opts);
					if (cur){
						appContainer.removeChild(cur,true);
						cur.destroy();
					}	

					appContainer.addChild(instance);
				}

			}));			
		},

		registerRoute: function(route, callback){
			return Router.register(route, callback);
		},

		setupRoutes: function(){
			console.log("Base setupRoutes() stub");
		},
 
		listen: function(){

			console.log("App Listener Starting...");

			/* listen for clicks that should navigate through the app router */
			on(win.doc, ".ApplicationNavLink:click", lang.hitch(this, function(evt){
				evt.preventDefault();
				evt.stopPropagation();
				var parts = evt.target.href.split(evt.target.pathname);
				Router.go(evt.target.pathname + (parts[1] || ""));
			}));

			on(win.doc, ".ApplicationDialogButton:click", lang.hitch(this, function(evt){
				console.log("DialogButton Click()");
				evt.stopPropagation();
				evt.preventDefault();
				var rel = domAttr.get(evt.target,"rel");
				var parts = rel.split(":");

				var ctor = parts.shift();
				var opts = parts.join(":");

				console.log("ctor: ", ctor, "opts: ", opts)

				if (opts && opts.charAt(0)=="{"){
					opts = JSON.parse(opts);
				}else{
					var title = opts||"";
				}

				console.log("DialogButton Click", rel);

				if (!this._dialog){
					this._dialog = new Dialog({title: title});

					on(this._dialog.domNode, "refreshed", lang.hitch(this,function(evt){
						console.log("Dialog caught refreshed event")
						this._dialog.resize();
					}));
				}else{
					this._dialog.set("title", title);
				}

				var dlg = this._dialog;

				this.getConstructor(ctor).then(lang.hitch(this,function(ctor){
					var w = new ctor((opts && typeof opts=="object")?opts:{});

					if (w.title){
						this._dialog.set('title', w.title);
					}
					domConstruct.empty(dlg.containerNode);
					domConstruct.place(w.domNode,dlg.containerNode,"first");
					w.startup();
					dlg.show();
				}))
			}))

			on(window, "dialogAction", lang.hitch(this, function(evt){
				if (this._dialog){
					this._dialog.hide();
				}
			}))
	
		}
    	})
});
