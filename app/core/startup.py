from app.db import SessionLocal
from app.seeds.run_seeds import run_all_seeds


def startup_seed():
    db = SessionLocal()

    try:
        run_all_seeds()
        db.commit()

    finally:
        db.close()