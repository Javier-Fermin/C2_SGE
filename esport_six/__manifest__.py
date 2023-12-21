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
    "depends": ['base'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'Views/esporst.xml',
        'Views/MatchView.xml',
        'Views/stas_form',
        'Views/stats_tree'
    ],
    "application": True,
    "installable": True,
}