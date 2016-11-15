L.Control.SidebarButton = L.Control.extend({
    includes: L.Mixin.Events,
    options: {
        style: 'leaflet-control-sidebar-btn',
        position: 'topleft',
        title: '',
        text: null,
        active: false
    },
    initialize: function(options) {
        L.setOptions(this, options);
    },
    getContent: function(){
        return $('<div>' + this.options.title + '</div>');
    },
    onAdd: function(){

        var _this = this;
        var style_class = 'leaflet-bar leaflet-control leaflet-control-sidebar-btn';
        if(this.options.style !== 'leaflet-control-sidebar-btn'){
            style_class += this.options.style;
        }
        var container = $('<div>')
			.attr('class', style_class);
        this._container = container[0];

        this.pane = this.getContent();

		var button = $('<a>')
			.attr('class', 'control-button')
			.attr('href', '#')
			.attr('title', this.options.title)
            .on('click', function(e) {
    			e.stopPropagation();
    			e.preventDefault();
    			_this.options.sidebar.togglePane(_this.pane, button);
    		})
            .appendTo(container);

        if(typeof(this.options.text) !== 'undefined' &&
            this.options.text !== null){
            button.html(this.options.text);
        }

        this.options.sidebar.addPane(this.pane);

        if(this.options.active === true){
            _this.options.sidebar.togglePane(this.pane, button);
        }
        return this._container;
    },

    removeFrom: function(a){
        console.debug('TODO: pendent de fer el removeFrom de L.Control.SidebarButton');
    }

});
