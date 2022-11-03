data = [{"name": 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': '₲. 24.600'}, {"name": 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': '₲. 3.450'}, {"name": 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': '₲. 6.700'}, {"name": 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': '₲. 5.100 × Kilogramo'}, {"name": 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': '₲. 9.900 × Kilogramo'}, {"name": 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': '₲. 11.200 × Kilogramo'}, {"name": 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': '₲. ₲. 45.900 × Kilogramo'}, {"name": 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': '₲. 7.600'}, {"name": 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': '₲. 4.350'}, {"name": 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': '₲. 5.400'}, {"name": 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': '₲. 5.950'}, {"name": 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': '₲. 6.500'}, {"name": 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': '₲. 1.200'}, {"name": 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': '₲. 7.700 × Kilogramo'}, {"name": 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': '₲. 4.400 × Kilogramo'}, {"name": 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': '₲. 6.300 × Kilogramo'}, {"name": 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': '₲. 11.200 × Kilogramo'}, {"name": 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': '₲. 4.550'}, {"name": 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': '₲. 12.700 × Kilogramo'}, {"name": 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': '₲. 10.880'}, {"name": 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': '₲. 16.900 × Kilogramo'}, {"name": 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': '₲. 36.650 × Kilogramo'}, {"name": 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': '₲. 4.400'}, {"name": 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': '₲. 8.950'}, {"name": 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': '₲. 3.600'}]

Precio_notvalid = ["28.950","4250","7.250","7.800","12.350","14.250","39.900","7500","4850","6100","5.950","6.550","6.300","1.850","10.400","5.750","3.900","12.150","11.400","13.750","17.950","45.350","4.800","11.700","6.950"]
Precio = []
print(len(Precio_notvalid))
for i in Precio_notvalid:
    i=  i.replace(".","")
    Precio.append(int(i))
    


add_praise_list = []
i = -1
for praise in data: 
    i = i +1
    praise["praise"] = Precio[i]

print(data)
print(Precio)
# def get_praise(data):
#     for praise in data:
#         add_praise_list = []
#         precios = praise.replace("× Kilogramo","").replace("₲. ","").replace(".","") #this will depend on the list
#         add_praise_list.append(int(precios))


# a = get_praise(Precio_notvalid) 
# print(a)
#last step, send it all to the, cumsum funtion


