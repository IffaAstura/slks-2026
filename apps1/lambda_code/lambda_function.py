import pymysql
import os
import json

# Environment variables
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_pass = os.environ['DB_PASS']
db_name = os.environ['DB_NAME']

def lambda_handler(event, context):
    try:
        # Parse JSON body
        body = json.loads(event['body'])
        nama = body.get('nama', '')
        kelas = body.get('kelas', '')
        sekolah = body.get('sekolah', '')
        gender = body.get('gender', '')

        # Validasi dasar (opsional)
        if not (nama and kelas and sekolah and gender):
            return {
                "statusCode": 400,
                "body": json.dumps("Semua field harus diisi.")
            }

        # Connect DB
        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_pass,
            db=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        create_table_if_not_exists(conn)
        insert_data(conn, nama, kelas, sekolah, gender)
        conn.close()

        return {
            "statusCode": 200,
            "body": json.dumps(f"Berhasil menambahkan data: {nama}")
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(f"Terjadi kesalahan: {str(e)}")
        }

def create_table_if_not_exists(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nama VARCHAR(100),
                kelas VARCHAR(50),
                sekolah VARCHAR(100),
                gender VARCHAR(20)
            );
        """)
    conn.commit()

def insert_data(conn, nama, kelas, sekolah, gender):
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO users (nama, kelas, sekolah, gender)
            VALUES (%s, %s, %s, %s)
        """, (nama, kelas, sekolah, gender))
    conn.commit()
