import os
os.environ['DATABASE_URL'] = 'sqlite://'

import unittest
from app import app, db
from app.models import User, Post
from datetime import datetime, timezone, timedelta

