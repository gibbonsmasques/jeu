from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.rational_field import RationalField
QQ = RationalField()
R = PolynomialRing(QQ, "T")
T = R.gen()
Q = T**4 + 5*T**3 - 2*T**2 - 3*T - 1
dico = dict()
dico["plume"] = (0, -1)
dico["tiroir"] = (1, 0)
dico["boum"] = (2, 41)
dico["attendre"] = (3, 188)
dico["balon"] = (4, 531)
dico["jardin"] = (5, 1184)
dico["tendre"] = (6, 2285)
dico["garage"] = (7, 3996)

def indice(psw):
    try:
        t = R.lagrange_polynomial([dico[w] for w in psw])
    except KeyError:
        return "Mauvais mot de passe"

    if t == Q:
        return "Bravo, voici le prochain indice : ..."
    else:
        return "Il manque encore des mots de passe pour que je vous donne l'indice."
