import pandas as pd

df = pd.DataFrame([
    {"nazwa":"RURA EN10357 29x1,5 304L", "nr_faktury":"4887/BE/06/2025", "cena_netto":20.50},
    {"nazwa":"RURA EN10357 29x1,5 304L", "nr_faktury":"5555/BE/07/2025", "cena_netto":25.50},
])
pivot = df.pivot_table(index="nazwa", columns="nr_faktury", values="cena_netto", aggfunc="mean")
st = "4887/BE/06/2025"; nw = "5555/BE/07/2025"
pivot["delta_%"] = (pivot[nw] - pivot[st]) / pivot[st]
pivot.to_excel("output/porownanie_cen.xlsx")
print("Zapisano: output/porownanie_cen.xlsx")
