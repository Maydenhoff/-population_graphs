import csv
import matplotlib.pyplot as plt

def read_csv(path):
    with open(path, "r") as cvsfile:
        reader = csv.reader(cvsfile, delimiter=",")
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict ={key: value for key, value in iterable}
            data.append(country_dict)
        return data


def look_for_country(data, country):
  labels = []
  values = []
  labels_graf = []
  for i in data:
    if i["Country/Territory"] == country:
      for k in i:
        if "Population" in k and len(k) == 15:
          labels.insert(0,k)
          arr= k.split()
          print("k", arr)
          labels_graf.insert(0,arr[0])
          # years.append(arr[0])
      for v in labels:
        values.append(i[v])
      break
  if len(labels) == 0:
    print("No se encontraron resultados")  
    return   
    
  fig, ax=plt.subplots()
  ax.bar(labels_graf, values)
  plt.savefig("pie.png")
  plt.close()

if __name__ == "__main__":
    pais=input("ingrese un pais: ")
    data = read_csv("data.csv")
    # print(data)
    look_for_country(data,pais)
    
