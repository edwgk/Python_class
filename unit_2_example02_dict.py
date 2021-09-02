def generarreortesnotas(boletascalificaciones):
    sumatoria=0
    sumatoria=sumatoria+boletascalificaciones["nota1"]
    sumatoria=sumatoria+boletascalificaciones["nota2"]
    sumatoria=sumatoria+boletascalificaciones["nota3"]
    sumatoria+=boletascalificaciones["nota4"]
    prom=sumatoria/4
    reportenotas={
        "estudiante":boletascalificaciones["estudiante"],
        "promedio":prom


    }
    return reportenotas

def reportarpromedio (repnotas):
    return "el estudiante "+ repnotas ["estudiante"] + " tuvo un promedio de " + str(repnotas["promedio"])

calificaciones={
    "estudiante":"jose david",
    "nota1":3.0,
    "nota2":2.1,
    "nota3":5.0,
    "nota4":4.7
}
reportegenerado=generarreortesnotas(calificaciones)
reportepromedio=reportarpromedio(reportegenerado)
print(reportepromedio)