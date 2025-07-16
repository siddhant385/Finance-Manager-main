from ..config import DB_PATH
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    FloatField,
    DateField,
    TextField,
    Check
)

# 📦 Database setup (change the path if needed)
db = SqliteDatabase(DB_PATH)  # or use full path: "src/db/finance.db"

# 📄 BaseModel to link with the database
class BaseModel(Model):
    class Meta:
        database = db

# 💰 Finance model
class Finance(BaseModel):
    tag = CharField()
    amount = FloatField()
    date = DateField()
    desc = TextField()
    type = CharField(constraints=[Check("type IN ('income', 'expense')")])
