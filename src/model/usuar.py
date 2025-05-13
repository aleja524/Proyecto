class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la pensión en la aplicación
    """
    def __init__(self, nombre:str, apellido:str, documento_identidad:int, correo:str, telefono: int):
        self.nombre = nombre
        self.apellido = apellido
        self.documeto_identidad = documento_identidad
        self.correo = correo
        self.telefono = telefono

    def esIgual( self, comparar_con ) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert( self.nombre == comparar_con.nombre )
        assert( self.apellido == comparar_con.apellido )
        assert( self.documeto_identidad == comparar_con.documento_identidad )
        assert( self.correo == comparar_con.correo )
        assert( self.telefono == comparar_con.telefono )
        return True