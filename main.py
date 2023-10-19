from shapes.circle import Circle
from shapes.rectangle import Rectangle


def run_demo_lab() -> None:
    """Run demo from labb"""
    cirkel1 = Circle(x=0, y=0, radius=1)  # enhetscirkel
    cirkel2 = Circle(x=1, y=1, radius=1)
    rektangel = Rectangle(x=0, y=0, side1=1, side2=1)

    print(f"{cirkel1 == cirkel2 = }")  # True
    print(f"{cirkel2 == rektangel = }")  # False
    print(f"{cirkel1.is_inside(0.5, 0.5) = }")  # True
    cirkel1.translate(5, 5)
    print(f"{cirkel1.is_inside(0.5, 0.5) = }")  # False

    try:
        cirkel1.translate("TRE", 5)  # ge ValueError med lämplig kommentar
    except TypeError:
        print("Måste ha int eller float som datatyp till 'translate'.")

    print(
        "(För mer omfattande info om hur klasserna är menade att användas, se enhetstesterna)"
    )


if __name__ == "__main__":
    run_demo_lab()
