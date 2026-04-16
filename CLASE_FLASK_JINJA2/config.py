from urllib.parse import quote_plus

password = quote_plus("123")

SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{password}@localhost:5432/empresa_db"