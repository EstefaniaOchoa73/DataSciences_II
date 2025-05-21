def infoDataFrame (df):
    print("-- INFO --")
    print(df.info())
    print("\n-- HEAD --")
    print(df.head())
    print("\n-- DESCRIBRE --")
    print(df.describe())
    print("\nCantidad de Filas: ",len(df))   