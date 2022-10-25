from numpy import char
import utils
import read_csv
import charts
import pandas as pd

def run():

    df = pd.read_csv("data.csv") #leemos el CSV con pandas 
    df = df[df["Continent"]=="Africa"] #elegimos en que columnas se enfoque
    countries = df["Country/Territory"].values #elgimos uqe separe la columna de paises
    percentages=df["World Population Percentage"].values
    charts.generate_pie_chart(countries,percentages)
    
    data = read_csv.read_csv("data.csv")
    
    country = input("Type Country => ").capitalize()
  
    
    print(country)
    
    result = utils.population_by_country(data,country)
    if len(result) > 0:
        country = result[0]
        keys,values = utils.get_population(country)
        #charts.generate_pie_chart(keys,values)
    print(result)


if __name__ == "__main__": #hace que podamos ejecutar este modulo directamente desde la terminal como un script
    run()