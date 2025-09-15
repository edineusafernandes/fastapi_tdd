from pathlib import Path

ROOT_PATH = Path('__flie__').parent

try:
    with open(ROOT_PATH / "ooracao_obaluae.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo. {exc}")