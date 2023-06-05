class PersonaDao:
    """
    DAO=data access object
    CRUD= create,read,update,delete
    """
    _seleccionar = 'SELECT * FROM persona ORDER BY id_persona'
    _insertar = 'INSERT INTO persona(,nombre,apellido,email)VALUES(,%s,%s,%s)'
    _actualizar = 'UPDATE persona SET nombre = %s,apellido,email=%s,email=%s WHERE id_persona=%s'
    _eliminar = 'DELETE FROM persona WHERE id_persona= %s'
