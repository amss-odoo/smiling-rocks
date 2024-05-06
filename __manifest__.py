{
    'name': 'Smiling Rocks',
    'description': 'Online store for diamond jewellery',
    'category':'Website',
    'version':'1.0',
    'author':'Shashwati',
    'license':'LGPL-3',
    'depends':['website'],
    'data':[
        'data/images.xml',
        'data/presets.xml',
        'data/mega_menu.xml',
        'data/menu.xml',

        'views/header.xml',
        'views/website_templates.xml',
        'views/snippets/options.xml',
        'views/snippets/s_hero.xml',
        'views/snippets/s_light_grid.xml',
        'views/snippets/s_banner.xml',
        'views/snippets/s_blog.xml',

        'data/pages/home.xml',
    ],
    'assets':{
        'web._assets_primary_variables':[
            'rocks/static/src/scss/primary_variables.scss',
        ],
        'web.assets_frontend': [
            'rocks/static/src/scss/font.scss',
            'rocks/static/src/scss/mega_menu.scss',
            'rocks/static/src/snippets/s_hero.scss',
            'rocks/static/src/snippets/s_light_grid.scss',
            'rocks/static/src/snippets/s_banner.scss',
            'rocks/static/src/snippets/s_blog.scss',
        ]
    },
    'installable':'True',
    'application':'True',
}