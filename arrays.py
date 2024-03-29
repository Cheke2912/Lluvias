class Array:
    def __init__(self,n):
        self.__n = n
        self.__arreglo = []
        for i in range(0,n,1):
            self.__arreglo.append(0)

    def length(self):
        return self.__n

    def get_item(self,index):
        return self.__arreglo[index]

    def set_item(self,index,value):
        self.__arreglo[index] = value

    def clearing(self,value):
        for i in range(0,self.__n,1):
            self.__arreglo[i] = value

    def to_string(self):
        print(f"El Tamaño del Arreglo es: {self.__n}")
        print(self.__arreglo)

#Arreglo 2D

class Array2D:
    def __init__(self,rows,cols):
        self.__rows = rows
        self.__cols = cols
        self.__arreglo = []
        for r in range(self.__rows):
            tmp = []
            for c in range(self.__cols):
                tmp.append(0)
            self.__arreglo.append(tmp)            

    def to_string(self):
        for ren in self.__arreglo:
            print(ren)

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def set_item(self,rows,cols,value):
        self.__arreglo[rows][cols] = value
        
    def get_item(self,rows,cols):
        return self.__arreglo[rows][cols]

    def clearing(self,value):
        for i in range(self.__rows):
            for j in range(self.__cols):
                self.__arreglo[i][j] = value


#Arreglo 3D
class Array3D:
    def __init__(self,depth,rows,cols):
        
        self.__rows = rows
        self.__cols = cols
        self.__depth = depth
        self.__arreglo = [[[0 for j in range(cols)]for k in range(rows)]for l in range(depth)]
       
    def get_num_depth(self):
        return self.__depth

    def get_num_rows(self):
        return self.__rows
    
    def get_num_cols(self):
        return self.__cols
    
    def set_item(self,depth,rows,cols,value):
        self.__arreglo[depth][rows][cols] = value
        
    def get_item(self,depth,rows,cols):
        return self.__arreglo[depth][rows][cols]

    def clearing(self,value):
        for i in range(self.__depth):
            for j in range(self.__rows):
                for k in range(slef.__cols):
                    self.__arreglo[i][j][k] = value
    
    def to_string(self):
        #print(f"el tamaño del arreglo es de {self.__arreglo}")
        capa=0
        for layer in self.__arreglo:
            print(f"-------capa{capa+1}-----")
            for ren in layer:
                print(ren)
            capa +=1





    
