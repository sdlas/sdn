from mininet.topo import Topo

class Router_Topo(Topo):
	def __init__(self):
		# Initialize topology
		Topo.__init__(self)
		self.k=4
		self.Hostlist = []
		self.Elist = []
		self.Alist = []
		self.Clist = []
			# Add hosts and switches
		for i in range(0,self.k*4):
			self.Hostlist.append(self.addHost(str('h'+str(i+1))))
			for i in range(0,self.k*2):
				self.Elist.append(self.addSwitch(str('E'+str(i+1))))
				self.Alist.append(self.addSwitch(str('A'+str(i+1))))
			for i in range(0,self.k):
				self.Clist.append(self.addSwitch(str('C'+str(i+1))))
			
		# Links Between Host and E
		for i in range(0,self.k*4):
			self.addLink(self.Hostlist[i],self.Elist[int(i/2)])
		# Links Between E and A
		for i in range(0,self.k*2):
			self.addLink(self.Elist[i],self.Alist[int(i/2)*2])
			self.addLink(self.Elist[i],self.Alist[int(i/2)*2+1])
		# Links Between A and C
		for i in range(0,self.k):
			self.addLink(self.Alist[i*2],self.Clist[0])
			self.addLink(self.Alist[i*2],self.Clist[1])
			self.addLink(self.Alist[i*2+1],self.Clist[2])
			self.addLink(self.Alist[i*2+1],self.Clist[3])

topos = {
        'router': (lambda: Router_Topo())
}
