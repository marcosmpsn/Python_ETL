def criar_carro(modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", motor="1.0", combustivel="Gasolina", marca="Fiat")
criar_carro("Corsa", 2010, "FGH-5678", "GM", "1.4", "Etanol")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

def criar_carro2(*,modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro2(modelo="Palio", ano=1999, placa="ABC-1234", motor="1.0", combustivel="Gasolina", marca="Fiat")
#criar_carro2("Corsa", 2010, "FGH-5678", "GM", "1.4", "Etanol")

def criar_carro3(modelo, ano, placa, /, *, marca, motor, combustivel):
        print(modelo, ano, placa, marca, motor, combustivel)

criar_carro3("Palio", 1999, "ABC-1234", motor="1.0", combustivel="Gasolina", marca="Fiat")
#criar_carro3("Corsa", 2010, "FGH-5678", "GM", "1.4", "Etanol")
#criar_carro3(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")