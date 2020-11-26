from src.model.user import User


def populate_db(make_record):
    make_record(User, username='admin', password='password', ip_address='127.0.0.1')
    make_record(User, username='admin2', password='password2', ip_address='127.0.0.2')
