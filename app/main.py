import utils
import read_csv
import charts

def run():

    data = read_csv.read_csv("./app/data.csv")
    MUNDO="MUNDO"
    
    populatio_global=[]
    for country in data:
        populatio_global.append (int(country['2022 Population']))
    def suma():
        for population in populatio_global:
            suma_population =+ populatio_global
        return suma_population
    
    charts.generate_pie_chart(MUNDO,populatio_global)
    
    result = utils.population_by_country(data,country)
    if len(result) > 0:
        country = result[0]
        keys,values = utils.get_population(country)
        #charts.generate_pie_chart(keys,values)
    print(result)


if __name__ == "__main__": #hace que podamos ejecutar este modulo directamente desde la terminal como un script
    run()