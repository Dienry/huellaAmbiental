#Agregar que pongan Nombre, Apellido, DNI y mail
print """Los hábitos alimentarios tienen implicancias sociales, ambientales y económicas siendo un eje de trabajo importante para el Desarrollo Sustentable.
Según datos de la Organización de las Naciones Unidas para la Alimentación y la Agricultura (FAO) un tercio de los alimentos producidos en todo el mundo se pierde o desecha durante la etapa de producción y de consumo, representando el equivalente a 300 millones de toneladas. Esta cantidad que se desperdicia sería suficiente para alimentar a 900 millones de personas con déficit de alimentación en todo el mundo.
Por otro lado el sistema alimenticio mundial tiene profundas implicancias para el medio ambiente por la sobreexplotación de los recursos.
"""

Menu = """Elige una opcion: 
A) Consejos de Naciones Unidas y mis hábitos Alimentarios
B) Huella de Agua de mis hábitos Alimentarios
C) Huella Ecológica de mis hábitos Alimentarios"""


def opcionA():
    Resultado = []
    resultNum = 0
    respuesta = ["SI","S","NO","N"]
    print "La generación de desechos de alimentos comienza desde la compra de los mismos: "
    primera = str.upper(raw_input("1. ¿Al comprar frutas y verduras, selecciono lo que voy a llevar en función de su aspecto estético? (Si/No)"))
    while True:
        if primera[0]=='S':
            print ":("
            break
        elif primera[0]=='N':
            Resultado.append(":)")
            resultNum = resultNum + 1
            print ":)"
            break
        else:
            while not primera in respuesta: 
                print "Huy! parece que no pusiste si o no"
                primera = str.upper(raw_input("1. ¿Al comprar frutas y verduras, selecciono lo que voy a llevar en función de su aspecto estético? (Si/No)"))
    print "CONSEJO: Consuma fruta 'FEA'. Se desechan gran cantidad de frutas y verduras por su forma, tamaño o color. Comprando estas frutas en cualquier punto de venta estará consumiendo productos que de otra forma serían desperdiciados, generando impactos tanto en la etapa de producción de los mismos como también restando disponibilidad de alimentos para otras personas." 

    segunda = str.upper(raw_input("2. ¿Organizo mis compras armando una lista en base a lo que falta en mi hogar? (Si/No)"))
    while True:
        if segunda[0]=='S':
            Resultado.append(":)")
            resultNum = resultNum + 1
            print ":)"
            break
        elif segunda[0]=='N':
            print ":("
            break
        else:
            while not segunda in respuesta:
                print "Huy! parece que no pusiste si o no"
                segunda = str.upper(raw_input("2. ¿Organizo mis compras armando una lista en base a lo que falta en mi hogar? (Si/No)"))
    print "Consejo: Planifique sus comidas y utilice una lista. No compre más de lo que necesita. Mire su heladera y escriba una lista con los productos que necesite y que sabe que se van a consumir. Piense en comprar productos frescos en pequeñas cantidades más a menudo para poder disfrutarlos en su mejor momento."
    
    tercera = str.upper(raw_input("3. ¿Cuándo como en un restaurant queda comida sobrante en mi plato? (Si/No)"))
    while True:
        if tercera[0]=='S':
            print ":("
            break
        elif tercera[0]=='N':
            Resultado.append(":)")
            resultNum = resultNum + 1
            print ":)"
            break
        else:
            while not tercera in respuesta:
                print "Huy! parece que no pusiste si o no"
                tercera = str.upper(raw_input("3. ¿Cuándo como en un restaurant queda comida sobrante en mi plato? (Si/No)"))
    print "Consejo: Pida llevar los restos y colóquelos en el freezer o heladera de su casa para poder consumirlo en otra ocasión. Elija medias porciones en restaurantes y bares."
    
    cuarta = str.upper(raw_input("4. ¿Cuando compro productos lácteos, mantengo la cadena de frío durante el traslado? (Si/No)"))
    while True:
        if cuarta[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif cuarta[0]=='N':
            print ":("
            break
        else:
            while not cuarta in respuesta:
                print "Huy! parece que no pusiste si o no"
                cuarta = str.upper(raw_input("4. ¿Cuando compro productos lácteos, mantengo la cadena de frío durante el traslado? (Si/No)"))
    print "Consejo: Lleve una bolsa conservadora para llevar los alimentos congelados del supermercado a casa especialmente en días de calor."

    quinta = str.upper(raw_input("5. ¿Genero residuos de alimentos por no consumirlos antes de su fecha de vencimiento? (Si/No)"))
    while True:
        if quinta[0]=='S':
            print ":("
            break
        elif quinta[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not quinta in respuesta:
                print "Huy! parece que no pusiste si o no"
                quinta = str.upper(raw_input("5. ¿Genero residuos de alimentos por no consumirlos antes de su fecha de vencimiento? (Si/No)"))
    print "Consejo: No compre en exceso. Acuérdese de mirar las fechas de vencimiento para asegurarse que podrá usar los alimentos antes de que se estropeen."

    sexta = str.upper(raw_input("6. Cuando utilizo mi heladera, ¿controlo la temperatura para optimizar la conservación de los alimentos? (Si/No)"))
    while True:
        if sexta[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif sexta[0]=='N':
            print ":("
            break
        else:
            while not sexta in respuesta:
                print "Huy! parece que no pusiste si o no"
                sexta = str.upper(raw_input("6. Cuando utilizo mi heladera, ¿controlo la temperatura para optimizar la conservación de los alimentos? (Si/No)"))
    print "Consejo: Acuérdese de mantener su heladera a una temperatura por debajo de los 5ºC. Las investigaciones muestran que hasta un 70% de las heladeras se mantienen a temperaturas demasiado altas, lo que supone que los alimentos no duren todo lo que deberían. Por ejemplo, la leche se estropea mucho antes si la heladera no se encuentra a la temperatura adecuada. Todos los productos lácteos deben ser refrigerados en un plazo de dos horas tras ser comprados, de aquí la importancia de mantener la cadena de frío. Conserve todos los productos lácteos en la heladera, a menos que haya planeado congelarlos. Mueva los alimentos de su heladera, de modo que tenga lo que tiene que ser consumido antes adelante y de esa forma, no se olvide de ello."

    septima = str.upper(raw_input("7. Cuando cargo el freezer ¿Realizo un análisis previo de los alimentos que voy a almacenar? (Si/No)"))
    while True:
        if septima[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif septima[0]=='N':
            print ":("
            break
        else:
            while not septima in respuesta:
                print "Huy! parece que no pusiste si o no"
                septima = str.upper(raw_input("7. Cuando cargo el freezer ¿Realizo un análisis previo de los alimentos que voy a almacenar? (Si/No)"))
    print "Consejo: Hay alimentos, como ser ciertas variedades de pan, que se conservan mejor en un lugar fresco y oscuro como en un armario o un cajón del pan. Asimismo, hay alimentos que no admiten ser descongelados y re-congelados (cuando compre alimentos congelados, no olvide acortar todo lo posible el período entre la compra y carga en el freezer), en cuyo caso si se prevé consumirlo en el corto plazo puede ser mejor opción refrigerarlo en heladera. Cuando congele alimentos, etiquételos y acomódelos de manera tal de tenerlos disponibles según su frecuencia de consumo y/o plazos de conservación en estado congelado."
    
    octava = str.upper(raw_input("8. ¿Guardo los cereales con cierre hermético? (Si/No)"))
    while True:
        if octava[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif octava[0]=='N':
            print ":("
            break
        else:
            while not octava in respuesta:
                print "Huy! parece que no pusiste si o no"
                octava = str.upper(raw_input("8. ¿Guardo los cereales con cierre hermético? (Si/No)"))
    print "Consejo: Guardando los cereales en recipientes herméticos se mantienen crocantes, extendiendo su vida útil y evitando la generación de desechos."

    print "Al preparar alimentos"

    novena = str.upper(raw_input("9. Luego de las comidas, y particularmente cuando organizo eventos festivos, ¿Sobran alimentos? (Si/No)"))
    while True:
        if novena[0]=='S':
            print ":("
            break
        elif novena[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not novena in respuesta:
                print "Huy! parece que no pusiste si o no"
                novena = str.upper(raw_input("9. Luego de las comidas, y particularmente cuando organizo eventos festivos, ¿Sobran alimentos? (Si/No)"))
    print "Consejo: Planifique las comidas en función de la cantidad de comensales y en ocasiones que deba calcular y prepararla en exceso, trate de hacerlo con aquellos platos o preparaciones cuya conservación minimice la necesidad de  desecharla y permita una  fácil conservación para su consumo futuro."

    print "Restos de comida"
    decima = str.upper(raw_input("10. ¿Guardo los restos de comidas? (Si/No)"))
    while True:
        if decima[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif decima[0]=='N':
            print ":("
            break
        else:
            while not decima in respuesta:
                print "Huy! parece que no pusiste si o no"
                decima = str.upper(raw_input("10. ¿Guardo los restos de comidas? (Si/No)"))
    print "Consejo: Aproveche al máximo sus alimentos enfriando los restos lo más rápido posible después de cocinarlos y almacenándolos en la heladera. Consúmalos en los días subsiguientes, de ser posible, congélelos para ser aprovechados en otra ocasión. Buscar modos de aprovechar los restos de comidas anteriores es una manera de reducir los desechos alimenticios."

    decimoprimera = str.upper(raw_input("11. ¿Desecha las frutas golpeadas o marcadas? (Si/No)"))
    while True:
        if decimoprimera[0]=='S':
            print ":("
            break
        elif decimoprimera[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not decimoprimera in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimoprimera = str.upper(raw_input("11. ¿Desecha las frutas golpeadas o marcadas? (Si/No)"))
    print "Consejo: Antes de desecharlas, realice preparaciones cuya presentación no dependan del aspecto de la fruta como por ejemplo ensaladas de frutas, licuados o compotas."

    decimosegunda = str.upper(raw_input("12. ¿Desecho cereales húmedos? (Si/No)"))
    while True:
        if decimosegunda[0]=='S':
            print ":("
            break
        elif decimosegunda[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not decimosegunda in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimosegunda = str.upper(raw_input("12. ¿Desecho cereales húmedos? (Si/No)"))
    print "Consejo: Puede utilizarlos para hacer tortas u otras preparaciones pasteleras."

    decimotercera = str.upper(raw_input("13. ¿Desecho las frutas maduras? (Si/No)"))
    while True:
        if decimotercera[0]=='S':
            print ":("
            break
        elif decimotercera[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not decimotercera in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimotercera = str.upper(raw_input("13. ¿Desecho las frutas maduras? (Si/No)"))
    print "Consejo: Puede cortarlas y congelarlas para hacer licuados y helados."

    decimocuarta = str.upper(raw_input("14. ¿Desecho el pan viejo? (Si/No)"))
    while True:
        if decimocuarta[0]=='S':
            print ":("
            break
        elif decimocuarta[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not decimocuarta in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimocuarta = str.upper(raw_input("14. ¿Desecho el pan viejo? (Si/No)"))
    print "Consejo: Puede utilizarlo para budines, rebozadores y otros complementos útiles en la elaboración de comidas."

    decimoquinta = str.upper(raw_input("15. ¿Desecha los tomates maduros? (Si/No)"))
    while True:
        if decimoquinta[0]=='S':
            print ":("
            break
        elif decimoquinta[0]=='N':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        else:
            while not decimoquinta in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimoquinta = str.upper(raw_input("15. ¿Desecha los tomates maduros? (Si/No)"))
    print "Consejo: Puede utilizarlos para hacer salsas y sopas."

    decimosexta = str.upper(raw_input("16. ¿Utiliza utensilios especiales para pelar tubérculos y frutas? (Si/No)"))
    while True:
        if decimosexta[0]=='S':
            print ":)"
            Resultado.append(":)")
            resultNum = resultNum + 1
            break
        elif decimosexta[0]=='N':
            print ":("
            break
        else:
            while not decimosexta in respuesta:
                print "Huy! parece que no pusiste si o no"
                decimosexta = str.upper(raw_input("16. ¿Utiliza utensilios especiales para pelar tubérculos y frutas? (Si/No)"))
    print "Consejo: Evite la utilización de cuchillos ya que generan mucho desperdicio de alimento arrastrado en la cáscara separada."

    porcentaje = (resultNum*100)/16
    print "Su resultado es: ", ' '.join(Resultado)
    print "Mis hábitos alimentarios representan un ", porcentaje, "% de los hábitos recomendados por UNEP en su programa: Come, Piensa Ahorra. ¡Ahora a trabajar en mejorar mis hábitos alimentarios para evitar el hambre y proteger el ambiente!"
    if porcentaje >= 70:
        print "Sus habitos son excelentes."
    elif porcentaje >= 30:
        print "Tiene buenos habitos, pero son mejorables."
    else:
        print "Debe mejorar sus habitos alimenticios."
    
def opcionB():
    resp1 = 0
    resp2 = 0
    resp3 = 0
    resp4 = 0
    resp5 = 0
    resp6 = 0 
    resp7 = 0
    resp8 = 0
    resp9 = 0
    resp10 = 0
    resp11 = 0
    resp12 = 0 
    resp13 = 0
    resp14 = 0
    resp15 = 0 
    print "El volumen y patrón de consumo y la huella de agua de cada uno de los productos que se consumen son los factores principales que determinan la Huella de Agua de una persona. La Huella de agua de una persona considera dos componentes, una directa y una indirecta. A modo de ejemplo, al consumir carne, hablamos de huella de agua directa cuando nos referimos al volumen de agua consumido o contaminado cuando se prepara y cocina la carne. La huella de agua indirecta del consumidor de carne depende de las huellas directas de agua del intermediario que prepara la carne para ponerla en el mercado, del distribuidor, del criadero del ganado y de los cultivos que se utilizaron para alimentar al animal."
    primera = input("1. ¿Cuántas personas habitan la vivienda de forma normal y habitual?")
    resp1 = resp1 + primera
    segunda = input("2. ¿Cuántas veces a la semana lava los platos a mano? Se consideran 4 comidas diarias.")
    resp2 = resp2 + segunda
    tercera = input("3. ¿Cuántas veces a la semana utiliza el lavavajillas?")
    resp3 = resp3 + tercera
    cuarta = input("4. ¿Cuántos kg de carne consume semanalmente?")
    resp4 = resp4 + cuarta
    quinta = input("5. Si consume cereales (trigo, arroz, maíz, avena, harinas, pan), considerando 4 comidas diarias ¿En cuántas comidas los incluye en un día?")
    resp5 = resp5 + quinta
    sexta = input("6. ¿Cuantos litros de leche consume semanalmente?")
    resp6 = resp6 + sexta
    septima = input("7. ¿Cuántos huevos consume semanalmente?")
    resp7 = resp7 + septima
    octava = input("8. Si consume aceite (aceite de girasol, maíz, soja, oliva) considerando 4 comidas diarias ¿En cuántas comidas los incluye en un día?")
    resp8 = resp8 + octava
    novena = input("9. Si consume azúcar considerando 4 comidas diarias ¿En cuántas comidas los incluye en un día?")
    resp9 = resp9 + novena
    decima = input("10. Si consume edulcorante considerando 4 comidas diarias ¿En cuántas comidas los incluye en un día?")
    resp10 = resp10 + decima
    decimoprimera = input("11. ¿Cuántos kg de verduras consume semanalmente?")
    resp11 = resp11 + decimoprimera
    decimosegunda = input("12. ¿Cuántos kg de fruta consume semanalmente?")
    resp12 = resp12 + decimosegunda
    decimotercera = input("13. ¿Cuántas tazas de té Consume semanalmente?")
    resp13 = resp13 + decimotercera
    decimocuarta = input("14. ¿Cuántas tazas de café consume semanalmente?")
    resp14 = resp14 + decimocuarta
    decimoquinta = input("15. ¿Cuántas litros de vino consume semanalmente?")
    resp15 = resp15 + decimoquinta
    huellaDirecta = ((resp2*400/resp1)+(resp3*136/resp1))
    huellaIndirecta = ((resp4*297524 + resp4*16668 + resp4*4368) + (resp5*5210.42+ resp5*142.5 + resp5*316.875) + (resp6*2232.816 + resp6*98.688 + resp6*49.344) + (resp7*324.672 + resp7*11.136 + resp7*14.976) + (resp8*1452.08 + resp8*24.375 + resp8*15.42) + (resp9*588.125 + resp9*179.58 + resp9*49.16) + (resp10*1414.58 + resp10*136.25) + (resp11*14452 + resp11*1504 + resp11*1004) + (resp12*22624 + resp12*5916 + resp12*1656) + (resp13*76.37 + resp13*12.17 + resp13*2.84) + (resp14*323.9 + resp14*4.984 + resp11*0.952) + (resp15*973.072 + resp15*1399.788 + resp12*227.316))
    huellaAgua = huellaDirecta + huellaIndirecta
    print "La huella de agua directa es de ", huellaDirecta, "litros agua/mes."
    print "La huella de agua indirecta es de ", huellaIndirecta, "litros agua/mes"
    print "La huella de agua total es de ", huellaAgua, "litros agua/mes"
    
def opcionC():
    Huella_Cereales_ALTO = 0.14676 * 0.9516
    Huella_Cereales_MEDIO = 0.1223 * 0.9516
    Huella_Cereales_BAJO = 0.09784 * 0.9516
    Huella_Raices_ALTO = 0.0564 * 0.115
    Huella_Raices_MEDIO = 0.047 * 0.115
    Huella_Raices_BAJO = 0.0376 * 0.115
    Huella_Azucar_ALTO = 0.04968 * 0.04396
    Huella_Azucar_MEDIO = 0.0414 * 0.04396
    Huella_Azucar_BAJO = 0.03312 * 0.04396
    Huella_Legumbres_ALTO = 0.0006 * 2.3145
    Huella_Legumbres_MEDIO = 0.0005 * 2.3145
    Huella_Legumbres_BAJO = 0.0004 * 2.3145
    Huella_Nueces_ALTO = 0.00048 * 1.086
    Huella_Nueces_MEDIO = 0.0004 * 1.086
    Huella_Nueces_BAJO = 0.00032 * 1.086
    Huella_AceiteVegetal_ALTO = 0.01776 * 4.288
    Huella_AceiteVegetal_MEDIO = 0.0148 * 4.288
    Huella_AceiteVegetal_BAJO = 0.01184 * 4.288
    Huella_Fruta_ALTO = 0.08352 * 0.16547
    Huella_Fruta_MEDIO = 0.0696 * 0.16547
    Huella_Fruta_BAJO = 0.05568 * 0.16547
    Huella_Infusiones_ALTO = 0.0096 * 1.867
    Huella_Infusiones_MEDIO = 0.008 * 1.867
    Huella_Infusiones_BAJO = 0.0064 * 1.867
    Huella_Especias_ALTO = 0.0024 * 2.4344
    Huella_Especias_MEDIO = 0.002 * 2.4344
    Huella_Especias_BAJO = 0.0016 * 2.4344
    Huella_Vino_ALTO = 0.02892 * 0.3198
    Huella_Vino_MEDIO = 0.0241 * 0.3198
    Huella_Vino_BAJO = 0.01928 * 0.3198
    Huella_Carne_ALTO = 0.06588 * 0.02208
    Huella_Carne_MEDIO = 0.0549 * 0.02208
    Huella_Carne_BAJO = 0.04392 * 0.02208
    Huella_Pescado_ALTO = 0.00684 * 15.98
    Huella_Pescado_MEDIO = 0.0057 * 15.98
    Huella_Pescado_BAJO = 0.00456 * 15.98

    Cereales = 0
    Raices = 0
    Azucar = 0
    Legumbres = 0
    Nueces = 0
    AceiteVegetal = 0
    Fruta = 0
    Infusiones = 0
    Especias = 0
    Vino = 0
    Carne = 0
    Pescado = 0
    respuesta = ["alto","medio","bajo"]
    print "La Huella Ecológica es el área necesaria para producir los productos consumidos y absorber los residuos generados. Considerando nuestros hábitos alimenticios refleja el área necesaria para: producir los vegetales, producir el forraje necesario para el alimento del ganado, producir el pescado que se consume."
    cereales = str.lower(raw_input("¿Su consumo de cereales es Alto, Medio o Bajo? "))
    while True:
        if cereales=='alto':
            Cereales = Huella_Cereales_ALTO
            break
        elif cereales=='medio':
            Cereales = Huella_Cereales_MEDIO
            break
        elif cereales=='bajo':
            Cereales = Huella_Cereales_BAJO
            break
        else:
            while not cereales in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                cereales = str.lower(raw_input("¿Su consumo de cereales es Alto, Medio o Bajo? "))
    raices = str.lower(raw_input("¿Su consumo de raíces es Alto, Medio o Bajo? "))
    while True:
        if raices=='alto':
            Raices = Huella_Raices_ALTO
            break
        elif raices=='medio':
            Raices = Huella_Raices_MEDIO
            break
        elif raices=='bajo':
            Raices = Huella_Raices_BAJO
            break
        else:
            while not raices in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                raices = str.lower(raw_input("¿Su consumo de raíces es Alto, Medio o Bajo? "))
    azucar = str.lower(raw_input("¿Su consumo de azúcares es Alto, Medio o Bajo? "))
    while True:
        if azucar=='alto':
            Azucar = Huella_Azucar_ALTO
            break
        elif azucar=='medio':
            Azucar = Huella_Azucar_MEDIO
            break
        elif azucar=='bajo':
            Azucar = Huella_Azucar_BAJO
            break
        else:
            while not azucar in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                azucar = str.lower(raw_input("¿Su consumo de azúcares es Alto, Medio o Bajo? "))
    legumbres = str.lower(raw_input("¿Su consumo de legumbres es Alto, Medio o Bajo? "))
    while True:
        if legumbres=='alto':
            Legumbres = Huella_Legumbres_ALTO
            break
        elif legumbres=='medio':
            Legumbres = Huella_Legumbres_MEDIO
            break
        elif legumbres=='bajo':
            Legumbres = Huella_Legumbres_BAJO
            break
        else:
            while not legumbres in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                Legumbres = str.lower(raw_input("¿Su consumo de legumbres es Alto, Medio o Bajo? "))
    nueces = str.lower(raw_input("¿Su consumo de nueces es Alto, Medio o Bajo? "))
    while True:
        if nueces=='alto':
            Nueces = Huella_Nueces_ALTO
            break
        elif nueces=='medio':
            Nueces = Huella_Nueces_MEDIO
            break
        elif nueces=='bajo':
            Nueces = Huella_Nueces_BAJO
            break
        else:
            while not nueces in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                nueces = str.lower(raw_input("¿Su consumo de nueces es Alto, Medio o Bajo? "))
    vegetales = str.lower(raw_input("¿Su consumo de vegetales es Alto, Medio o Bajo? "))
    while True:
        if vegetales=='alto':
            AceiteVegetal = Huella_AceiteVegetal_ALTO
            break
        elif vegetales=='medio':
            AceiteVegetal = Huella_AceiteVegetal_MEDIO
            break
        elif vegetales=='bajo':
            AceiteVegetal = Huella_AceiteVegetal_BAJO
            break
        else:
            while not vegetales in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                vegetales = str.lower(raw_input("¿Su consumo de vegetales es Alto, Medio o Bajo? "))
    frutas = str.lower(raw_input("¿Su consumo de frutas es Alto, Medio o Bajo? "))
    while True:
        if frutas=='alto':
            Fruta = Huella_Fruta_ALTO
            break
        elif frutas=='medio':
            Fruta = Huella_Fruta_MEDIO
            break
        elif frutas=='bajo':
            Fruta = Huella_Fruta_BAJO
            break
        else:
            while not frutas in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                frutas = str.lower(raw_input("¿Su consumo de frutas es Alto, Medio o Bajo? "))
    infusiones = str.lower(raw_input("¿Su consumo de infusiones es Alto, Medio o Bajo? "))
    while True:
        if infusiones=='alto':
            Infusiones = Huella_Infusiones_ALTO
            break
        elif infusiones=='medio':
            Infusiones = Huella_Infusiones_MEDIO
            break
        elif infusiones=='bajo':
            Infusiones = Huella_Infusiones_BAJO
            break
        else:
            while not infusiones in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                infusiones = str.lower(raw_input("¿Su consumo de infusiones es Alto, Medio o Bajo? "))
    especias = str.lower(raw_input("¿Su consumo de especias es Alto, Medio o Bajo? "))
    while True:
        if especias=='alto':
            Especias = Huella_Especias_ALTO
            break
        elif especias=='medio':
            Especias = Huella_Especias_MEDIO
            break
        elif especias=='bajo':
            Especias = Huella_Especias_BAJO
            break
        else:
            while not especias in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                especias = str.lower(raw_input("¿Su consumo de especias es Alto, Medio o Bajo? "))
    vino = str.lower(raw_input("¿Su consumo de vino es Alto, Medio o Bajo? "))
    while True:
        if vino=='alto':
            Vino = Huella_Vino_ALTO
            break
        elif vino=='medio':
            Vino = Huella_Vino_MEDIO
            break
        elif vino=='bajo':
            Vino = Huella_Vino_BAJO
            break
        else:
            while not vino in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                vino = str.lower(raw_input("¿Su consumo de vino es Alto, Medio o Bajo? "))
    carne = str.lower(raw_input("¿Su consumo de carne es Alto, Medio o Bajo? "))
    while True:
        if carne=='alto':
            Carne = Huella_Carne_ALTO
            break
        elif carne=='medio':
            Carne = Huella_Carne_MEDIO
            break
        elif carne=='bajo':
            Carne = Huella_Carne_BAJO
            break
        else:
            while not carne in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                carne = str.lower(raw_input("¿Su consumo de carne es Alto, Medio o Bajo? "))

    pescado = str.lower(raw_input("¿Su consumo de pescado es Alto, Medio o Bajo? "))
    while True:
        if pescado=='alto':
            Pescado = Huella_Pescado_ALTO
            break
        elif pescado=='medio':
            Pescado = Huella_Pescado_MEDIO
            break
        elif pescado=='bajo':
            Pescado = Huella_Pescado_BAJO
            break
        else:
            while not pescado in respuesta:
                print "Huy! parece que no pusiste Alto, Medio o Bajo"
                pescado = str.lower(raw_input("¿Su consumo de pescado es Alto, Medio o Bajo? "))

    HuellaEcologica = Cereales + Raices + Azucar + Legumbres + Nueces + AceiteVegetal + Fruta + Infusiones + Especias + Vino + Carne + Pescado
    print "Su huella ecologica es de ", HuellaEcologica, " hectareas/año"

print Menu
Funcion = str.upper(raw_input("Elija la funcion que quiere ejecutar: "))
if Funcion == "A":
    print opcionA()
elif Funcion == "B":
    print opcionB()
elif Funcion == "C":
    print opcionC()


