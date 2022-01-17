ORIGINAL_CREATOR_FOUNDER = "yasserprogamer"

DEVELOPERS = [
    "yasserprogamer",
    "alex"
]

TRANSLATORS = []


def credit():
    print("")
    print("".center(106, "—"))
    print("|"+"Software credit".center(104, " ")+"|")
    print("|"+"".center(104," ")+"|")
    print("|"+f"Original Creator and Founder: {ORIGINAL_CREATOR_FOUNDER}.".center(104," ")+"|")
    print("|"+"".center(104," ")+"|")
    print("|"+"+====== Developers ======+".center(104," ")+"|")
    print("|"+"".center(104," ")+"|")
    for developer in DEVELOPERS:
        print("|"+f"• {developer} •".center(104," ")+"|")
    print("|"+"".center(104," ")+"|")
    print("|"+"+========================+".center(104," ")+"|")
    print("|"+"".center(104," ")+"|")
    print("|"+"P.O.S.I-SW © 2022".center(104," ")+"|")
    print("".center(106, "—"))
    print("")
    PressToContinue = input("Press ENTER to continue . . . ")