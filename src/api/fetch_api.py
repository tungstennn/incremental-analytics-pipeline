import os
import json
import time
import requests


POKEMON_API = "https://pokeapi.co/api/v2/pokemon/pikachu"


def fetch_pokemon_data(output_path: str, retries: int = 3, delay: float = 1.0) -> dict:
    """
    Fetches Pikachu data from the Pokémon API and saves it as JSON.
    Includes retries + basic validation.
    """

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(POKEMON_API, timeout=5)
            response.raise_for_status()
            data = response.json()

            # Basic validation
            if "name" not in data:
                raise ValueError("API returned unexpected structure")

            # Ensure folder exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            with open(output_path, "w") as f:
                json.dump(data, f, indent=4)

            return data

        except Exception as e:
            print(f"Attempt {attempt} failed with error: {e}")
            if attempt == retries:
                raise
            time.sleep(delay)  # retry delay


if __name__ == "__main__":
    fetch_pokemon_data("data/raw/api_response.json")
