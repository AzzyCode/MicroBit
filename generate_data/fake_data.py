import random
from faker import Faker
from datetime import datetime, timezone
from app import app, db
from app.models import User, Post

def generate_fake_users(count=10):
    fake = Faker()
    for _ in range(count):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        about_me = fake.sentence()
        last_seen = datetime.now(timezone.utc)
        
        user = User(
            username=username,
            email=email,
            about_me = about_me,
            last_seen = last_seen,
        )
        user.set_password(password)

        db.session.add(user)
    db.session.commit()
    
    
def generate_fake_posts(count=10):
    fake = Faker()
    user = [user.id for user in User.query.all()]
    
    for _ in range(count):
        body = fake.text(max_nb_chars=140)
        timestamp = datetime.now(timezone.utc)
        user_id = random.choice(user)
        
        post = Post(body=body, timestamp=timestamp, user_id = user_id)
        
        db.session.add(post)
        
    db.session.commit()
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        generate_fake_users(15)
        generate_fake_posts(200)
        
        
        
        
