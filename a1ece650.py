import sys
import re

#Global Dictionaries
Street = {}
v = {}
vbackup = {}

#Global Lists
vertices = []
edge = []
Edges = []
intersection = []
lineintersect = []
points = []

#Starting variables
imatch = 'pp'
aaa = 'start'
checker = 'no'


def streetinput(addinput):
    aaa = 'start'
    a2 = 'start'

    addstreet = re.compile('a\s"[A-Za-z]+(\s*[A-Za-z]*)*"\s((\(-?\d+,-?\d+\))+$)')

    if addstreet.match(addinput):
        x1 = addinput.split('"')
        # print(x1)
        #This is the command a
        a1 = (x1[0]).replace(" ", "")
        #This is the Street name
        a2 = x1[1]
        #These are all the coordinates
        a3 = (x1[2]).replace(","," ")

    alower = 0
    for key, value in Street.items():
        if key.lower() == a2.lower():
            alower = 1

    if a2 not in Street and alower == 0 and addstreet.match(addinput):

        coorset = []
        numcheck = re.compile('-?\d+')
        matches = numcheck.finditer(a3)
        for match in matches:
            a = float(match.group(0))
            #print(a)
            coorset.append(a)

        lencoorset = (len(coorset)/2)
        x = 0
        i = 0
        xycoor = []
        for num in coorset:
            if x < lencoorset:
                xx = coorset[i]
                yy = coorset[i+1]
                xy = (xx, yy)
                xycoor.append(xy)
                i += 2
                x += 1
        # print(xycoor)
        
        if len(coorset) < 4:
            print('Error: not enough coordinates given.')
        else:
            Street[a2] = xycoor
        # print(Street)
        # print(len(coorset))

    # elif aaa.lower() == a2.lower():
    elif alower == 1:
        print("Error: 'a' is to add a non-existing street.")
    
    else:
        print("Error: the format 'a' was inputted incorrectly.")
    # print(Street)
    

def changestreet(addinput):
    #print(Street)

    changeinput = re.compile('c\s"[A-Za-z]+(\s*[A-Za-z]*)*"\s((\(-?\d+,-?\d+\))+$)')
    if changeinput.match(addinput):
        x2 = addinput.split('"')
        #This is the command c
        c1 = (x2[0]).replace(" ", "")
        #This is the Street name
        c2 = x2[1]
        #These are all the coordinates
        c3 = (x2[2]).replace(" ","")

        clower = 0
        for key, value in Street.items():
            if key.lower() == c2.lower():
                clower = 1
                c2 = key
        # print(clower)     

        # if c2 in Street and clower == 1 and changeinput.match(addinput):
        if clower == 1 and changeinput.match(addinput):
            coorset = []
            numcheck = re.compile('-?\d+')
            matches = numcheck.finditer(c3)
            for match in matches:
                a = float(match.group(0))
                #print(a)
                coorset.append(a)
            
            lencoorset = (len(coorset)/2)
            x = 0
            i = 0
            xycoor = []
            for num in coorset:
                if x < lencoorset:
                    xx = coorset[i]
                    yy = coorset[i+1]
                    xy = (xx, yy)
                    xycoor.append(xy)
                    i += 2
                    x += 1
            # print(xycoor)
            
            if len(coorset) < 4:
                print('Not enough coordinates given.')
            else:
                Street[c2] = xycoor
        else:
            print("Error: 'c' only changes an existing street given in the correct format.")

        # print(Street)
    else:
        print("Error: 'c' only changes an existing street given in the correct format.")


