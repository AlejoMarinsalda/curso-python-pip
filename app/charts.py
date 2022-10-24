import matplotlib.pyplot as plt #Biblioteca para crear graficos


def generate_bar_chart(labels,values):
    fig,ax=plt.subplots()
    ax.bar(labels,values)
    plt.show()

def generate_pie_chart(labels,values):
    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis("equal")
    plt.show()

if __name__ =="__main__":
    labels= input("etiqueta: "),input("etiqueta: "),input("etiqueta: ")
    values=input("valor: "),input("valor: "),input("valor: ")
    generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)