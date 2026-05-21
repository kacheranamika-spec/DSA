# Graph

class Graph:

    def __init__(self):
        self.node = []
        self.graph = []
        self.nodeCount = 0



    def addNode(self, v):
        if v in self.node:
            print("Node already exists")

        else:
            self.node.append(v)
            self.nodeCount += 1

            for row in self.graph:
                row.append(0)

            new_row = [0] * self.nodeCount
            self.graph.append(new_row)

            print(v, "is added")



    def addEdge_Undirected_Unweighted(self, v1, v2):

        if v1 not in self.node or v2 not in self.node:
            print(v1, "and", v2, "not present")

        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)

            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1

            print(v1, "and", v2, "are connected")



    def addEdge_Undirected_Weighted(self, v1, v2, w):

        if v1 not in self.node or v2 not in self.node:
            print(v1, "and", v2, "not present")

        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)

            self.graph[index1][index2] = w
            self.graph[index2][index1] = w

            print(v1, "and", v2, "are connected with weight", w)



    def addEdge_Directed_Weighted(self, v1, v2, w):

        if v1 not in self.node or v2 not in self.node:
            print(v1, "and", v2, "not present")

        else:
            index1 = self.node.index(v1)
            index2 = self.node.index(v2)

            self.graph[index1][index2] = w

            print(v1, "->", v2, "with weight", w)

    def printGraph(self):
      print(*self.node)
      for i in range (len(self.node)):
        for j in range(len(self.node)):
          print(self.graph[i][j], end = " ")
        print()



    def deleteGraph(self, v):
      if v not in self.node:
        print(v, "not present")

      else:
        index = self.node.index(v)
        self.node.pop(index)
        self.graph.pop(index) 

        for x in self.graph:
          x.pop(index)

        # self.nodeCount -=1

        print(v, "is deleted")



if __name__ == '__main__':

    gra = Graph()

    while True:

        print("\n1. Insert")
        print("2. addEdge_Undirected_Unweighted")
        print("3. addEdge_Undirected_Weighted")
        print("4. addEdge_Directed_Weighted")
        print("5. printGraph")
        print("6. deleteGraph")
        print("7. Exit")

        n = int(input("Enter your choice = "))

        if n == 1:

            v = input("Enter vertices = ")
            gra.addNode(v)

        elif n == 2:

            v1 = input("Enter vertex 1 = ")
            v2 = input("Enter vertex 2 = ")

            gra.addEdge_Undirected_Unweighted(v1, v2)

        elif n == 3:

            v1 = input("Enter vertex 1 = ")
            v2 = input("Enter vertex 2 = ")

            w = int(input("Enter weight = "))

            gra.addEdge_Undirected_Weighted(v1, v2, w)

        elif n == 4:

            v1 = input("Enter vertex 1 = ")
            v2 = input("Enter vertex 2 = ")

            w = int(input("Enter weight = "))

            gra.addEdge_Directed_Weighted(v1, v2, w)

        elif n == 5:

            gra.printGraph()

        elif n == 6:
            v = input("Enter vertex = ")
            gra.deleteGraph(v)

        else:
            break