import os
os.environ['DATABASE_URL'] = 'sqlite://'

import unittest
from datetime import datetime, timezone, timedelta
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
      
        
    def test_password_hashing(self):
        u = User(username='mark', email='mark@example.com')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
     
        
    def test_avatar(self):
        u = User(username='mark', email='mark@example.com')    
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                        '31b5b1c264dbbc3a54215449b5795e3e'
                                        '?d=identicon&s=128'))
        
        
    def test_follow(self):
        # Setup users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='emily', email='emily@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        following = db.session.scalars(u1.following.select()).all()
        followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(following, [])
        self.assertEqual(followers, [])
        
        # Following
        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 1)
        self.assertEqual(u2.followers_count(), 1)
        u1_following = db.session.scalars(u1.following.select()).all()
        u2_followers = db.session.scalars(u2.followers.select()).all()
        self.assertEqual(u1_following[0].username, 'emily')
        self.assertEqual(u2_followers[0].username, 'john')
        
        # Unfollowing
        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.following_count(), 0)
        self.assertEqual(u1.followers_count(), 0)
        
    
    def test_follow_posts(self):
        # Create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='emily', email='emily@example.com')
        u3 = User(username='ben', email='ben@example.com')
        u4 = User(username='lily', email='lily@example.com')
        db.session.add_all([u1, u2, u3, u4])
        
        # Create four posts
        now = datetime.now(timezone.utc)
        p1 = Post(body="post from john", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from emily", author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from ben", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from lily", author=u4, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()
        
        # Setup the followers
        u1.follow(u2) # john follows emily
        u1.follow(u4) # john follows lily
        u2.follow(u3) # emily follows ben
        u3.follow(u4) # ben follows lily
        db.session.commit()
        
        # Check the following posts of each user
        f1 = db.session.scalars(u1.following_posts()).all()
        f2 = db.session.scalars(u2.following_posts()).all()
        f3 = db.session.scalars(u3.following_posts()).all()
        f4 = db.session.scalars(u4.following_posts()).all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)       
                
        
        
        
            
            
