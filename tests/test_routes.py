from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/2")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 2,
        "name": "Mars",
        "description": "Planet Mars"
    }

def test_get_one_planet_no_record(client):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == None

def test_get_all_planets_with_records(client, two_saved_planets):
    # Act
    response = client.get("/planets",two_saved_planets)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [{'description': 'Planet Mercury', 'id': 1, 'name': 'Mercury'},
                    {'description': 'Planet Mars', 'id': 2, 'name': 'Mars'}]



def test_post_planets(client, planet_data):
    # Act
    response = client.post("/planets", json=planet_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == f'planet {new_planet.name} has been created', 201