def removestreet(addinput):
    # print("In Remove")

    removeinput = re.compile('r\s"[A-Za-z]+(\s*[A-Za-z]*)*"')
    if removeinput.match(addinput):
        x3 = addinput.split('"')
        #This is the command c
        r1 = (x3[0]).replace(" ", "")
        #This is the Street name
        r2 = x3[1]
        #These are all the coordinates
        r3 = (x3[2]).replace(" ","")
        
        rlower = 0
        for key, value in Street.items():
            if key.lower() == r2.lower():
                rlower = 1
                r2 = key
        # print(rlower)       

        if r2 in Street and rlower == 1 and removeinput.match(addinput):
            del Street[r2]
        else:
            print("Error: 'r', when given in the correct format, is to remove a street that already exists.")
        # print(Street)
    else:
        print("Error: 'r', when given in the correct format, is to remove a street that already exists.")


def creatingpairs():
    newstreet = {}
    #tnewstreet = {}
    linesegment = []
    #tlinesegment = []

    ii = 0
    x4 = 0
    for key, value in Street.items():
        linesegment = []
        tlinesegment = []
        kk = key
        lenlinesegment = (len(value)-1)
        x4 = 0
        ii = 0
        while x4 < lenlinesegment:
            a = value[ii]
            b = value[ii+1]
            #Change this , to plus to + avoid brackets
            lineseg = [a, b]
            # print(lineseg)
            linesegment.append(lineseg)
            ii += 1
            x4 += 1
        newstreet[kk] = linesegment
    # print("This is the newstreet: \n" + str(newstreet))

    #trying = []
    checkline = []
    tcheckline = []
    for key1, value1 in newstreet.items():
        # print(value1)
        # print(len(value1))
        for key2, value2 in newstreet.items():
            aa = len(value1)
            bb = len(value2)
            maxx = (max(aa, (bb)))
            xx = 0
            for values in value2:
                #print("This are the current values: " +str(values))
                if key2 != key1:
                    while xx < aa:
                        # print(xx)
                        line2 = values
                        # print("this is line2" + str(line2))
                        for x in line2:
                            a1 = (line2[0])
                            a = str(a1).strip('()')
                            bb = (line2[1])
                            b = str(bb).strip('()')
                            c1 = a + ', ' + b

                        line1 = value1[xx]
                        for x in line1:
                            a1 = (line1[0])
                            a = str(a1).strip('()')
                            bb = (line1[1])
                            b = str(bb).strip('()')
                            c2 = a + ', ' + b


                        check = [line1, line2]
                        tcheck = c2 + ', ' + c1
                        # print(check)
                        # print("this is tcheck\t" + str(tcheck))

                        h1 = 'Yes'
                        for value in tcheckline:
                            firstpart = re.compile('^(-?\d+.\d+,\s-?\d+.\d+,\s-?\d+.\d+,\s-?\d+.\d+)')
                            m1 = firstpart.finditer(value)
                            tc1 = firstpart.finditer(tcheck)
                            
                            secondpart = re.compile('(-?\d+.\d+,\s-?\d+.\d+,\s-?\d+.\d+,\s-?\d+.\d+)$')
                            m2 = secondpart.finditer(value)
                            tc2 = secondpart.finditer(tcheck)

                            for match in m1:
                                p1 = match.group(0)
                                # print("This is p1 " + str(p1))
                            for match in tc1:
                                t1 = match.group(0)
                                # print("This is t1 " + str(t1))
                            for match in m2:
                                p2 = match.group(0)
                                # print("This is p2 " + str(p2))
                            for match in tc2:
                                t2 = match.group(0)
                                # print("This is t2 " + str(t2))
                            if (t1 == p1 or t1 == p2) and (t2 == p1 or t2 == p2):
                                # print('Here')
                                # check = ""
                                h1 = 'No'
                                #Is this break put in correctly? I wanted to break out of the loop if they coordinates all match
                                break
                            else:
                                h1 = 'Yes'
                                # print(h1)
                            # print("This is part1 " + str(p1))
                            # print("This is part2 " + str(p2))


                        if h1 == 'Yes':
                            # print('put in')
                            checkline.append(check)
                            # print(checkline)
                            tcheckline.append(tcheck)
                            h1 = 'Yes'
                        xx +=1
    # print('\nThis is checkline\n' + str(checkline))
    intersection_vertices(checkline)

