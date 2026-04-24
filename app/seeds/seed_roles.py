from app.db import SessionLocal
from app.models.roles_models import Roles


def seed_roles():
    db = SessionLocal()

    roles = [
    {
        "name": "admin",
        "description": "Full access to all system features and settings"
    },
    {
        "name": "visitor",
        "description": "Regular visitor with limited access to view data"
    },
    {
        "name": "moderator",
        "description": "Can manage and review user-generated content"
    }
]

    for role in roles:
        exists = db.query(Roles).filter(Roles.name == role["name"]).first()

        if not exists:
            role = Roles(
                name=role["name"], 
                description=role["description"]
                )
            db.add(role)

    db.commit()
    db.close()


if __name__ == "__main__":
    seed_roles()
    print("Roles seeded successfully")