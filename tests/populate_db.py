from werkzeug.security import generate_password_hash

from src.model.user import User
from src.model.stat import Stat


def populate_db(make_record):
    user = make_record(User, username='admin',
                password=generate_password_hash('password1'),
                ip_address='127.0.0.1')
    stat = make_record(Stat, user_id=user.id)

    user = make_record(User, username='admin2',
                password=generate_password_hash('password2'),
                ip_address='127.0.0.2')
    stat = make_record(Stat, user_id=user.id)

    user = make_record(User, username='test',
                password=generate_password_hash('password_test'),
                ip_address='127.0.0.3')
    stat = make_record(Stat, user_id=user.id)
