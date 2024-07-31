from app import app, db
from app.models import User, Post

def cleanup_fake_data():
    Post.query.delete()
    User.query.delete()
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        cleanup_fake_data()
