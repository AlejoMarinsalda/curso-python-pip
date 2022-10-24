import csv
from email import header
from hashlib import new

def read_csv(path):#creamos la funcion con el parametro "path=el cual sera la ruta de nuestro data.csv"
    with open(path,"r") as csvfile:# usamos un with para que el archivo se cierre de forma automatica una vez finalizada la lectura//pasamos el parametro ruta y la "r" para lectura//le agregamos el nombre "csvfile" al csv que leyamos
        reader = csv.reader(csvfile,delimiter=",")# usamos la funcion "reader" de la libreria "csv" para leer el csv(pasamos por parametro el nombre del archivo "csvfile" y como estan separados los datos de ese archivo ",")
        header = next(reader)#se paramos las primeras columnas en una variable llamada "header" para posteriormente crear un diccionario
        data=[]#creamos una lista vacia
        for row in reader:
            iterable= zip(header,row)#unimos las primeras columnas con los datos correspondientes a cada pais en este, caso en forma de tuplas// ejemplo =("population","3 millones" "capital","buenos aires") 
            country_dict = {key:value for key,value in iterable}#creamos un diccionario en el que separamos la clave y el valor por ":" y para esto utilizamos la union del header y cada linea que es = "itereable"
            data.append(country_dict)#utilizamos (dictionary comprehension ) para agregar el diccionario a la lista data y asi formar una lista de diccionario
        return data 
            


if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    print(data[0])