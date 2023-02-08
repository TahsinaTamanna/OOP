import InsectClass as ic


def main():
    insect1 = ic.Insect()
    insect1.len_flight()
    print("Miles for insect 1: ", insect1.get_flight())

    insect2 = ic.Insect()
    insect2.len_flight()
    print("Miles for insect 2: ", insect2.get_flight())


# Call the main function.

main()
