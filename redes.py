from enlace import enlace

class redes(enlace):
  def __init__(self):
    super().__init__()
    # super().__init__(link)
    self.__neighbors = []
    self.routeTable = []
    self.__topologia = []

  def RouteRequest(self,topologia):
    #Todo DSR or AODV
    pass

  def RouteResponse(self):
    #Todo DSR or AODV
    pass

  def PrintNeighbors(self):
    print("{", end="")
    for i in self.__neighbors:
      print(i.ID+":", end="")
    print("}")

  def __Hellou(self,myposition,topologia):
    self.__topologia = topologia #guarda a topologia da rede para não precisar reenviar
    self.__neighbors = []
    for i in topologia: #i é um host
      if(i.CheckEnergy()):
        if(myposition == i):
          self.__neighbors.append(i)

  def __send(self,dado):
    for i in self.__neighbors: #verifica se é vizinho
      if(i.ID == dado.destination):#verifica cada vizinho
        if(self._enlace__GetBusy()):#se o enlace estiver ocupado, 
          print("[Redes] Canal ocupado, esperando liberação")
          while(not self._enlace__GetBusy):#espera desocupar
            pass
        if(not self._enlace__GetBusy()):#se o enlace não estiver ocupado
          self._enlace__SendDado(i,dado) #envia referencia do host e o dado
          break






