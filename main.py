import re

def lista_a_palabra(lista):
     return ''.join(lista)

def y_vocal(cadena):
    i = 0
    while i < len(cadena):
        if cadena[i] == 'y' and (i == len(cadena) - 1 or cadena[i + 1] not in ['a', 'e', 'i', 'o', 'u']):
            cadena = cadena[:i] + 'ç' + cadena[i+1:]
            i += 2  
        else:
            i += 1
    return cadena


def guiones_a_lista(cadena):
    cadena=cadena.replace(',','')
    cadena=cadena.replace('ç','y')
    cadena=cadena.rstrip('-')
    cadenaresultado=""
    lista=[]
    for i in range(len(cadena)):
        if cadena[i]!='-':
            cadenaresultado+=cadena[i]
        else:
            lista.append(cadenaresultado)
            cadenaresultado=""

    
    lista.append(cadenaresultado)   
    return lista


def silabear(cadena):
    R1=r"(?P<regla1>([aeiouáéíóúïü])(([bcdfghjklmnñpqrstvwxyz]|ll|rr|ch)[aeiouáéíóúïüç]))" 
    R2a=r"(?P<regla2a>([aeiouáéíóúïü])([pcbgf][rl][aeiouáéíóúïü]))"
    R2b=r"(?P<regla2b>([aeiouáéíóúïü])([dt][r][aeiouáéíóúïü]))"
    R2c=r"(?P<regla2c>([aeiouáéíóúïü][bcdfghjklmnñpqrstvwxyz])([bcdfghjklmnñpqrstvwxyz][aeiouáéíóúïü]))"
    R3a=r"(?P<regla3a>([aeiouáéíóúïü][bcdfghjklmnñpqrstvwxyz])((([pcbgf][rl])|([dt][r]))[aeiouáéíóúïü]))"
    R3b=r"(?P<regla3b>([aeiouáéíóúïü][bdnmlr][s])([bcdfghjklmnñpqrstvwxyz][aeiouáéíóúïü]))"
    R3c=r"(?P<regla3c>([aeiouáéíóúïü][s][t])([bcdfghjklmnñpqrstvwxyz][aeiouáéíóúïü]))"
    R4=r"(?P<regla4>([aeiouáéíóúïü](([bdnml][s])|([s][t])))([pcbgf][rl][aeiouáéíóúïü]))"
    R5a1=r"(?P<regla5a1>(([aeoáéó]h?)([iu])))"
    R5a2=r"(?P<regla5a2>(([iuü]h?)([aeoáéó])))"
    R5a3=r"(?P<regla5a3>(((([ií]h?)([uüú]))|(([uüú]h?)([ií])))))"
    R5b1=r"(?P<regla5b1>((([aeo]h?)([íú]))|(([íú]h?)([aeo]))))"
    R5b2=r"(?P<regla5b2>(([aá]h?)([aá]))|(([eé]h?)([eé]))|(([ií]h?)([ií]))|(([oó]h?)([oó]))|(([uú]h?)([uú])))"
    R5b3=r"(?P<regla5b3>(([aá]h?)([eo]))|(([eé]h?)([ao]))|(([oó]h?)([ae]))|((ah?)([eoéó]))|((eh?)([aáoó]))|((oh?)([aáeé])))"
    R6=r"(?P<regla6>(([iu])([aeoáéó][iuy])))"
    R="(?i)"+R1+"|"+R2a+"|"+R2b+"|"+R2c+"|"+R3a+"|"+R3b+"|"+R3c+"|"+R4+"|"+R6+"|"+R5a1+"|"+R5a2+"|"+R5a3+"|"+R5b1+"|"+R5b2+"|"+R5b3

    er=re.compile(R)
    lista = []
    m = er.search(cadena)
    cadenanueva=cadena
    while m!=None and len(cadenanueva)>1:
        
        if m.group("regla1"):
            
            cadenanueva=er.sub(r"\2-\3",cadenanueva,1)
            
        elif m.group("regla2a"):
            
            cadenanueva=er.sub(r"\6-\7",cadenanueva,1)

        elif m.group("regla2b"):
            
            cadenanueva=er.sub(r"\9-\10",cadenanueva,1)
        
        elif m.group("regla2c"):
            
            cadenanueva=er.sub(r"\12-\13",cadenanueva,1)

        elif m.group("regla3a"):
            
            cadenanueva=er.sub(r"\15-\16",cadenanueva,1)

        elif m.group("regla3b"):
           
            cadenanueva=er.sub(r"\21-\22",cadenanueva,1)

        elif m.group("regla3c"):
            
            cadenanueva=er.sub(r"\24-\25",cadenanueva,1)

        elif m.group("regla4") :
           
            cadenanueva=er.sub(r"\27-\31",cadenanueva,1)

        elif m.group("regla5a1") : #diptongos
            
            cadenanueva=er.sub(r"\38,\39",cadenanueva,1)
            

        elif m.group("regla5a2") :
            
            cadenanueva=er.sub(r"\42,\43",cadenanueva,1)
            

        elif m.group("regla5a3") :
            
            if (m.group(48)):
               
                cadenanueva=er.sub(r"\48,\49",cadenanueva,1)
            if (m.group(51)):
                
                cadenanueva=er.sub(r"\51,\52",cadenanueva,1)
            
        elif m.group("regla5b1") :
            if (m.group(56)):
               
                cadenanueva=er.sub(r"\56-\57",cadenanueva,1)
            if (m.group(59)):
                
                cadenanueva=er.sub(r"\59-\60",cadenanueva,1)

        elif m.group("regla5b2") :
            
            if (m.group(63)):
               
                cadenanueva=er.sub(r"\63-\64",cadenanueva,1)
            if (m.group(66)):
                
                cadenanueva=er.sub(r"\66-\67",cadenanueva,1)
            if (m.group(69)):
                
                cadenanueva=er.sub(r"\69-\70",cadenanueva,1)
            if (m.group(72)):
                
                cadenanueva=er.sub(r"\72-\73",cadenanueva,1)
            if (m.group(75)):
               
                cadenanueva=er.sub(r"\75-\76",cadenanueva,1)

        elif m.group("regla5b3") :
        
            if (m.group(79)):
                
                cadenanueva=er.sub(r"\79-\80",cadenanueva,1)
            if (m.group(82)):
                
                cadenanueva=er.sub(r"\82-\83",cadenanueva,1)
            if (m.group(85)):
                
                cadenanueva=er.sub(r"\85-\86",cadenanueva,1)
            if (m.group(88)):
               
                cadenanueva=er.sub(r"\88-\89",cadenanueva,1)
            if (m.group(91)):
                
                cadenanueva=er.sub(r"\91-\92",cadenanueva,1)
            if (m.group(94)):
                
                cadenanueva=er.sub(r"\94-\95",cadenanueva,1)

        elif m.group("regla6") :
                
            cadenanueva=er.sub(r"\34,\35",cadenanueva,1)
        
        else:
                break

        m=er.search(cadenanueva)

    
    return guiones_a_lista(cadenanueva)