def intersection_vertices(checkline):
    # vertices = []
    # edge = []
    # Edges = []
    # intersection = []
    # lineintersect = []
    # print(checkline)
    key = 1
    for value in checkline:
        store1 = value
        # print(store1)
        time = 0
        for value1 in store1:
            store2 = value1
            
            for value2 in store2:
                # print(value2)
                if time == 0:
                    x1 = value2[0]
                    y1 = value2[1]
                    # time += 1
                    # print(time)
                if time == 1:
                    x2 = value2[0]
                    y2 = value2[1]
                    # time += 1 
                    # print(time)
                if time == 2:
                    x3 = value2[0]
                    y3 = value2[1]
                    # time += 1
                    # print(time)
                if time == 3:
                    x4 = value2[0]
                    y4 = value2[1]
                    # print('This is x1 :' + str(x1) + ' ' + str(y1) + ' This is x4 :' + str(x4) + ' ' + str(y4) + '\n')
                    #Math should run in here

                    
                    xnum = (x2*y1-x1*y2)*(x4-x3) - (x2-x1)*(x4*y3-x3*y4)
                    xden = (y1-y2)*(x4-x3) - (x2-x1)*(y3-y4)
                    ynum = (y1-y2)*(x4*y3-x3*y4) - (x2*y1-x1*y2)*(y3-y4)
                    yden = (y1-y2)*(x4-x3) - (x2-x1)*(y3-y4)
                    # print('xnum: ' + str(xnum) + ' xden: ' + str(xden) + ' ynum: ' + str(ynum) + ' yden: ' + str(yden))

                    #The lower case edges are temporary (all possible edges), these below are overlapping streets
                    #So every point counts towards a vertice and a possible a edge
                    if xnum==0 and ynum==0 and xden==0 and yden==0 :
                        if (x1,y1) not in vertices: vertices.append((x1,y1))
                        if (x1,y1) not in edge: edge.append((x1,y1))
                        if (x2,y2) not in vertices: vertices.append((x2,y2))
                        if (x2,y2) not in edge: edge.append((x2,y2))
                        if (x3,y3) not in vertices: vertices.append((x3,y3))
                        if (x3,y3) not in edge: edge.append((x3,y3))
                        if (x4,y4) not in vertices: vertices.append((x4,y4))
                        if (x4,y4) not in edge: edge.append((x4,y4))
                        sortededge= sorted(edge , key=lambda k: [k[0], k[1]])
                        if (sortededge[0],sortededge[1]) not in Edges: Edges.append((sortededge[0],sortededge[1]))
                        if (sortededge[1],sortededge[2]) not in Edges: Edges.append((sortededge[1],sortededge[2]))
                        # print("These are the sorted edges:" + str(sortededge))
                        del edge[:]
                    if xden == 0 or yden == 0:
                        time += 1
                        continue
                    #To avoid mutual abcisses
                    elif (max(x1,x2) < min(x3,x4)):
                        time += 1
                        continue
                    #To avoid mutual ordinates
                    elif (max(y1,y2) < min(y3,y4)):
                        time += 1
                        continue
                    else:
                        #This is where the intersedtion is calculated
                        xc = xnum / xden
                        yc = ynum / yden
                        # print('This is xc: ' + str(xc) + ' this is yc: ' + str(yc))
                        #These all for the points on the line segment to only be considered
                        if (xc < max(min(x1,x2),min(x3,x4))) or (xc > min(max(x1,x2),max(x3,x4))):
                            time += 1
                            continue
                        elif (yc < max(min(y1,y2),min(y3,y4))) or (yc > min(max(y1,y2),max(y3,y4))):
                            time += 1
                            continue
                        else:
                            #Every set that created the intersection is a vertice
                            if (xc,yc) not in vertices: vertices.append((xc,yc))
                            if (xc,yc) not in intersection: intersection.append((xc,yc))
                            if (x1,y1) not in vertices: vertices.append((x1,y1))
                            if (x2,y2) not in vertices: vertices.append((x2,y2))
                            if (x3,y3) not in vertices: vertices.append((x3,y3))
                            if (x4,y4) not in vertices: vertices.append((x4,y4))
                            if ((x1,y1),(x2,y2)) not in lineintersect: lineintersect.append(((x1,y1),(x2,y2)))
                            if ((x3,y3),(x4,y4)) not in lineintersect: lineintersect.append(((x3,y3),(x4,y4)))
                            #Every set with their intersection counts towards a possible Edge
                            if ((x1,y1),(xc,yc)) not in Edges: Edges.append(((x1,y1),(xc,yc)))
                            if ((x2,y2),(xc,yc)) not in Edges: Edges.append(((x2,y2),(xc,yc)))
                            if ((x3,y3),(xc,yc)) not in Edges: Edges.append(((x3,y3),(xc,yc)))
                            if ((x4,y4),(xc,yc)) not in Edges: Edges.append(((x4,y4),(xc,yc)))
                            
                            else:
                                time += 1
                                continue
                
                else:
                    time += 1
                    continue
                    # print('This is x1 :' + str(x1) + ' ' + str(y1) + ' This is x4 :' + str(x4) + ' ' + str(y4))
                # time += 1
                    
    # print('These are the vertices:\n' + str(vertices))
    # print('These are the Edges:\n' + str(Edges))
    # print('These are the edges:\n' + str(edge))
    moreedges()


