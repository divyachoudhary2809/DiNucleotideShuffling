import random
 
def for_mon(s):
    A = s.count('A')
    G = s.count('G')
    T = s.count('T')
    C = s.count('C')
    N = s.count('N')
    return [A,G,T,C,N]

def for_check(s):
    countA=0
    countG=0
    countT=0
    countC=0
    for i in range (0, len(s)-1):
        if (s[i] == s[i+1]) and (s[i]== 'A'):
            countA+=1
        if (s[i] == s[i+1]) and (s[i]== 'G'):
            countG+=1    
        if (s[i] == s[i+1]) and (s[i]== 'T'):
            countT+=1    
        if (s[i] == s[i+1]) and (s[i]== 'C'):
            countC+=1
    AG2 = s.count('AG')
    AT2 = s.count('AT')
    AC2 = s.count('AC')
    CA2 = s.count('CA')
    CG2 = s.count('CG')
    CT2 = s.count('CT')
    TA2 = s.count('TA')
    TG2 = s.count('TG')
    TC2 = s.count('TC')
    GA2 = s.count('CA')
    GT2 = s.count('GT')
    GC2 = s.count('GC')
    
    AA2=countA
    GG2=countG
    TT2=countT
    CC2=countC
    
    return [AG2,AA2,AT2,AC2,CA2,CG2,CT2,CC2,TA2,TG2,TT2,TC2,GA2,GG2,GT2,GC2]


 
 
def counting(seq):
 
  Allbase = {}  
  seq= seq.upper()
  Allbase['A'] = []
  Allbase['C'] = [] 
  Allbase['G'] = [] 
  Allbase['T'] = []
  Allbase['N'] = []
  baseList   = ["A","C","G","T","N"]
  nCnt    = {}  
  nCnt['A'] = seq.count('A')
  nCnt['G'] = seq.count('G')
  nCnt['T'] = seq.count('T')
  nCnt['C'] = seq.count('C')
  nCnt['N'] = seq.count('N')
  dnCnt  = {}

  
  for i in baseList:
    dnCnt[i]={}  
    for j in baseList:
          dnCnt[i][j]=0 
 
       

  for i in range(len(seq)-1):
    Allbase[seq[i]].append( seq[i+1])
    
    
  countA=0
  countG=0
  countT=0
  countC=0
  countN=0
  for i in range (0, len(seq)-1):
    if (seq[i] == seq[i+1]) and (seq[i]== 'A'):
        countA+=1
    if (seq[i] == seq[i+1]) and (seq[i]== 'G'):
        countG+=1    
    if (seq[i] == seq[i+1]) and (seq[i]== 'T'):
        countT+=1    
    if (seq[i] == seq[i+1]) and (seq[i]== 'C'):
        countC+=1
    if (seq[i] == seq[i+1]) and (seq[i]== 'N'):
        countN+=1
  AG2 = seq.count('AG')
  AT2 = seq.count('AT')
  AC2 = seq.count('AC')
  CA2 = seq.count('CA')
  CG2 = seq.count('CG')
  CT2 = seq.count('CT')
  TA2 = seq.count('TA')
  TG2 = seq.count('TG')
  TC2 = seq.count('TC')
  GA2 = seq.count('CA')
  GT2 = seq.count('GT')
  GC2 = seq.count('GC')
  AN = seq.count('AN')
  GN = seq.count('GN')
  TN = seq.count('TN')
  CN = seq.count('CN')
  NA = seq.count('NA')
  NG = seq.count('NG')
  NT = seq.count('NT')
  NC = seq.count('NC')
  NN = countN
  
  AA2=countA
  GG2=countG
  TT2=countT
  CC2=countC
  
    
  dnCnt['A']['A'] = AA2
  dnCnt['A']['G'] = AG2
  dnCnt['A']['T'] = AT2
  dnCnt['A']['C'] = AC2
  dnCnt['G']['A'] = GA2
  dnCnt['G']['G'] = GG2
  dnCnt['G']['T'] = GT2
  dnCnt['G']['C'] = GC2
  dnCnt['T']['A'] = TA2
  dnCnt['T']['G'] = TG2
  dnCnt['T']['T'] = TT2
  dnCnt['T']['C'] = TC2
  dnCnt['C']['A'] = CA2
  dnCnt['C']['G'] = CG2
  dnCnt['C']['T'] = CT2
  dnCnt['C']['C'] = CC2
  dnCnt['N']['A'] = NA
  dnCnt['N']['G'] = NG
  dnCnt['N']['T'] = NT
  dnCnt['N']['C'] = NC
  dnCnt['A']['N'] = AN
  dnCnt['G']['N'] = GN
  dnCnt['T']['N'] = TN
  dnCnt['C']['N'] = CN
  dnCnt['N']['N'] = NN
 

  return nCnt,dnCnt,Allbase
 
 
    



 
