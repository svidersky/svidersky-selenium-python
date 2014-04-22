from model.film import Film
from model.user import User

def test_add_film(app):
    app.ensure_login_as(User.Admin())
    fake_film = Film.fake_film()
    app.add_film(fake_film)
    app.logout()