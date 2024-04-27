{
    'name': 'Modulo de Consultorios',
    'description': """
        Este módulo sirve para gestionar consultorios, manejar su facturación y sus pagos
    """,
    'category': 'Sales/Sales',
    'version': '15.0.1.0.0',
    'sequence': 32,
    'depends': ['base', 'contacts'],
    'data': [
        'data/disponibilidad_data.xml',
        'security/ir.model.access.csv',
        'views/ias_consultorio_view.xml',
        'views/ias_reservas_view.xml',
        'views/citas_medicas_menu.xml',
    ],
    'demo': [
        
    ],
    'post_init_hook': '_post_init_presidents',
    'license': 'AGPL-3',
    'auto_install': True,
    'application': True,
    'assets': {
    }
}