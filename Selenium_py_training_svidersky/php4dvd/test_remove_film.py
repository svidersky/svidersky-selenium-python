from model.film import Film
from model.user import User


def test_add_film(app):
    app.ensure_login_as(User.Admin())
    new_film = Film.random()
    app.add_film(new_film)
    app.remove_film(new_film)
    app.logout()