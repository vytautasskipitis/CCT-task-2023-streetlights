
# paskaiciuoja kiek sviesos gauname is kaimyniniu zibintu
def illumination_intensity(distance):
    return 3 ** (-(distance / 100) ** 2)

# sudaro lista su galutiniais zibintu sviesos stiprumais
def zibintu_listas(road_length: int, not_working_street_lights: list[int]) -> int:
    sarasas_kurie_dega = []

    # pridedu 1 zibinta kelio pradzioje ,o "i" reiksme nurodo zibinto indeksa
    for i in range(road_length // 20 + 1):

        # jei zibintas dega tai sarase zymimas kaip 1, jei nedega 0
        if i not in not_working_street_lights:
            sarasas_kurie_dega.append(1)
        else:
            sarasas_kurie_dega.append(0)
    # print(sarasas_kurie_dega)

    zibintu_sviesumo_listas = []
    galutine_zibinto_sviesa = 0

    # pereina per kiekviena zibinta sarase
    for i in range(len(sarasas_kurie_dega)):

        # pereina per kiekviena zibinta sarase
        for number in range(len(sarasas_kurie_dega)):

            # paraso atstumus iki kaimyniniu zibintu tik dar ne metrais
            atstumas = number - i
            # (>0.01 sviesumo zibintai yra ignoruojami)
            if abs(atstumas) < 11:

                # pasiverciam atstuma i metrus
                atstumas = abs(atstumas * 20)
                # print(atstumas)

                # jeigu kaimyninis zibintas dega tada jo sviesa sumuojam jei nedega - ignoruojam
                if sarasas_kurie_dega[number] == 1:
                    galutine_zibinto_sviesa += illumination_intensity(atstumas)
                # print(galutine_zibinto_sviesa)

        # sudaro lista kuriame surasyti galutiniai zibintu sviesumai
        zibintu_sviesumo_listas.append(galutine_zibinto_sviesa)
        galutine_zibinto_sviesa = 0
    print(zibintu_sviesumo_listas)

    # grazina indeksa tamsiausio zibinto
    return zibintu_sviesumo_listas.index(min(zibintu_sviesumo_listas))


if __name__ == "__main__":
    # Example test for finding the darkest street light
    print(zibintu_listas(road_length=100, not_working_street_lights=[3, 4, 5]))
    print(zibintu_listas(road_length=200, not_working_street_lights=[4, 5, 6]))
    print(zibintu_listas(road_length=1000, not_working_street_lights=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]))

###############################################################################################################
# optimalus zibintu kiekis
###############################################################################################################





















