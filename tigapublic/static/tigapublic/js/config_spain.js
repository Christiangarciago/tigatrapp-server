var MOSQUITO = (function (m, _) {
    m.config = _.extend(m.config || {}, {
        roles: {
            "notification": ['superexpert','gestors','notifier','supermosquito']
        },
        lngs: ['es', 'ca', 'en'],
        lngs_admin: ['es'],
        default_lng: ['es'],

        URL_API: '/tigapublic/',
        URL_PUBLIC: '/tigapublic/',

        lon: 1.130859375,
        lat: 37.53097889440026,
        maxzoom_cluster: 13,
        zoom: 5,
        login_allowed: true,
        embeded: window !== parent,
        minZoom: 1,

        default_layers: 'A',
        printreports:true,
        maxPrintReports: 300,
        "groups":[
            {'name': 'none', 'icon':''}
        ]
        ,
        "layers": [
            {
                key: 'A',
                group:'none',
                title: 'layer.tiger',
                categories: {
                  'albopictus_2': ['mosquito_tiger_probable', 'mosquito_tiger_confirmed']
                }
            },
            {
                key: 'B',
                group:'none',
                title: 'layer.zika',
                categories: {
                  'aegypti_2': ['yellow_fever_probable', 'yellow_fever_confirmed']
                }
            },
            {
                key: 'C',
                group:'none',
                title: 'layer.other_species',
                categories: {
                  'noseparece': ['other_species']
                }
            },
            {
                key: 'D',
                group:'none',
                title: 'layer.unidentified',
                categories: {
                  'nosesabe': ['unidentified']
                }
            },
            {
                key: 'E',
                group:'none',
                title: 'layer.site',
                categories: {
                  'site_water': ['storm_drain_water'],
                  'site_dry': ['storm_drain_dry'],
                }
            },
            {
              'key': 'I',
              'group': 'none',
              'title': 'layer.predictionmodels',
              'deviation_min_zoom': 7,
              'prob_ranges': [
                {'minValue':0, 'maxValue':0.1, 'color': 'rgba(255,255,178,0.5)', 'label': 'models.label.prob-1'},
                {'minValue':0.1, 'maxValue':0.2, 'color': 'rgba(254,204,92,0.5)', 'label': 'models.label.prob-2'},
                {'minValue':0.2, 'maxValue':0.3, 'color': 'rgba(253,141,60,0.5)', 'label': 'models.label.prob-3'},
                {'minValue':0.3, 'maxValue':1, 'color': 'rgba(227,26,28,0.5)', 'label': 'models.label.prob-4'}
              ],
              'sd_ranges': [
                {'minValue':0, 'maxValue':0.05, 'color': '#fff', 'label': 'models.label.sd-1'},
                {'minValue':0.05, 'maxValue':0.1, 'color': '#c8b2b2', 'label': 'models.label.sd-2'},
                {'minValue':0.1, 'maxValue':0.15, 'color': '#8f8c8c', 'label': 'models.label.sd-3'},
                {'minValue':0.15, 'maxValue':1, 'color': '#000', 'label': 'models.label.sd-4'}
              ]

            },
            {
                key: 'F',
                group: 'none',
                title: 'layer.userfixes',
                'style': { // Default style for all items on this layer
                    //'color': 'red',
                    'color': 'green',
                    //'strokecolor': 'rgb(120,198,121)',
                    'strokecolor': 'rgb(120,198,121)',
                    'weight': 0.1,
                    'opacity': 0.8,
                    'fillColor': 'red',
                    'fillOpacity': 0.8
                },
                'segmentationkey': 'color', // name of the attribute that will be used to paint the different segments (color, opacity)
                'segments': [
                  {
                      "from": 0,
                      "to": 9,
                      "color": '65,171,93', // VERD
                      'opacity': 0.2 // only used when "segmentationkey" equals "opacity"
                    },{
                      "from": 10,
                      "to": 99,
                      "color": "35,132,67", //VERD
                      "opacity": 0.4
                    },{
                      "from": 100,
                      "to": 999,
                      "color": "0,104,55", //VERD
                      "opacity": 0.6
                    },{
                      "from": 1000,
                      "color": "0,69,41", //VERD
                      "opacity": 0.8
                    }
                ]
            }
        ],
        "logged": {
            "managers_group":['gestors'],
            "superusers_group":['supermosquito'],
            "epidemiologist_edit_group":['epidemiologist'],
            "epidemiologist_view_group":['epidemiologist_viewer'],
            "lngs": ['es'],
            "groups":[
                {'name': 'observations', 'icon': 'fa fa-mobile'},
                {'name': 'userdata', 'icon':'fa fa-user'},
                {'name': 'none', 'icon':''}
            ],
            "layers": [
              {
                  key: 'A2',
                  group:'observations',
                  title: 'layer.mosquito_tiger_confirmed',
                  categories: {
                    'albopictus_2': ['mosquito_tiger_confirmed']
                  }
              },
              {
                  key: 'A1',
                  group:'observations',
                  title: 'layer.mosquito_tiger_probable',
                  categories: {
                    'albopictus_1': ['mosquito_tiger_probable']
                  }
              },
              {
                  key: 'B2',
                  group:'observations',
                  title: 'layer.yellow_fever_confirmed',
                  categories: {
                    'aegypti_2': ['yellow_fever_confirmed']
                  }
              },
              {
                  key: 'B1',
                  group:'observations',
                  title: 'layer.yellow_fever_probable',
                  categories: {
                    'aegypti_1': ['yellow_fever_probable']
                  }
              },
              {
                  key: 'C',
                  group:'observations',
                  title: 'layer.other_species',
                  categories: {
                    'noseparece': ['other_species']
                  }
              },
              {
                  key: 'D',
                  group:'observations',
                  title: 'layer.unidentified',
                  categories: {
                    'nosesabe': ['unidentified']
                  }
              },
              {
                  key: 'Q',
                  group: 'userdata',
                  title: 'layer.drainstorm',
                  categories: {
                    'drainstorm': ['water', 'nowater']
                  },
                  radius:{'15':3, '17':4, '18':6, '19':8},//PAir values: zoom level, px size,
                  stroke: {'14':0, '19':1},
                  strokecolor: 'rgba(0,0,0,0.5)',
                  strokewidth: 1
              },
              {
                  key: 'P',
                  group:'userdata',
                  title: 'layer.epidemiology',
                  categories: {
                    'state': ['suspected', 'confirmed']
                  },
                  default_palette: 'patient_states',
                  palettes:{
                      'patient_states':{
                          'name': 'patient_states',//select value
                          'column': 'patient_state',
                          'type':'qualitative',
                          'images':{
                              //Key vaues Witout accents
                              //This order will show on the epi layer legend
                              'confirmat_den': {'img':'img/epi_confirmed_den.svg', 'subgroup':'confirmat'},
                              'confirmat_wnv':{'img':'img/epi_confirmed_wnv.svg','subgroup': 'confirmat'},
                              'confirmat_yf':{'img':'img/epi_confirmed_yf.svg', 'subgroup': 'confirmat'},
                              'confirmat_zk':{'img':'img/epi_confirmed_zk.svg', 'subgroup': 'confirmat'},
                              'confirmat_chk':{'img':'img/epi_confirmed_chk.svg', 'subgroup': 'confirmat'},
                              'confirmat':{'img':'img/epi_confirmed_undefined.svg', 'subgroup': 'confirmat'},
                              'probable': {'img':'img/epi_likely.svg'},
                              'sospitos': {'img':'img/epi_suspected.svg'},
                              'no_cas': {'img':'img/epi_nocase.svg'},
                              'indefinit': {'img':'img/epi_none.svg'},
                          }
                      }
                  }
              },
              {
                  key: 'G',
                  group:'observations',
                  title: 'layer.unclassified',
                  categories: {
                    'unclassified': ['not_yet_validated']
                  },
                  private:true
              },
              {
                  key: 'E',
                  title: 'layer.site',
                  group:'observations',
                  categories: {
                    'site_water': ['storm_drain_water'],
                    'site_dry': ['storm_drain_dry'],
                    'site_other': ['breeding_site_other'],
                    'site_pending': ['breeding_site_not_yet_filtered']
                  },
                  private:true
              },
              {
                  key: 'H',
                  group:'observations',
                  title: 'layer.trash_layer',
                  categories: {
                    'trash': ['trash_layer']
                  },
                  private:true
              },
              {
                'key': 'I',
                'group': 'none',
                'title': 'layer.predictionmodels',
                'deviation_min_zoom': 7,
                'prob_ranges': [
                  {'minValue':0, 'maxValue':0.1, 'color': 'rgba(255,255,178,0.5)', 'label': 'models.label.prob-1'},
                  {'minValue':0.1, 'maxValue':0.2, 'color': 'rgba(254,204,92,0.5)', 'label': 'models.label.prob-2'},
                  {'minValue':0.2, 'maxValue':0.3, 'color': 'rgba(253,141,60,0.5)', 'label': 'models.label.prob-3'},
                  {'minValue':0.3, 'maxValue':1, 'color': 'rgba(227,26,28,0.5)', 'label': 'models.label.prob-4'}
                ],
                'sd_ranges': [
                  {'minValue':0, 'maxValue':0.05, 'color': '#fff', 'label': 'models.label.sd-1'},
                  {'minValue':0.05, 'maxValue':0.1, 'color': '#c8b2b2', 'label': 'models.label.sd-2'},
                  {'minValue':0.1, 'maxValue':0.15, 'color': '#8f8c8c', 'label': 'models.label.sd-3'},
                  {'minValue':0.15, 'maxValue':1, 'color': '#000', 'label': 'models.label.sd-4'}
                ]
              },
              {
                  key: 'F',
                  group: 'none',
                  title: 'layer.userfixes',
                  'style': { // Default style for all items on this layer
                      'color': 'red',
                      'strokecolor': 'rgb(194,230,153)',
                      'weight': 0.1,
                      'opacity': 0.8,
                      'fillColor': 'red',
                      'fillOpacity': 0.8
                  },
                  'segmentationkey': 'color', // name of the attribute that will be used to paint the different segments (color, opacity)
                  'segments': [
                    {
                        "from": 0,
                        "to": 9,
                        "color": '65,171,93', // VERD
                        'opacity': 0.2 // only used when "segmentationkey" equals "opacity"
                      },{
                        "from": 10,
                        "to": 99,
                        "color": "35,132,67", //VERD
                        "opacity": 0.4
                      },{
                        "from": 100,
                        "to": 999,
                        "color": "0,104,55", //VERD
                        "opacity": 0.6
                      },{
                        "from": 1000,
                        "color": "0,69,41", //VERD
                        "opacity": 0.8
                      }
                  ]
              }
            ]
        }
    });

    return m;

}(MOSQUITO || {}, _));
