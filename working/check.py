import pandas as pd

df = pd.read_parquet("ftsfr_commodities_returns.parquet")

df.to_excel("commodities_returns.xlsx", index=False)

gsci_indices_tickers = {
    "SPGCBRP Index": "Brent Crude Oil",
    "SPGCGOP Index": "Gasoil",
    "SPGCCLP Index": "WTI Crude",
    "SPGCHUP Index": "Unleaded Gasoline",
    "SPGCHOP Index": "Heating Oil",
    "SPGCNGP Index": "Natural Gas",
    "SPGCCTP Index": "Cotton",
    "SPGCKCP Index": "Coffee",
    "SPGCCCP Index": "Cocoa",
    "SPGCSBP Index": "Sugar",
    "SPGCSOP Index": "Soybeans",
    "SPGCKWP Index": "Kansas Wheat",
    "SPGCCNP Index": "Corn",
    "SPGCWHP Index": "Wheat",
    "SPGCLHP Index": "Lean Hogs",
    "SPGCFCP Index": "Feeder Cattle",
    "SPGCLCP Index": "Live Cattle",
    "SPGCGCP Index": "Gold",
    "SPGCSIP Index": "Silver",
    "SPGCIAP Index": "Aluminum",
    "SPGCIKP Index": "Nickel",
    "SPGCILP Index": "Lead",
    "SPGCIZP Index": "Zinc",
    "SPGCICP Index": "Copper",
}