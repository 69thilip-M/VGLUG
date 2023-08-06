def itachi(ability,clan,**kwargs):
    #print(f"ABILITY : {ability}")
    #print(f"CLAN : {clan}")

    print("ABILITY"+ability)
    for key,value in kwargs.items():
        print(f"{key.capitalize()}:{value}")

itachi("SHERINGAN","UCHIHA",power="AMETERASU",location="KONAHA")
