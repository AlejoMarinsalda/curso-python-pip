import utils
import read_csv
import charts

def prueba():
     data = read_csv.read_csv("./app/data.csv")
     result = utils.population_by_country(data)






if __name__ == "__main__":
    prueba()