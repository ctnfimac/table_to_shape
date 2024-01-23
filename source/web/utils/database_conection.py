import psycopg2 

class DatabaseConection:
    """
    Clase usando patron Singleton para la instancia de las credenciales de la base de datos
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DatabaseConection, cls).__new__(cls)

        if len(args) == 1:
            cls._instance.host = args[0]['host']
            cls._instance.port = args[0]['port']
            cls._instance.user = args[0]['user']
            cls._instance.database = args[0]['dbname']
            cls._instance.password = args[0]['password']
        return cls._instance
    
    def credentials(self) -> dict:
        return {
            "host": self._instance.host,
            "dbname": self._instance.database,
            "port": self._instance.port,
            "user": self._instance.user,
            "password": self._instance.password 
        }
    
    def credentials_sqlalchemy(self) -> str:
        return f"postgresql://{self._instance.user}:{self._instance.password}@database:{self._instance.port}/{self._instance.database}"
    

    def test_conection_postgresql(self):
        conn = psycopg2.connect(**self.credentials())
        conn.close()

    def get_schemas(self) -> list:
        conn = psycopg2.connect(**self.credentials())
        cur = conn.cursor()
        cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('tiger_data', 'tiger', 'topology', 'information_schema', 'pg_catalog', 'pg_toast');")
        records = cur.fetchall()
        return records

    def get_tables(self, schema:str='public') -> list:
        conn = psycopg2.connect(**self.credentials())
        cur = conn.cursor()
        cur.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{schema}' AND table_name not in ('geography_columns','geometry_columns','spatial_ref_sys') ORDER BY table_name DESC;")
        records = cur.fetchall()
        return records