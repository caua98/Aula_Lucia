VCompra = float(input("Informe o valor da compra: "))
Vpagamento = float(input("Informe o valor pago: "))

if VCompra < Vpagamento:
    troco = Vpagamento - VCompra
    print("Troco Total: ", troco)
    resultado = troco//100
    print("Notas de 100: ", resultado)
    troco = troco - resultado * 100
    resultado = troco//50
    print("Notas de 50: ", resultado)
    troco = troco - resultado * 50
    resultado = troco//20
    print("Notas de 20: ", resultado)
    troco = troco - resultado * 20
    resultado = troco//10
    print("Notas de 10: ", resultado)
    troco = troco - resultado * 10
    resultado = troco//5
    print("Notas de 5: ", resultado)
    troco = troco - resultado * 5
    resultado = troco//1
    print("Notas de 1: ", resultado)

else:
    print("Não há troco a ser devolvido.")
    