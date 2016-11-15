var MOSQUITO = (function (m) {

    var ControlMoreinfo = L.Control.SidebarButton.extend({
        options: {
            style: 'leaflet-control-moreinfo-btn',
            position: 'topleft',
            title: 'leaflet-control-moreinfo-btn',
            text: '',
            active: false
        },

        getContent: function(){
            var container = $('<div>')
              .attr('class', 'sidebar-control-moreinfo');
            container.html( $('#content-control-moreinfo-tpl').html());

            return container;
        }

    });

    m.control = m.control || {};
    m.control.ControlMoreinfo = ControlMoreinfo;

    return m;

}(MOSQUITO || {}));
