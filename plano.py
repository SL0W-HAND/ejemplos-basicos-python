def run():

   # from prettytable import prettyTable

    puntoP = {
        'x':0,
        'y':1,
        'z':0
    }
    puntoQ = {
        'x':1,
        'y':1,
        'z':0
    }
    puntoR = {
        'x':1,
        'y':1,
        'z':1
    }

    print('PQ = (' + str(puntoQ['x']) + '-' + str(puntoP['x']) + ","+ str(puntoQ['y'])+ '-' + str(puntoP['y']) + "," +str(puntoQ['z']) + '-' + str(puntoP['z']) + ') = (' + str(puntoQ['x']-puntoP['x'])  + "," + str(puntoQ['y']-puntoP['y']) + "," + str(puntoQ['z']-puntoP['z']) + ')')
    print('')
    print('QR = (' + str(puntoR['x']) + '-' + str(puntoQ['x']) + ","+ str(puntoR['y'])+ '-' + str(puntoQ['y']) + "," +str(puntoR['z']) + '-' + str(puntoQ['z']) + ') = (' + str(puntoR['x']-puntoQ['x'])  + "," + str(puntoR['y']-puntoQ['y']) + "," + str(puntoR['z']-puntoQ['z']) + ')')
    print('')

    pq = {
        'i':puntoQ['x']-puntoP['x'],
        'j':puntoQ['y']-puntoP['y'],
        'k':puntoQ['z']-puntoP['z']
    }
    qr = {
        'i':puntoR['x']-puntoQ['x'],
        'j':puntoR['y']-puntoQ['y'],
        'k':puntoR['z']-puntoQ['z']
    }

    #myTable = PrettyTable({"i","j","k"})
    #myTable.add_row([pq['i'],pq['j'],pq['k']])
    #myTable.add_row([qr['i'],qr['j'],qr['k']])

    pqxqr = {
        'i':(pq['j']*qr['k'])-(pq['k']*qr['j']),
        'j':(pq['k']*qr['i'])-(pq['i']*qr['k']),
        'k':(pq['i']*qr['j'])-(pq['j']*qr['i'])
    }

    print("PQxQR = " + str(pqxqr['i']) + 'i' + str(pqxqr['j']) + 'j' + str(pqxqr['k']) + 'k' + '= ('+ str(pqxqr['i']) + ',' + str(pqxqr['j']) + ',' + str(pqxqr['k']) + ')' )

    print('')
    print('π:' + str(pqxqr['i']) + '(x-' + str(puntoP['x']) + ') + ' + str(pqxqr['j']) + '(y-' + str(puntoP['y']) + ') + ' + str(pqxqr['k']) + '(z-' + str(puntoP['z']) + ') = 0')
    print('')
    print('  ' + str(pqxqr['i'])  + 'x +' + str(pqxqr['i']*-puntoP['x']) + '+'  + str(pqxqr['j'])  + 'y +' + str(pqxqr['j']*-puntoP['y']) + '+'  + str(pqxqr['k'])  + 'z +' + str(pqxqr['k']*-puntoP['z']) + ' = 0' )
    print('') 
    print('  ' + str(pqxqr['i'])  + 'x +' + str(pqxqr['j'])  + 'y +' + str(pqxqr['k'])  + 'z +' + str((pqxqr['i']*-puntoP['x'])+(pqxqr['j']*-puntoP['y'])+(pqxqr['k']*-puntoP['z'])) + ' = 0')
    print('')
    print('  ' + str(pqxqr['i'])  + 'x +' + str(pqxqr['j'])  + 'y +' + str(pqxqr['k'])  + 'z = ' + str(-((pqxqr['i']*-puntoP['x'])+(pqxqr['j']*-puntoP['y'])+(pqxqr['k']*-puntoP['z']))))

if __name__ == '__main__':
    run()