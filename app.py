from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

data = [{"name": 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': '₲. ₲. 24.600'}, {"name": 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': '₲. 3.450'}, {"name": 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': '₲. 6.700'}, {"name": 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': '₲. 5.100 × Kilogramo'}, {"name": 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': '₲. 9.900 × Kilogramo'}, {"name": 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': '₲. 11.200 × Kilogramo'}, {"name": 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': '₲. ₲. 45.900 × Kilogramo'}, {"name": 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': '₲. 7.600'}, {"name": 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': '₲. 4.350'}, {"name": 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': '₲. 5.400'}, {"name": 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': '₲. 5.950'}, {"name": 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': '₲. 6.500'}, {"name": 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': '₲. 1.200'}, {"name": 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': '₲. 7.700 × Kilogramo'}, {"name": 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': '₲. 4.400 × Kilogramo'}, {"name": 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': '₲. 6.300 × Kilogramo'}, {"name": 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': '₲. 11.200 × Kilogramo'}, {"name": 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': '₲. 4.550'}, {"name": 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': '₲. 12.700 × Kilogramo'}, {"name": 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': '₲. 10.880'}, {"name": 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': '₲. 16.900 × Kilogramo'}, {"name": 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': '₲. 36.650 × Kilogramo'}, {"name": 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': '₲. 4.400'}, {"name": 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': '₲. 8.950'}, {"name": 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': '₲. 3.600'}]

@app.route("/")
def inicio():
    return render_template("index.html",datos=data)#,datos=data)

data = [{'name': 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': 34250}, {'name': 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': 4100}, {'name': 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': 7250}, {'name': 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': 7200}, {'name': 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': 12250}, {'name': 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': 17900}, {'name': 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': 45900}, {'name': 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': 8600}, {'name': 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': 4850}, {'name': 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': 5200}, {'name': 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': 6550}, {'name': 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': 6300}, {'name': 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': 1600}, {'name': 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': 9850}, {'name': 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': 5650}, {'name': 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': 5750}, {'name': 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': 9500}, {'name': 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': 5950}, {'name': 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': 11400}, {'name': 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': 13750}, {'name': 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': 18550}, {'name': 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': 42800}, {'name': 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': 4800}, {'name': 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': 7950}, {'name': 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': 5400}]

@app.route("/stock.html")
def stock():
    return render_template('stock.html',datos = data)

data = [{'name': 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': 28950}, {'name': 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': 4100}, {'name': 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': 7270}, {'name': 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': 6150}, {'name': 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': 12150}, {'name': 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': 14450}, {'name': 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': 32400}, {'name': 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': 8600}, {'name': 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': 5250}, {'name': 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': 6100}, {'name': 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': 6600}, {'name': 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': 6800}, {'name': 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': 1350}, {'name': 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': 9750}, {'name': 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': 5400}, {'name': 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': 5350}, {'name': 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': 9600}, {'name': 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': 5700}, {'name': 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': 15600}, {'name': 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': 14500}, {'name': 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': 16900}, {'name': 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': 31500}, {'name': 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': 5150}, {'name': 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': 12150}, {'name': 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': 4425}]
@app.route("/real.html")
def real():
    return render_template('real.html',datos=data)

data = [{'name': 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': 28950}, {'name': 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': 4250}, {'name': 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': 7250}, {'name': 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': 7800}, {'name': 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': 12350}, {'name': 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': 14250}, {'name': 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': 39900}, {'name': 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': 7500}, {'name': 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': 4850}, {'name': 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': 6100}, {'name': 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': 5950}, {'name': 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': 6550}, {'name': 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': 6300}, {'name': 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': 1850}, {'name': 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': 10400}, {'name': 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': 5750}, {'name': 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': 3900}, {'name': 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': 12150}, {'name': 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': 11400}, {'name': 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': 13750}, {'name': 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': 17950}, {'name': 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': 45350}, {'name': 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': 4800}, {'name': 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': 11700}, {'name': 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': 6950}]

@app.route("/superseis.html")
def superseis():
    return render_template('superseis.html',datos=data)


data = [{'name': 'ACEITE NATURA BOT 900 ML', 'image': 'ACEITE-NATURA.jpg', 'praise': 25200}, {'name': 'ARROZ PARBOLIZADO PRIMICIA 500  GR', 'image': 'ARROZ PARBOLIZADO PRIMICIA 500  GR5.png', 'praise': 4250}, {'name': 'AZUCAR BLANCA AZPA X 1 KG', 'image': 'Azucar-1k.jpg', 'praise': 5900}, {'name': 'BANANA KARAPE KG', 'image': 'Bananakarape.png', 'praise': 5000}, {'name': 'CEBOLLA KG', 'image': 'Cebolla-1k.png', 'praise': 9900}, {'name': 'COQUITO MAS X KG*', 'image': 'COQUITO.png', 'praise': 11900}, {'name': 'COSTILLA TIRA NORMAL NEULAND X KG', 'image': 'Costilla-carne.jpg', 'praise': 45900}, {'name': 'DETERGENTE ZITRON FRASCO 950 ML', 'image': 'Detergente.jpg', 'praise': 7750}, {'name': 'FIDEOS ANITA TALLARIN 400 GR', 'image': 'FIDEO.jpg', 'praise': 4750}, {'name': 'HARINA PRIMICIA INDEGA 1 KG', 'image': 'Harina.png', 'praise': 5850}, {'name': 'HUEVO NUTRIHUEVOS TIPO A x6 Unidades', 'image': 'NUTRIHUEVOS.jpg', 'praise': 6100}, {'name': 'LECHE LACTOLANDA LARGA VIDA ENTERA 1 LT', 'image': 'Leche.jpg', 'praise': 6650}, {'name': 'LECHUGA PIRATI x2 MAZO', 'image': 'LECHUGA.png', 'praise': 1500}, {'name': 'LOCOTE VERDE KG', 'image': 'LOCOTE.png', 'praise': 7800}, {'name': 'MANDIOCA KG', 'image': 'Mandioca.png', 'praise': 4700}, {'name': 'NARANJA KG', 'image': 'NARANJAS.png', 'praise': 3800}, {'name': 'PAPA BLANCA KG', 'image': 'Papa.png', 'praise': 10100}, {'name': 'PAPEL HIGIENICO HIGIENOL TEXTURADO 4 UNIDADES', 'image': 'PAPELHIGIENOL.png', 'praise': 5400}, {'name': 'POLLO SUPER FRESCO PECHUGON X KG', 'image': 'POLLO-entero.png', 'praise': 15600}, {'name': 'POROTO COLORADO INDEGA 500 GR', 'image': 'Poroto-500-indega.jpg', 'praise': 13.0}, {'name': 'PUCHERO PRIMERA X KG', 'image': 'Puchero.png', 'praise': 16400}, {'name': 'QUESO PARAGUAY TREBOL X KG', 'image': 'Queso-paraguay.png', 'praise': 35700}, {'name': 'SAL FINA INDEGA PRIMICIA 1 KG', 'image': 'SAL-1kPrimicia.png', 'praise': 4700}, {'name': 'TOMATE SANTA CRUZ KG', 'image': 'TOMATE SANTA CRUZ KG63.png', 'praise': 9100}, {'name': 'ZANAHORIA X KG', 'image': 'Zanahoria.png', 'praise': 3300}]

@app.route("/grutter.html")
def grutter():
    return render_template('grutter.html',datos=data)