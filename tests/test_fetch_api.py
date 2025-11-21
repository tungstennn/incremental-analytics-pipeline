import json
from unittest.mock import patch, MagicMock
from src.api.fetch_api import fetch_pokemon_data


@patch("requests.get")
def test_fetch_pokemon_data_success(mock_get, tmp_path):
    # Mock API response
    fake_api_response = {"name": "pikachu", "id": 25}

    mock_response = MagicMock()
    mock_response.json.return_value = fake_api_response
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    output_file = tmp_path / "api_response.json"

    data = fetch_pokemon_data(str(output_file))

    assert data["name"] == "pikachu"

    # Verify file was written
    with open(output_file) as f:
        saved_data = json.load(f)
    assert saved_data["name"] == "pikachu"
