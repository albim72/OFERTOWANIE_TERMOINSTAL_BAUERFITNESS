if __name__ == "__main__":
    # przykład
    D = 29.0      # mm
    Tm = 80.0     # C
    To = 20.0     # C
    lamb = 0.035  # W/mK
    q = 15.0      # W/m
    print("Grubość izolacji [mm]:", round(grubosc_izolacji(D, Tm, To, lamb, q), 1))