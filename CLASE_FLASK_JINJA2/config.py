from urllib.parse import quote_plus
import os

password = quote_plus("123")

SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{password}@localhost:5432/empresa_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False