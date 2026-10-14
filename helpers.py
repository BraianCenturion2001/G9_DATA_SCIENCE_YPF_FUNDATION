import pandas as pd

def formato_moneda(val):
    if pd.isna(val):
        return ""
    return f"${val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")