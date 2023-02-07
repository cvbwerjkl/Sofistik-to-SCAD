file_name = 'Data.dat' #prime file name
file_name_loads = 'Loads.txt' #loads file name

#nodes correction
i = 1
with open ('out_nodes_SCAD.txt', 'w') as ouf:    
  ouf.write('\n' + '(4/' + '\n')
with open ('out_nodesdic_SCAD.txt', 'w') as ouf:    
  ouf.write('')
nodesdic={} #библиотека номеров узлов
with open (file_name, 'r') as inf:
  for line in inf:
    if line[0] == 'N' and line[1] == 'O' and line[2] == 'D' and line[5] == ' ':
      line = line.replace ('N', '')
      line = line.replace ('O', '')
      line = line.replace ('D', '')
      line = line.replace ('E', '')
      line = line.replace ('X', '')
      line = line.replace ('Y', '')
      line = line.replace ('Z', '')
      line = line.replace ('F', '')
      line = line.replace ('I', '')
      line = line.replace ('X', '')
      line = line.replace ('P', '')
      line = line.replace ('M', '')
      i = i+1
      line = line.strip()
      a=0
      NodeNum=''
      while line[a] !=' ': 
        NodeNum = line[:a+1]
        a=a+1
      nodesdic[NodeNum]=str(i-1)
     # print (nodesdic)
     # print (NodeNum)
     # with open ('out_nodes.txt', 'a') as ouf:
     #  ouf.write(line)
      line = line.strip()
      n = 0
      while line[n] !=' ':
        line = line[n+1:]
      line = line.strip()
      line = line + '/' 
      with open ('out_nodes_SCAD.txt', 'a') as ouf:
        ouf.write(line + '\n') 
      with open ('out_nodesdic_SCAD.txt', 'a') as ouf:
        ouf.write('\n' + nodesdic[NodeNum] + ' ' + NodeNum)
with open ('out_nodes_SCAD.txt', 'a') as ouf:
  ouf.write(')') 

#sections correction
with open ('out_secs_SCAD.txt','w') as ouf:
  ouf.write('')
secdic={} #библиотека соответствия сечений и номеров
Matdic={} #библиотека соответствия материалов и номеров
scitsecdic={} #библиотека соответствия круглых сечений и номеров
smnosecdic={} #библиотека соответствия сечений пластин и номеров
MatTitldic = {} #библиотека соответствия наименования материалов и номеров
#material propertis collection
MatTitldic = {} #библиотека соответствия наименования материалов и номеров
with open (file_name,'r') as inf:  #открытие исходного файла
  for line in inf:
    #line = line.strip()
    if line[0] == 'C' and line[1] == 'O':
      line = line.strip()
      n = len(line) 
      bb = len(line)
      MatTitl = line
      while line[n-1] !='=':
        n = n-1 
      MatTitl = MatTitl[n:bb-1]
      line = line.replace('C','')  #вырезание символов из строки
      line = line.replace('O','')
      line = line.replace('N','')
      line = line.replace('C','')
  #сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      MatNum = line[:n]
      MatTitldic[MatNum] = MatTitl #запись в библиотеку наименований материалов  
    if line[0] == 'S' and line[1] == 'T' and line[2] == 'E' and line [3] == 'E':
      line = line.strip()
      n = len(line) 
      bb = len(line)
      MatTitl = line
      while line[n-1] !='=':
        n = n-1 
      MatTitl = MatTitl[n:bb-1]
      line = line.replace('S','')  #вырезание символов из строки
      line = line.replace('T','')
      line = line.replace('E','')
      line = line.replace('E','')
  #сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      MatNum = line[:n]
      MatTitldic[MatNum] = MatTitl #запись в библиотеку наименований материалов
#rectungular sections correction
    if line[0] == 'S' and line[1] == 'R':
      line = line.replace('S','')  #вырезание символов из строки
      line = line.replace('R','')
      line = line.replace('E','')
      line = line.replace('C','')
      line = line.replace('H','')
      line = line.replace('B','')
      line = line.replace('O','')
      line = line.replace('U','')
      line = line.replace('M','')
      line = line.replace('N','')
#сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      srecsecNum = line[:n]
      line = line[n:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      srecsec1SEC = line[:n]
      line = line[n:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      srecsec2SEC = line[:n]
      line = line[n:]
#вырезание не нужных символов из строки слева
      for ii in range (3):     
        line = line.strip() 
        n = 0  
        #print (n)
        while line[n] !=' ':
          line = line[n+1:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      srecMatNum = line[:n]

      secdic[srecsecNum] = 'S0' + ' ' + '0' + ' ' + srecsec1SEC + ' ' + srecsec2SEC + ' EM 0 NU 0.2 Name"' + MatTitldic[srecMatNum] + '"' #запись в библиотеку характеристик сечений
      Matdic[srecsecNum] = srecMatNum #запись в библиотеку характеристик материалов
#circular sections correction
    if line[0] == 'S' and line[1] == 'C':
      line = line.replace('S','')  #вырезание символов из строки
      line = line.replace('C','')
      line = line.replace('I','')
      line = line.replace('T','')
      line = line.replace('D','')
      line = line.replace('A','')
      line = line.replace('O','')
      line = line.replace('M','')
      line = line.replace('N','')
  #сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      scitsecNum = line[:n]
      line = line[n:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      scitsecSEC = line[:n]
      line = line[n:]
  #вырезание не нужных символов из строки слева
      for ii in range (1):     
        line = line.strip() 
        n = 0  
        #print (n)
        while line[n] !=' ':
          line = line[n+1:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      scitMatNum = line[:n]
      secdic[scitsecNum] = 'S6' + ' ' + '0' + ' ' + scitsecSEC + ' ' + '0.0005' + ' EM 0 NU 0.2 Name"' + MatTitldic[scitMatNum] + '"'#запись в библиотеку характеристик сечений
      Matdic[scitsecNum] = scitMatNum #запись в библиотеку характеристик материалов
      #print (secdic, Matdic)
#steel sections correction
    if line[0] == 'S' and line[1] == 'E' and line[2] == 'C' and line[3] == 'T':
      line = line.replace('S','')  #вырезание символов из строки
      line = line.replace('E','')
      line = line.replace('C','')
      line = line.replace('T','')
      line = line.replace('D','')
      line = line.replace('A','')
      line = line.replace('O','')
      line = line.replace('M','')
      line = line.replace('N','')
  #сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      scitsecNum = line[:n]
      line = line[n:]
      line = line.strip()
      n=0
      while line[n] !=' ':
        n = n+1 
      scitMatNum = line[:n]
      secdic[scitsecNum] = 'S6' + ' ' + '0' + ' ' + '30' + ' ' + '0.0005' + ' EM 0 NU 0.2 Name"' + MatTitldic[scitMatNum] + '"'#запись в библиотеку характеристик сечений
      Matdic[scitsecNum] = scitMatNum #запись в библиотеку характеристик материалов
      #print (secdic, Matdic)
#material propertis collection
    if line[0] == 'C' and line[1] == 'O':
      line = line.replace('C','')  #вырезание символов из строки
      line = line.replace('O','')
      line = line.replace('N','')
      line = line.replace('C','')
  #сбор номеров жесткостей в библиотеку
      line = line.strip()
      n = 0
      while line[n] !=' ':
        n = n+1 
      MatNum = line[:n]
      line = line[n:]
      line = line.strip()
      n = len(line) 
      bb = len(line)
      MatTitl = line
      while line[n-1] !='=':
        n = n-1 
      line = line[:n-1]
      MatTitl = MatTitl[n:bb-1]
      MatTitldic[MatNum] = MatTitl #запись в библиотеку наименований материалов  
#print(MatTitldic)


#quad correction
with open ('out_quads_SCAD.txt','w') as ouf:
  ouf.write('')
i = 1 #счетчик номера пластин 
quasecdic={} #библиотека соответствия жесткостей и номеров 4пластины
quaNod1dic={} #библиотека соответствия 1 узла и номеров 4пластины
quaNod2dic={} #библиотека соответствия 2 узла и номеров 4пластины
quaNod3dic={} #библиотека соответствия 3 узла и номеров 4пластины
quaNod4dic={} #библиотека соответствия 4 узла и номеров 4пластины
quaMatdic={} #библиотека соответствия материалов и номеров 4пластин
with open (file_name,'r') as inf:  #открытие исходного файла
  for line in inf:
    #line = line.strip()
    if line[0] == 'Q' and line[1] == 'U':
      line = line.replace('Q','')  #вырезание символов из строки
      line = line.replace('U','')
      line = line.replace('A','')
      line = line.replace('D','') 
      line = line.replace('M','')
      line = line.replace('N','')
      line = line.replace('O','') 
      line = line.replace('R','')
      line = line.replace('F','')
      line = line.replace('N','')
      line = line.replace('P','')
      line = line.replace('S','')
      line = line.replace('I','')
      line = line.replace('T','')
      line = line.replace('C','')
      line = line.replace('X','') 
      line = line.replace('B','')
      line = line.replace('E','')
      line = line.replace('L','')
      line = line.replace('V','')
#вырезание не нужных символов из строки справа
      for ii in range (5):     
        line = line.strip() 
        n = len(line)  
        #print (n)
        while line[n-1] !=' ':
          line = line[:n-1]
          n = n-1
      #print(line) 
#сбор жесткостей в библиотеку
      line = line.strip()
      n = len(line)
      quasecNum = line
      while line[n-1] !=' ':
        n = n-1 
      line = line[:n-1]
      quasecNum = quasecNum[n:]
      line = line.strip()
      #print (quasecdic)
#вырезание не нужных символов из строки справа
      for ii in range (2):     
        line = line.strip() 
        n = len(line)  
        #print (n)
        while line[n-1] !=' ':
          line = line[:n-1]
          n = n-1
      line = line.strip()
#сбор материалов в библиотеку
      line = line.strip()
      n = len(line)
      quaMatNum = line
      while line[n-1] !=' ':
        n = n-1 
      line = line[:n-1]
      quaMatNum = quaMatNum[n:]
      quaMatdic[i]=quaMatNum #запись в библиотеку
      line = line.strip()
#сбор 4 узла 4пластин в библиотеку
      n = len(line)
      quaNod4Num = line
      while line[n-1] !=' ':
        n = n-1
      line = line[:n-1] 
      quaNod4Num = quaNod4Num[n:]
      quaNod4dic[i]=quaNod4Num #запись в библиотеку
      #with open ('out_secdic.txt', 'a') as ouf: #!!!
      #  ouf.write(quaNod4Num + '\n')      #!!!
      line = line.strip()
      #print (line)
#сбор 3 узла 4пластин в библиотеку
      n = len(line)
      quaNod3Num = line
      while line[n-1] !=' ':
        n = n-1
      line = line[:n-1] 
      quaNod3Num = quaNod3Num[n:]
      quaNod3dic[i]=quaNod3Num #запись в библиотеку
      line = line.strip()
      #print (line)
#сбор 2 узла 4пластин в библиотеку
      n = len(line)
      quaNod2Num = line
      while line[n-1] !=' ':
        n = n-1
      line = line[:n-1] 
      quaNod2Num = quaNod2Num[n:]
      quaNod2dic[i]=quaNod2Num #запись в библиотеку
      line = line.strip()
      #print (line)
#сбор 1 узла 4пластин в библиотеку
      n = len(line)
      quaNod1Num = line
      while line[n-1] !=' ':
        n = n-1
      line = line[:n-1] 
      quaNod1Num = quaNod1Num[n:]
      quaNod1dic[i]=quaNod1Num #запись в библиотеку
      line = line.strip()
      #print (line)      
      nn = len(secdic)
      #print(MatTitldic)
      dd = ' GE 3e+007 0.2 ' + quasecNum + ' RO 2.45 TMP 1e-005 1e-005' + '\n'  +  '    Material ="{00000048-0000-0000-0100-000000000000}" Name"' + MatTitldic[quaMatNum] + '"'
      iii=0
      ddd = 'not'
      for key in secdic:
        if secdic[key] == dd:
            ddd = key  
      if ddd == 'not':
        nnnn = str(nn+1)
        secdic[nnnn] = dd
        quasecNum2 = nnnn
      else:
        quasecNum2 = ddd
      quasecdic[i]=quasecNum2 #запись в библиотеку
      i = i+1 #счетчик номера 4пластин
      #print(secdic) 

#print (quasecdic)
#print(quasecdic[5])
#print (quaNod4dic)
#print (quaNod3dic)
#print (quaNod2dic)
#print (quaMatdic)
#замена номеров узлов 4пластин
for c in range (i-1):
  Nod1 = str(quaNod1dic[c+1])
  #print(nodesdic[Nod1])
  Nod2 = str(quaNod2dic[c+1])
  #print(nodesdic[Nod2])
  Nod3 = str(quaNod3dic[c+1])
  #print(nodesdic[Nod3])
  Nod4 = str(quaNod4dic[c+1])
  #print(nodesdic[Nod4])
  #print(nodesdic[Nod1])
  with open ('out_quads_SCAD.txt', 'a') as ouf:
      ouf.write('44' + ' ' + quasecdic[c+1] + ' ' + nodesdic[Nod1] + ' ' + nodesdic[Nod2] + ' ' + nodesdic[Nod4] + ' ' + nodesdic[Nod3] +'/' + '\n')
with open ('out_quads_SCAD.txt', 'a') as ouf:
    ouf.write(')' + '\n')

#beams correction
with open ('out_beams_SCAD.txt','w') as ouf:
  ouf.write('(1/')
i = 1 #счетчик номера стержня 
bemsecdic={} #библиотека соответствия жесткостей и номеров стержня
bemNod1dic={} #библиотека соответствия 1 узла и номеров стержня
bemNod2dic={} #библиотека соответствия 2 узла и номеров стержня
with open (file_name,'r') as inf:
  for line in inf:
    if line[0] == 'B' and line[1] == 'E':
      line = line.replace('B','')  #вырезание символов из строки
      line = line.replace('E','')
      line = line.replace('A','')
      line = line.replace('M','') 
      line = line.replace('N','')
      line = line.replace('C','')
      line = line.replace('S','') 
      line = line.replace('D','')
      line = line.replace('R','')
      line = line.replace('X','') 
      line = line.strip() 
      n = len(line)  #вырезание не нужных символов из строки справа
      #print (n)
      while line[n-1] !=' ':
        line = line[:n-1]
        n = n-1
      line = line.strip()
      #print(line)
      n = len(line)  #вырезание не нужных символов из строки справа
      while line[n-1] !=' ':
        line = line[:n-1]
        n = n-1
      line = line.strip()
      #print(line)
      n = len(line)  #вырезание не нужных символов из строки справа
      while line[n-1] !=' ':
        line = line[:n-1]
        n = n-1
      line = line.strip()
      #print(line) 
      n = len(line)
      bemsecNum = line
      while line[n-1] !=' ': #сбор значения жесткостей стержней в библиотеку
        n = n-1 
      line = line[:n-1]
      bemsecNum = bemsecNum[n:]
      bemsecdic[i]=bemsecNum #запись в библиотеку
      line = line.strip()
      #print (line)
      n = len(line)
      bemNod2Num = line
      while line[n-1] !=' ': #сбор значения 2 узла стержней в библиотеку
        n = n-1
      line = line[:n-1] 
      bemNod2Num = bemNod2Num[n:]
      bemNod2dic[i]=bemNod2Num #запись в библиотеку
      line = line.strip()
      #print (line)
      n = len(line)
      bemNod1Num = line
      while line[n-1] !=' ': #сбор значения 1 узла стержней в библиотеку
        n = n-1
      line = line[:n-1] 
      bemNod1Num = bemNod1Num[n:]
      bemNod1dic[i]=bemNod1Num #запись в библиотеку
      i = i+1 #счетчик номера стержня
#print (bemsecdic)
#print (bemNod2dic)
#print (bemNod1dic)
for c in range (i-1):
  Nod1 = str(bemNod1dic[c+1])
  #print(nodesdic[Nod1])
  Nod2 = str(bemNod2dic[c+1])
  with open ('out_beams_SCAD.txt', 'a') as ouf: 
      ouf.write('5' + ' ' + bemsecdic[c+1] + ' ' + nodesdic[Nod2] + ' ' + nodesdic[Nod1] + '/' + '\n')

#sections file creation
with open ('out_secs_SCAD.txt','w') as ouf:
  ouf.write('')
with open ('out_secs_SCAD.txt', 'a') as ouf:
  ouf.write('(3/')
  gg = len(secdic) 
  for cc in range(gg):
    kk = str(cc+1)
    #if kk in secdic:
    ouf.write('\n' + kk + ' ' + secdic[kk]+'/')
  ouf.write(')')  
 
#loads correction
with open ('out_loads_SCAD.txt', 'w') as ouf:    
  ouf.write('\n' + '(7/' + '\n')
with open ('out_loadsdis_SCAD.txt', 'w') as ouf:    
  ouf.write('\n' + '(6/' + '\n')
  ouf.write('1 Name="SW" Type=9 Mode=1 ReliabilityFactor=1.1 /' + '\n')
i = 1
with open (file_name_loads, 'r') as inf:
  for line in inf:
    line = line.strip()
    if line == '' or line[0] == ' ':
      t = 0#useless
    elif line[0] == 'A' and line[1] == 'p':
      i = i + 1
      si = str(i)
      ll = len(line)
      with open ('out_loadsdis_SCAD.txt','a') as ouf:
        ouf.write(si + ' Name="' + line[ll-2:] + '" Type=9 Mode=1 ReliabilityFactor=1.1 /' + '\n')
      with open ('out_loads_SCAD.txt','a') as ouf:
        ouf.write('\n' + '0 3 Load=' + si + ' 0.0001:1 /' + '\n')
    elif line[0] != 'A' and line[0] != 'N':
      #reversing of node numbers
      a=0 
      NodeNumLoad=''
      while line[a] !=' ': 
        NodeNumLoad = line[:a+1]
        a=a+1
      line = line.strip()
      n = 0
      while line[n] !=' ':
        line = line[n+1:]
      line = line.strip()
      ds = 0
      tt = 0
      for ww in range(3):
        n = 0
        a = 0
        line2 = line
        ds = ds + 1
        while line[n] !=' ':
          line = line[n+1:]
          a = a + 1 
        tt = tt + 1
        line2 = line2[:a]
        #print(line2)
        line = line.strip()
        #adding line to file if nodal load not 0
        if line2 != '0.0' and line2 != '0.00':
          if NodeNumLoad in nodesdic != False:
            line3 = float(line2)#reversing of nodal load orientation
            line3 = line3 * -0.0001
            line3 = round(line3, 7)
            line3 = str(line3)
            strtt = str(tt)
            with open ('out_loads_SCAD.txt','a') as ouf:
              ouf.write('0' + ' ' + strtt + ' ' + line3 + ':' + nodesdic[NodeNumLoad] + ' /' + '\n')
          else:
            print (NodeNumLoad, 'узел отсутствует в списке   LoadCaseNumber=', si)

with open ('out_loads_SCAD.txt', 'a') as ouf:    
  ouf.write(')' + '\n')
with open ('out_loadsdis_SCAD.txt', 'a') as ouf:    
  ouf.write(')')

#files connection
with open ('out_summary_SCAD.txt','w') as ouf:
  ouf.write('(0;Version=21/' + '\n')
  ouf.write('1;"NONAME";/' + '\n')
  ouf.write('2;5/' + '\n' + '\n')
  ouf.write('23;LoadingCode=1;' + '\n')
  ouf.write('SteelCode=1;' + '\n')
  ouf.write('ConcreteCode=1;' + '\n')
  ouf.write('SafetyCode=1;' + '\n')
  ouf.write('NoForceInsert=1;' + '\n')
  ouf.write('CoeffIntervalGeom=5;' + '\n')
  ouf.write('/' + '\n' + '\n')
  ouf.write('33;м 1 м 1 Т 1 /)' + '\n' + '\n')

ouf = open ('out_summary_SCAD.txt','a')
inf = open ('out_beams_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
inf = open ('out_quads_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
inf = open ('out_secs_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
inf = open ('out_nodes_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
inf = open ('out_loadsdis_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
inf = open ('out_loads_SCAD.txt','r') 
for line in inf:
  ouf.write(line)
inf.close()
ouf.close()
