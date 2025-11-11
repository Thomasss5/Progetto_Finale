import sys
import os

# Aggiunge la cartella principale al path, per evitare errori di import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src_exercises.esempio import saluta, somma, media


def test_saluta():
    assert saluta("Mario") == "Ciao, Mario! Benvenuto!"
    assert saluta("Lucia") == "Ciao, Lucia! Benvenuto!"
    assert isinstance(saluta("Paolo"), str)  # Deve restituire una stringa


def test_somma():
    assert somma(2, 3) == 5
    assert somma(-1, 1) == 0
    assert somma(0, 0) == 0
    assert somma(1.5, 2.5) == 4.0  # Test con float


def test_media():
    assert media([10, 20, 30]) == 20
    assert media([5]) == 5
    assert media([]) == 0  # Lista vuota → 0
    assert media([1, 2, 3, 4]) == 2.5