def clasifica_entonacion(lsilabas):
    
    for i in range(len(lsilabas)):
        for j in range(len(lsilabas[i])):
            if lsilabas[i][j] in ['A','E','I','O','U','Y']:
                if i==len(lsilabas)-1:
                    return "Aguda"
                elif i==len(lsilabas)-2:
                    return "Llana"
                else:
                    return "Esdrújula"
        
def entonacion(lsilabas):
    listanueva=[]
    resultado=False
    listanueva,resultado=buscar_tilde(lsilabas)
    if resultado==True:
        return listanueva
    else:
        silaba,numero=busca_silaba(lsilabas)
        acentuada=vocal_tonica(silaba)
        listanueva[len(listanueva)-numero]=acentuada
        return listanueva
    

def buscar_tilde(ls):
    lsilabas=[]
    for i in range(len(ls)):
        lsilabas.append(ls[i])
    R1 = r"(?P<regla1>([a-z]*)(?P<mayus>[áéíóú])([a-z]*))"
    R = "(?i)" + R1
    er = re.compile(R)
    listanueva = []
    prueba = False

    for i in range(len(lsilabas)):
        if er.search(lsilabas[i]):
            for j in range(len(lsilabas[i])):
                if lsilabas[i][j]== 'á':
                    lsilabas[i] = lsilabas[i].replace('á', 'A', 1)
                elif lsilabas[i][j] == 'é':
                    lsilabas[i] = lsilabas[i].replace('é', 'E', 1)
                elif lsilabas[i][j] == 'í':
                    lsilabas[i] = lsilabas[i].replace('í', 'I', 1)
                elif lsilabas[i][j] == 'ó':
                    lsilabas[i] = lsilabas[i].replace('ó', 'O', 1)
                elif lsilabas[i][j] == 'ú':
                    lsilabas[i] = lsilabas[i].replace('ú', 'U', 1)

            listanueva.append(lsilabas[i])
            prueba = True
        else:
            listanueva.append(lsilabas[i])

    return listanueva, prueba
    
    
    
