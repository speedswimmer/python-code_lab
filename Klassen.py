class Fahrrad:
    """
    Erstellt das Objekt Fahrrad für einen Fahrradhändler.
    """
    def __init__(self, artnr, preis, farbe, fahrradtyp, laufradgroesse):
        """
        Initialissiert ein neues Objekt Fahrrad
        Argumente:

        *Artikelnummer (int): artnr
        *param preis:
        *param farbe:
        *param fahrradtyp:
        *param laufradgroesse:
        """
        self.Artikelnummer = artnr
        self.Preis = preis
        self.Farbe = farbe
        self.Fahrradtyp = fahrradtyp
        self.Laufradgroesse = laufradgroesse

