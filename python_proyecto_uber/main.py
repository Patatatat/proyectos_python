from uberVan import UberVan
from driver import Driver

if __name__ == "__main__":
    uberPro = UberVan(16, "ASD123", Driver(16, "Martin", "123123", "@gmail", "pass"), 6, "PerroVolador", "Perro")
    print(uberPro.getId())
    print(uberPro.getDriver().getName())
    print(uberPro.getPassengers())