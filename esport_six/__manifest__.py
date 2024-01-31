{
    "name": "Esports Six",
    "version": "1.0.0",
    "category": "esports",
    'author': "G5",
    'summary': """
            Nueva aplicacion para la gestión de esports de Rainbow Six
        """,
    'description': """
            Aplicación para gestión de esports de Rainbow Six, a su vez como un seguimiento de estadisticas.
        """,
    "license": "AGPL-3",
    "depends": ['base','hr'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/MatchView.xml',
        'views/stats_form.xml',
        'views/stats_kanban.xml',
        'views/stats_tree.xml',
        'views/esporst.xml',
        'views/res_users_form_ext.xml',
        'views/res_users_tree_ext.xml',
        'report/report_stats.xml'
    ],
    "application": True,
    "installable": True,
    #"icon":/repo/C2_SGE/esport_six/static/description/icon.png,
}