def busca_silaba(lsilabas):
    palabra=lista_a_palabra(lsilabas)

    if palabra=="y":
        return lsilabas[len(lsilabas)-1],1 
    elif palabra[-1] in ['a','e','i','o','u','s','n','y']:
        return lsilabas[len(lsilabas)-2],2
    else:
        return lsilabas[len(lsilabas)-1],1
    
    

def vocal_tonica(silaba):
    R1 = r"(?P<regla1>([bcdfghjklmnñpqrstvwxyz]*)(?P<a>[aeiou])([bcdfghjklmnñpqrstvwxyz]*))"
    R2 = r"(?P<regla2>([bcdfghjklmnñpqrstvwxyz]*)(?P<b>[aeo])(?P<c>[iu])([bcdfghjklmnñpqrstvwxyz]*))"
    R3 = r"(?P<regla3>([bcdfghjklmnñpqrstvwxyz]*)(?P<d>[iu])(?P<e>[aeo])([bcdfghjklmnñpqrstvwxyz]*))"
    R4 = r"(?P<regla4>([bcdfghjklmnñpqrstvwxyz]*)(?P<f>[iu])(?P<g>[iu])([bcdfghjklmnñpqrstvwxyz]*))"
    R5 = r"(?P<regla5>([bcdfghjklmnñpqrstvwxyz]*)(?P<h>[aeiou])(?P<i>[aeiou])(?P<j>[aeiou])([bcdfghjklmnñpqrstvwxyz]*))"
    R = "(?i)" + R5 + "|" + R2 + "|" + R3 + "|" + R4 + "|" +R1
    er = re.compile(R)
    m = er.search(silaba)

    if m:
        if m.group("regla1"):
            vocal = m.group("a")
            return silaba.replace(vocal, vocal.upper(), 1)
        elif m.group("regla2"):
            vocal = m.group("b")
            return silaba.replace(vocal, vocal.upper(), 1)
        elif m.group("regla3"):
            vocal = m.group("e")
            return silaba.replace(vocal, vocal.upper(), 1)
        elif m.group("regla4"):
            vocal = m.group("g")
            return silaba.replace(vocal, vocal.upper(), 1)
        elif m.group("regla5"):
            vocal = m.group("i")
            return silaba.replace(vocal, vocal.upper(), 1)
    if len(silaba)==1 and silaba=="y":
        silaba="Y"
    return silaba

def rimalizer_asonante(listamayus):
    palabra_entonada=lista_a_palabra(listamayus)
    inicio=False
    terminacion=""
    for i in range(len(palabra_entonada)):
        if palabra_entonada[i] in ['A','E','I','O','U','Y']:
            terminacion+=palabra_entonada[i]
            inicio=True
        if palabra_entonada[i] in ['a','e','i','o','u'] and inicio:
            terminacion+=palabra_entonada[i]
    return terminacion 
    
