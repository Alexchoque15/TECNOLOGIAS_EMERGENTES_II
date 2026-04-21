import os

uri = os.environ.get("DATABASE_URL")

# Render usa postgres:// → lo convertimos
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

SQLALCHEMY_DATABASE_URI = uri
SQLALCHEMY_TRACK_MODIFICATIONS = False