from pathlib import Path

import pandas as pd


# Arquivo possui registros de 245 bytes.
# As posições abaixo vêm diretamente do layout COTAHIST da B3.
COLUNAS = [
    "TIPREG",
    "DATA_PREGÃO",
    "CODBDI",
    "CODNEG",
    "TPMERC",
    "NOMRES",
    "ESPECI",
    "PRAZOT",
    "MODREF",
    "PREABE",
    "PREMAX",
    "PREMIN",
    "PREMED",
    "PREULT",
    "PREOFC",
    "PREOFV",
    "TOTNEG",
    "QUATOT",
    "VOLTOT",
    "PREEXE",
    "INDOPC",
    "DATVEN",
    "FATCOT",
    "PTOEXE",
    "CODISI",
    "DISMES",
]

# Largura de cada campo no registro de 245 bytes.
LARGURAS = [
    2,    # TIPREG       01-02
    8,    # DATA_PREGÃO  03-10
    2,    # CODBDI       11-12
    12,   # CODNEG       13-24
    3,    # TPMERC       25-27
    12,   # NOMRES       28-39
    10,   # ESPECI       40-49
    3,    # PRAZOT       50-52
    4,    # MODREF       53-56
    13,   # PREABE       57-69
    13,   # PREMAX       70-82
    13,   # PREMIN       83-95
    13,   # PREMED       96-108
    13,   # PREULT       109-121
    13,   # PREOFC       122-134
    13,   # PREOFV       135-147
    5,    # TOTNEG       148-152
    18,   # QUATOT       153-170
    18,   # VOLTOT       171-188
    13,   # PREEXE       189-201
    1,    # INDOPC       202
    8,    # DATVEN       203-210
    7,    # FATCOT       211-217
    13,   # PTOEXE       218-230
    12,   # CODISI       231-242
    3,    # DISMES       243-245
]


def carregar_cotacoes(caminho: str | Path) -> pd.DataFrame:
    """
    Carrega o arquivo histórico COTAHIST da B3.

    Parâmetros
    ----------
    caminho:
        Caminho para o arquivo COTAHIST_AAAA.txt.

    Retorno
    -------
    pd.DataFrame
        DataFrame contendo os registros do arquivo.
    """

    caminho = Path(caminho)

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}"
        )

    df = pd.read_fwf(
        caminho,
        widths=LARGURAS,
        names=COLUNAS,
        header=None,
        dtype=str,
    )

    # Remove espaços existentes nos campos de texto.
    for coluna in df.columns:
        df[coluna] = df[coluna].str.strip()

    return df