def cToFConverter():
    while True:
        cTemp = input("Please enter C degree: ")
        if cTemp:
            cTemp = float(cTemp)
            fTemp = round(cTemp * 9 / 5 + 32, 1)
            print(f"{cTemp}C is converted to {fTemp}F")
            break
        else:
            print("cTemp input is empty")
def main():
    cToFConverter()

if __name__ == "__main__":
    main()