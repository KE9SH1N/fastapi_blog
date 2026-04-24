from app.db import SessionLocal
from app.seeds.seed_roles import seed_roles


def run_all_seeds():
    db = SessionLocal()

    seed_roles()

    db.commit()
    db.close()


if __name__ == "__main__":
    run_all_seeds()
    print("Seeding completed")