def moreedges():
    for i in range (0,len(lineintersect)):
        #create equation
        del points[:]
        x1=lineintersect[i][0][0]
        y1=lineintersect[i][0][1]
        x2=lineintersect[i][1][0]
        y2=lineintersect[i][1][1]
        
        count=0 
        for w in range (0,len(vertices)):
            x=vertices[w][0]
            y=vertices[w][1]
            if (x2 <= x <= x1) or (x1 <= x <= x2):
                l=int((y-y1)*(x2-x1))
                r=int((y2-y1)*(x-x1))
            
                if(l==r):
                    count +=1
                    if (x1,y1) not in points: points.append((x1,y1))
                    if (x2,y2) not in points: points.append((x2,y2))
                    if (x,y) not in points: points.append((x,y))
                elif(l!=r):
                    continue
            else:
                continue
        if count >= 3:
            sortedpoints= sorted(points , key=lambda k: [k[0], k[1]]) 
            for o in range (0,len(sortedpoints)-1):
                x1=sortedpoints[o][0]
                y1=sortedpoints[o][1]
                x2=sortedpoints[o+1][0]
                y2=sortedpoints[o+1][1]
                if ((x1,y1),(x2,y2)) not in Edges: 
                    if ((x2,y2),(x1,y1)) not in Edges:
                        Edges.append(((x1,y1),(x2,y2)))
            for z in range (0,len(sortedpoints)-2):
                x1=sortedpoints[z][0]
                y1=sortedpoints[z][1]
                for u in range(0,len(sortedpoints)-2-z):
                    x2=sortedpoints[z+u+2][0]
                    y2=sortedpoints[z+u+2][1]
                    f=(x1,y1),(x2,y2)
                    g=(x2,y2),(x1,y1)
                    if ((x1,y1),(x2,y2)) in Edges:
                        Edges.remove(f)
                    elif ((x2,y2),(x1,y1)) in Edges:
                        Edges.remove(g)
            for (x,y) in Edges:
                if x==y:
                    Edges.remove((x,y))
    return None




