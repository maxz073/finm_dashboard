import pandas as pd

df = pd.read_parquet("ftsfr_commodities_returns.parquet")

df = df.pivot(index='ds', columns='unique_id', values='y')

gsci_indices_tickers = {
    "SPGCBRP": "Brent Crude Oil",
    "SPGCGOP": "Gasoil",
    "SPGCCLP": "WTI Crude",
    "SPGCHUP": "Unleaded Gasoline",
    "SPGCHOP": "Heating Oil",
    "SPGCNGP": "Natural Gas",
    "SPGCCTP": "Cotton",
    "SPGCKCP": "Coffee",
    "SPGCCCP": "Cocoa",
    "SPGCSBP": "Sugar",
    "SPGCSOP": "Soybeans",
    "SPGCKWP": "Kansas Wheat",
    "SPGCCNP": "Corn",
    "SPGCWHP": "Wheat",
    "SPGCLHP": "Lean Hogs",
    "SPGCFCP": "Feeder Cattle",
    "SPGCLCP": "Live Cattle",
    "SPGCGCP": "Gold",
    "SPGCSIP": "Silver",
    "SPGCIAP": "Aluminum",
    "SPGCIKP": "Nickel",
    "SPGCILP": "Lead",
    "SPGCIZP": "Zinc",
    "SPGCICP": "Copper",
}

df = df.rename(columns=lambda x: gsci_indices_tickers.get(x[:7], x))

print(df.head())