def write_outputs(players, rounds, steals, gifts, values):

    with open("data/steals.txt", "w") as f:
        f.write(f"WHITE-ELEPHANT SIMULATOR\n")
        f.write(f"Avg. Number of Steals per Player\n")
        f.write(f"Generated for {players} Players over {rounds} iterations\n")
        f.write("-" * 30)
        f.write("\n\n")
        for i in steals:
            f.write(str(i) + "\n")

    with open("data/gifts.txt", "w") as f:
        f.write(f"WHITE-ELEPHANT SIMULATOR\n")
        f.write(f"Which Player gets the best gift?\n")
        f.write(f"Generated for {players} Players over {rounds} iterations\n")
        f.write("-" * 30)
        f.write("\n\n")
        for i in gifts:
            f.write(str(i) + "\n")

    with open("data/values.txt", "w") as f:
        f.write(f"WHITE-ELEPHANT SIMULATOR\n")
        f.write(f"Do better-quality gifts get stolen more?\n")
        f.write(f"Generated for {players} Players over {rounds} iterations\n")
        f.write("-" * 30)
        f.write("\n\n")
        for i in values:
            f.write(str(i[0]) + " " + str(i[1]) + "\n")