def main():
    ccv = 1 #This is to create the indexes
    cc = 0 #This is to know if the first statement has already been run
    checker = 'no'

    while True:
        addinput = sys.stdin.readline()
        imatch = 'pp'
        
        if (not (addinput and addinput.strip())):
            # print('Its empty')
            break

        checkinput = re.compile('^[acrg]')
        inputmatch = checkinput.finditer(addinput)
        for match in inputmatch:
            imatch = match.group(0)
        if imatch == 'a' or imatch == 'c' or imatch == 'r' or imatch == 'g':
            # print("We found a match.")
            imatch = 'pp'

            checka = re.compile('a "')
            amatch = checka.finditer(addinput)
            for match in amatch:
                amatched = match.group(0)
                if amatched == 'a "':
                    streetinput(addinput)

            checkc = re.compile('c "')
            cmatch = checkc.finditer(addinput)
            for match in cmatch:
                cmatched = match.group(0)
                if cmatched == 'c "':
                    changestreet(addinput)

            checkr = re.compile('r "')
            rmatch = checkr.finditer(addinput)
            for match in rmatch:
                rmatched = match.group(0)
                if rmatched == 'r "':
                    removestreet(addinput)

            checkg = re.compile('^g$')
            gmatch = checkg.finditer(addinput)
            for match in gmatch:
                gmatched = match.group(0)
                if gmatched == 'g':
                    v.clear()        
                    del vertices[:]
                    del Edges[:]
                    creatingpairs()
                    # print(vertices)


                    if cc == 0:
                        for i in range(0, len(vertices)):
                            v.update({ccv: vertices[i]})
                            vbackup.update({ccv: vertices[i]})
                            ccv += 1
                        sys.stdout.write("V = {")
                        for key,value in sorted(v.items()):
                            # print(value[0])
                            sys.stdout.write("\n  %d" %key)
                            sys.stdout.write(" :  (%d" %value[0])
                            sys.stdout.write(",%d)" %value[1])
                        sys.stdout.write("\n}")
                        # print('This is what is in v:\n' + str(v))
                        # print('This is what is in vbackup:\n' + str(vbackup))

                    if cc >= 1:
                        for i in range(0, len(vertices)):
                            for key, value in vbackup.items():
                                #if (vertices[i][0] == value[key][0]) and (vertices[i][1] == value[key][1]):
                                # print("This is vertices[i]: " + str(vertices[i]))
                                # print("This is value: " + str(value))
                                # print("This is vertices[i][0]: " + str(vertices[i][0]))
                                # print("This is value[0]: " + str(value[0]))
                                if vertices[i] == value:
                                    oldkey = key
                                    v.update({oldkey: vertices[i]})
                                    ccv += 1
                                    checker = 'yes'
                            if checker == 'no':
                                v.update({ccv: vertices[i]})
                                vbackup.update({ccv: vertices[i]})
                                checker = 'no'
                                ccv += 1
                        sys.stdout.write("V = {")
                        for key,value in sorted(v.items()):
                            sys.stdout.write("\n  %d" %key)
                            sys.stdout.write(" :  (%d" %value[0])
                            sys.stdout.write(",%d)" %value[1])
                        sys.stdout.write("\n}")
                        # print('2This is what is in v:\n' + str(v))
                        # print('2This is what is in vbackup:\n' + str(vbackup))
                    if cc == 0:
                        cc += 1

                    #This is to sort out edges by vertice index
                    sys.stdout.write ("\nE = {")
                    for i in range(0,len(Edges)):
                        for key1,value in v.items()  :
                            if Edges[i][0]==value:
                                for key2,value in v.items():
                                    if Edges[i][1]==value:
                                        if i==len(Edges)-1:
                                            sys.stdout.write ("\n  <%d" %key1)
                                            sys.stdout.write (",%d" %key2)
                                            sys.stdout.write( ">\n")
                                        else:
                                            sys.stdout.write ("\n  <%d" %key1)
                                            sys.stdout.write (",%d" %key2)
                                            sys.stdout.write( ">,")
                    sys.stdout.write ("}\n")
                    sys.stdout.flush()
        else:
            print("Error: 'a', 'c', 'r', 'g' are the only commands allowed.")
            main()
    print 'Finished reading input'
    return sys.exit(0)

if __name__ == "__main__":
    main()
