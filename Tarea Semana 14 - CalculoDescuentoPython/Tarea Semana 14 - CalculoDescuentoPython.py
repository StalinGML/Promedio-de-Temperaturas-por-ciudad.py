# Trabajo semana 14: Stalin Mendieta-CalculoDescuentoPython
# Definición de la función calcular_descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calculamos el monto del descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con el monto total (utilizando el valor predeterminado del descuento)
monto_total_1 = 1705  # Monto total 1
descuento_1 = calcular_descuento(monto_total_1)
monto_final_1 = monto_total_1 - descuento_1 # Calculo del monto final a pagar 1

# Llamada a la función con monto total y porcentaje de descuento personalizado
monto_total_2 = 2402  # Monto total 2
porcentaje_descuento_2 = 20  # Se especifica un 20% de descuento
descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
monto_final_2 = monto_total_2 - descuento_2 # Calculo del monto final a pagar con el nuevo descuento

# Mostrar resultados
print("========== Resultados de la Compra ==========")
print(f"\nPrimera compra:")
print(f"Monto Total de la Compra: ${monto_total_1:.2f}")
print(f"Descuento Aplicado (10%): ${descuento_1:.2f}")
print(f"Monto Final a Pagar: ${monto_final_1:.2f}")

print("\nSegunda compra:")
print(f"Monto Total de la Compra: ${monto_total_2:.2f}")
print(f"Descuento Aplicado ({porcentaje_descuento_2}%): ${descuento_2:.2f}")
print(f"Monto Final a Pagar: ${monto_final_2:.2f}")
print("\n=============================================")