def chooseEdge(x,dinuclCnt):
  z = random.random()
  denom=dinuclCnt[x]['A']+dinuclCnt[x]['C']+dinuclCnt[x]['G']+dinuclCnt[x]['T']+dinuclCnt[x]['N']
  numerator = dinuclCnt[x]['A']
  if z < float(numerator)/float(denom):
    dinuclCnt[x]['A'] -= 1
    return 'A'
  numerator += dinuclCnt[x]['C']
  if z < float(numerator)/float(denom):
    dinuclCnt[x]['C'] -= 1
    return 'C'
  numerator += dinuclCnt[x]['G']
  if z < float(numerator)/float(denom):
    dinuclCnt[x]['G'] -= 1
    return 'G'
  numerator += dinuclCnt[x]['T']
  if z < float(numerator)/float(denom):
    dinuclCnt[x]['T'] -= 1
    return 'T'
  dinuclCnt[x]['N'] -= 1
  return 'N'

def connectedToLast(edgeList,nuclList,lastCh):
  D = {}
  for x in nuclList: 
      D[x]=0
      
  for edge in edgeList:
    if edge[1]==lastCh: 
        D[edge[0]]=1
        
        
  for i in range(3):
    for edge in edgeList:
       
      if D[edge[1]]==1: 
          D[edge[0]]=1
 
  for x in nuclList:
    if x!=lastCh and D[x]==0:
         
        return 0
 
  return 1



def eulerian(s):
  nuclCnt,dinuclCnt,List = counting(s)
  nuclList = []
  for x in ["A","C","G","T","N"]:
    if x in s: nuclList.append(x) 
  firstCh = s[0]  
  lastCh  = s[-1]
  edgeList = []
  for x in nuclList:
    if x!= lastCh: edgeList.append( [x,chooseEdge(x,dinuclCnt)] )
  ok = connectedToLast(edgeList,nuclList,lastCh)
  return ok,edgeList,nuclList,lastCh


def shuffleEdgeList(L):
  n = len(L); barrier = n
  for i in range(n-1):
    z = int(random.random() * barrier)
    tmp = L[z]
    L[z]= L[barrier-1]
    L[barrier-1] = tmp
    barrier -= 1
  return L

def dinuclShuffle(s):
  ok = 0
  while not ok:
    ok,edgeList,nuclList,lastCh = eulerian(s)
  nuclCnt,dinuclCnt,List = counting(s)

  for [x,y] in edgeList: List[x].remove(y)
  for x in nuclList: shuffleEdgeList(List[x])
  for [x,y] in edgeList: List[x].append(y)

  L = [s[0]]; prevCh = s[0]
  for i in range(len(s)-2):
    ch = List[prevCh][0] 
    L.append( ch )
    del List[prevCh][0]
    prevCh = ch
  L.append(s[-1])
  t = ''.join(L)
  return t
 
 





 
file_name ='ucmi.fasta' #########
seed = 1
 
seqs = open(file_name,mode='r').read().split('\n') 

arr_seqs= [] 
for i in range(len(seqs)):
            if len(seqs[i])>0:
                if(seqs[i][0]!= '>' ):
                    seqs[i] = seqs[i] 
                    arr_seqs += [seqs[i]]


arr_name= [] 
for i in range(len(seqs)):
            if len(seqs[i])>0:
                if(seqs[i][0]== '>' ):
                    seqs[i] = seqs[i] 
                    arr_name += [seqs[i]]



random.seed(seed)
h=open('Output_shuffled_'+file_name,'w') 
h2=open('Input_'+file_name,'w') 
 
  
      		 
for s in range(len(arr_seqs)): 
        		str2=arr_seqs[s] 
 
        		h.write(str(arr_name[s])+'-1'+'   '+str(dinuclShuffle(str2))+'\n' +str(for_check(dinuclShuffle(str2)))+'\n' +str(for_mon(dinuclShuffle(str2)))+'\n'+'\n') 
        		h.write(str(arr_name[s])+'-2'+'   '+str(dinuclShuffle(dinuclShuffle(str2)))+'\n' +str(for_check(dinuclShuffle(dinuclShuffle(str2))))+'\n' +str(for_mon(dinuclShuffle(dinuclShuffle(str2)))) +'\n'+'\n') 
        		h.write(str(arr_name[s])+'-3'+'   '+str(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2))))+'\n' +str(for_check(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2)))))+'\n' +str(for_mon(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2)))))+'\n'+'\n') 
        		h.write(str(arr_name[s])+'-4'+'   '+str(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2)))))+'\n' +str(for_check(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2))))))+'\n' +str(for_mon(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2))))))+'\n'+'\n') 
        		h.write(str(arr_name[s])+'-5'+'   '+str(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2))))))+'\n' +str(for_check(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2)))))))+'\n' +str(for_mon(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(dinuclShuffle(str2)))))))+'\n'+'\n')
              #'''  
 
for s in range(len(arr_seqs)):
 
        strm =  arr_seqs[s]	
        h2.write(str(arr_name[s])+'   '+str(strm)+'\n' +str(for_mon(strm))+'\n')   
        h2.write(str(for_check(strm))+'\n'+'\n') 
                        
        	
 
