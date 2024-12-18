import sqlalchemy


# https://docs.sqlalchemy.org/en/14/core/type_basics.html
dict_sqltypes_2_humans = {
    sqlalchemy.sql.sqltypes.Date: 'Data',
    sqlalchemy.sql.sqltypes.DATE: 'Data',
    sqlalchemy.sql.sqltypes.DateTime: 'Data/Hora',
    sqlalchemy.sql.sqltypes.DATETIME: 'Data/Hora',
    sqlalchemy.sql.sqltypes.TIMESTAMP: 'Data/Hora',
    sqlalchemy.sql.sqltypes.Time: 'Hora',
    sqlalchemy.sql.sqltypes.TIME: 'Hora',
    sqlalchemy.sql.sqltypes.Interval: 'Invervalo',
    sqlalchemy.sql.sqltypes.Boolean: 'Booleano',
    sqlalchemy.sql.sqltypes.LargeBinary: 'Booleano',
    sqlalchemy.sql.sqltypes.BLOB: 'Booleano',
    sqlalchemy.sql.sqltypes.BINARY: 'Booleano',
    sqlalchemy.sql.sqltypes.BOOLEAN: 'Booleano',
    sqlalchemy.sql.sqltypes.VARBINARY: 'Booleano',
    sqlalchemy.sql.sqltypes.CHAR: 'Texto',
    sqlalchemy.sql.sqltypes.VARCHAR: 'Texto',
    sqlalchemy.sql.sqltypes.NCHAR: 'Texto',
    sqlalchemy.sql.sqltypes.NVARCHAR: 'Texto',
    sqlalchemy.sql.sqltypes.TEXT: 'Texto',
    sqlalchemy.sql.sqltypes.Text: 'Texto',
    sqlalchemy.sql.sqltypes.CLOB: 'Texto',
    sqlalchemy.sql.sqltypes.String: 'Texto',
    sqlalchemy.sql.sqltypes.Unicode: 'Texto',
    sqlalchemy.sql.sqltypes.UnicodeText: 'Texto',
    sqlalchemy.sql.sqltypes.Enum: 'Texto',
    sqlalchemy.sql.sqltypes.INTEGER: 'Inteiro',
    sqlalchemy.sql.sqltypes.BIGINT: 'Inteiro',
    sqlalchemy.sql.sqltypes.SMALLINT: 'Inteiro',
    sqlalchemy.sql.sqltypes.Integer: 'Inteiro',
    sqlalchemy.sql.sqltypes.SmallInteger: 'Inteiro',
    sqlalchemy.sql.sqltypes.BigInteger: 'Inteiro',
    sqlalchemy.sql.sqltypes.Float: 'Decimal',
    sqlalchemy.sql.sqltypes.FLOAT: 'Decimal',
    sqlalchemy.sql.sqltypes.REAL: 'Decimal',
    sqlalchemy.sql.sqltypes.NUMERIC: 'Decimal',
    sqlalchemy.sql.sqltypes.Numeric: 'Decimal',
    sqlalchemy.sql.sqltypes.DECIMAL: 'Decimal',
    sqlalchemy.sql.sqltypes.ARRAY: 'Array',
    sqlalchemy.sql.sqltypes.JSON: 'Json',
}
