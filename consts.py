from sqlalchemy.types import Integer, String, Boolean

SCHEMA = {
    'id': 'int',
    'marca': 'str',
    'modelo': 'str',
    'año': 'int',
    'precio_venta': 'int',
    'costo_vehiculo': 'int',
    'color': 'str',
    'disponible': 'bool',
    'fecha_compra': 'date',
    'kilometraje': 'int'

}

NAME_CHANGE = {
    'fecha_formato': 'fecha_compra'
}

CALCULATIONS = {
    'margen': 'precio_venta - costo_vehiculo',
    'ganancia': 'margen > 0'
}

DB_SCHEMA = {
    'id': "INTEGER",
    'marca': "STRING",
    'modelo': "STRING",
    'año': "INTEGER",
    'precio_venta': "INTEGER",
    'costo_vehiculo': "INTEGER",
    'color': "STRING",
    'disponible': "BOOLEAN",
    'fecha_compra': "STRING",
    'kilometraje': "INTEGER",
    'margen': "INTEGER",
    'ganacia': "BOOLEAN"
}