import logging

import validators


class Cli:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def get_url(self):
        print("Bienvenid@ al lector de noticias!")
        print("Por favor, escribe la URL a consultar y pulsa la tecla enter.")
        url = self._user_input()
        while not self._is_valid_url(url):
            print(
                "La URL no es válida"
                ". Por favor, escríbela de nuevo y pulsa la tecla enter."
            )
            url = self._user_input()
        return url

    def _user_input(self):
        return input("URL: ")

    def _is_valid_url(self, url: str) -> bool:
        if isinstance(validators.url(url), validators.ValidationFailure):
            self._logger.error(f"Invalid URL: {url}")
            return False
        return True


if __name__ == "__main__":
    Cli().get_url()
