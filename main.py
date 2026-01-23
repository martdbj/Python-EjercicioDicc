import csv

with (
    open("files/ej30notasdaw.csv", "r", encoding="utf-8") as n,
    open("files/ej30becas.txt", "r", encoding="utf-8") as b
):
    notas = csv.reader(n)
    