def rimalizer_consonante(listamayus):
    palabra_entonada=lista_a_palabra(listamayus)
    terminacion=""
    for i in range(len(palabra_entonada)):
        if palabra_entonada[i] in ['A','E','I','O','U','Y']:
            terminacion+=palabra_entonada[i:]
    return terminacion


def main():
    print("Bienvenido al silabeador de ALF")
    print("Opciones:")
    print("Inserta 1 para: silabear la palabra")
    print("Inserta 2 para: clasificar la palabra según su entonación")
    print("Inserta 3 para: obtener palabras que rimen con una dada")
    print("Inserta 666 para: salir")

    D = {}
    D_asonantes = {}
    D_consonantes = {}
    try:
        salida=open('salida.csv','r')

        for linea in salida:
            
            lista=linea.split(sep=':')
            patron_silabas = re.compile(r"\"*(?P<silabas>\[.*?\])\"*")
            patron_entonacion = re.compile(r"'entonacion': '(?P<entonacion>.*?)',")
            patron_term_aso = re.compile(r"'term_aso': '(?P<asonante>.*?)',")
            patron_term_conso = re.compile(r"'term_conso': '(?P<consonante>.*?)'}")

            match_silabas = patron_silabas.search(linea)
            match_entonacion = patron_entonacion.search(linea)
            match_term_aso = patron_term_aso.search(linea)
            match_term_conso = patron_term_conso.search(linea)

            silabas = match_silabas.group("silabas") if match_silabas else None
            listaentonacion = match_entonacion.group("entonacion") if match_entonacion else None
            term_asonante = match_term_aso.group("asonante") if match_term_aso else None
            term_consonante = match_term_conso.group("consonante") if match_term_conso else None
        
            D[lista[0]]={'silabas': silabas,'entonacion': listaentonacion,'term_aso':term_asonante,'term_conso':term_consonante}
            if term_asonante not in D_asonantes:
                D_asonantes[term_asonante]=lista[0]
            elif lista[0] not in D_asonantes.values():
                D_asonantes[term_asonante]=D_asonantes[term_asonante]+" , "+lista[0]
            if term_consonante not in D_consonantes:
                D_consonantes[term_consonante]=lista[0]
            elif lista[0] not in D_consonantes.values():
                D_consonantes[term_consonante]=D_consonantes[term_consonante]+" , "+lista[0] 
        
    except: 
        print("No hay diccionario que recuperar")
    while True:
        opcion=int(input("Introduce una opcion: "))
        if opcion == 1 or opcion == 2 or opcion == 3:
            cadena=input("Introduce una palabra bien escrita: ")
            asonante=rimalizer_asonante(cadena)
            consonante=rimalizer_consonante(cadena)
            if cadena not in D:
                cadena_analisis=y_vocal(cadena)       
                lista=silabear(cadena_analisis)
                listamayus=entonacion(lista)
                clasificacion=clasifica_entonacion(listamayus)
                asonante=rimalizer_asonante(listamayus)
                consonante=rimalizer_consonante(listamayus)
                D[cadena]={'silabas': lista,'entonacion': clasificacion,'term_aso':asonante,'term_conso':consonante}
                
            if asonante not in D_asonantes:
                D_asonantes[asonante]=cadena
            elif cadena not in D_asonantes.values():
                D_asonantes[asonante]=D_asonantes[asonante]+" , "+cadena
            if consonante not in D_consonantes:
                D_consonantes[consonante]=cadena
            elif cadena not in D_consonantes.values():
                D_consonantes[consonante]=D_consonantes[consonante]+" , "+cadena
            if opcion==1:
                print(D[cadena]["silabas"])
            if opcion==2:
                print(D[cadena]["entonacion"])
            if opcion==3:
                print("Rima asonante con: ",D_asonantes[asonante])
                print("Rima consonante con: ",D_consonantes[consonante])

        elif opcion==666:
            print("Guardando...")
            salida=open("salida.csv",'w')
            for k in D.keys():
                texto=k+":"+str(D[k])+"\n"
                salida.write(texto)
            salida.close()

            print("¡Adiós!")
            break
        else: 
            print("Opción incorrecta")
        
if __name__=="__main__":
    main()