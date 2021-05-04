import pytest
from app import create_app
from app import db
from app.models.planet import Planet



@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury_planet = Planet(name="Mercury",
                    description="Planet Mercury")
    mars_planet = Planet(name="Mars",
                        description="Planet Mars")

    db.session.add_all([mercury_planet, mars_planet])
    db.session.commit()

@pytest.fixture
def planet_data(app):
    return {
"name": "Uranus",
"description": "Planet Uranus"
}

