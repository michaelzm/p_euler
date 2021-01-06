class DijkstraNode:
  def __init__(self):
    #node connections
    self.prev_node = None
    self.next_node = []
   
    #sum til this node
    self.sumWeight = 100000000
    
    #graph information
    self.connectionWeight = 0 

  #sum til this node
  def getSum(self):
    return self.sumWeight

  def setSum(self, weightTilNode):
    self.sumWeight = weightTilNode

  #follower related stuff
  def getPrev(self):
    return self.prev_node
  
  def setPrev(self, prev):
    self.prev_node = prev

  def setNextNode(self,followerNode):
    self.next_node.append(followerNode)
    #print(self.next_node)
  
  def getNextNode(self):
    return self.next_node

  #connection weight
  def setConWeight(self,weight):
    self.connectionWeight = weight

  def getConWeight(self):
    return self.connectionWeight

