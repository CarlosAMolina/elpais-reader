# EL PAIS reader

## Introduction

Project to read elpais.com articles blocked by loging.

More information at: <https://carlosamolina.github.io/blog/2021-05-15-leer-periodicos-online-sin-iniciar-sesion.html>.

## Development

### Test

1. Download the project.
2. Activate a virtualenv and install the requirements.
3. Run tox.

### PyInstaller

```bash
# Linux.
pyinstaller program.py --add-data elpais_reader/:elpais_reader
cd dist/program
./program
```

Resource: <https://realpython.com/pyinstaller-python/>.
