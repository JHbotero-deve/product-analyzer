import os
import psycopg2

def init_database():
    \"\"\"Ejecuta los scripts SQL de inicialización.\"\"\"
    try:
        # Soporte para DATABASE_URL (Producción) o parámetros individuales (Local)
        db_url = os.getenv(\"DATABASE_URL\")
        if db_url:
            conn = psycopg2.connect(db_url)
        else:
            conn = psycopg2.connect(
                host=os.getenv(\"DB_HOST\", \"db\"),
                port=os.getenv(\"DB_PORT\", \"5432\"),
                dbname=os.getenv(\"DB_NAME\", \"productos_db\"),
                user=os.getenv(\"DB_USER\", \"productos_user\"),
                password=os.getenv(\"DB_PASSWORD\", \"productos_pass\"),
            )
        
        cursor = conn.cursor()
        
        sql_files = [
            \"sql/001_schema.sql\",
            \"sql/002_monetization.sql\",
            \"sql/003_3d_models.sql\"
        ]
        
        for sql_file in sql_files:
            try:
                # Ajuste de ruta para encontrar la carpeta /sql desde /app
                path_to_sql = os.path.join(os.path.dirname(__file__), \"..\", sql_file)
                with open(path_to_sql, 'r') as f:
                    sql_script = f.read()
                    cursor.execute(sql_script)
                    print(f\"✓ Ejecutado: {sql_file}\")
            except Exception as e:
                print(f\"⚠ Error en {sql_file}: {e}\")
                conn.commit()
                
        cursor.close()
        conn.close()
        print(\"✓ Base de datos inicializada correctamente\")
    except Exception as e:
        print(f\"✗ Error al inicializar BD: {e}\")

if __name__ == \"__main__\":
    init_database()
