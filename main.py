import tkinter as tk
from tkinter import messagebox

def calcular_tempo_para_stamina_atualizar(stamina_atual, stamina_desejada, opcao):
    horas_necessarias = 0
    minutos_necessarios = 0

    while stamina_atual < stamina_desejada:
        if stamina_atual >= 39 * 60:
            if opcao == "Offline":
                ganho_por_minuto = 6
            elif opcao == "Trainer":
                ganho_por_minuto = 5
            elif opcao == "PZ":
                ganho_por_minuto = 4
        else:
            if opcao == "Offline":
                ganho_por_minuto = 3
            elif opcao == "Trainer":
                ganho_por_minuto = 5
            elif opcao == "PZ":
                ganho_por_minuto = 2

        minutos_necessarios += ganho_por_minuto
        stamina_atual += 1

    horas_necessarias = minutos_necessarios // 60
    minutos_restantes = minutos_necessarios % 60

    return horas_necessarias, minutos_restantes


def calcular_tempo():
    try:
        stamina_atual = int(entry_stamina_atual_hh.get()) * 60 + int(entry_stamina_atual_mm.get())
        stamina_desejada = int(entry_stamina_desejada_hh.get()) * 60 + int(entry_stamina_desejada_mm.get())

        if stamina_desejada <= stamina_atual:
            raise ValueError("O tempo de stamina desejada deve ser maior que o tempo de stamina atual.")

        opcao = var_opcao.get()

        horas, minutos = calcular_tempo_para_stamina_atualizar(stamina_atual, stamina_desejada, opcao)

        resultado_label.config(text=f"Tempo necessário para alcançar a stamina desejada: {horas} horas e {minutos} minutos.")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Criar janela
window = tk.Tk()
window.title("Calculadora de Stamina")
window.minsize(300, 1)

# Labels e Entradas
label_stamina_atual = tk.Label(window, text="Stamina Atual (hh:mm):")
label_stamina_atual.grid(row=0, column=0)
entry_stamina_atual_hh = tk.Entry(window, width=2)
entry_stamina_atual_hh.grid(row=0, column=1)
entry_stamina_atual_mm = tk.Entry(window, width=2)
entry_stamina_atual_mm.grid(row=0, column=2)

label_stamina_desejada = tk.Label(window, text="Stamina Desejada (hh:mm):")
label_stamina_desejada.grid(row=1, column=0)
entry_stamina_desejada_hh = tk.Entry(window, width=2)
entry_stamina_desejada_hh.grid(row=1, column=1)
entry_stamina_desejada_mm = tk.Entry(window, width=2)
entry_stamina_desejada_mm.grid(row=1, column=2)

# Checkbox para opções
var_opcao = tk.StringVar()
var_opcao.set("Offline")

opcao_offline = tk.Radiobutton(window, text="Offline", variable=var_opcao, value="Offline")
opcao_offline.grid(row=2, column=0)
opcao_trainer = tk.Radiobutton(window, text="Trainer", variable=var_opcao, value="Trainer")
opcao_trainer.grid(row=2, column=1)
opcao_pz = tk.Radiobutton(window, text="PZ", variable=var_opcao, value="PZ")
opcao_pz.grid(row=2, column=2)

# Botão para calcular
calcular_button = tk.Button(window, text="Calcular", command=calcular_tempo)
calcular_button.grid(row=3, columnspan=3)

# Label para mostrar o resultado
resultado_label = tk.Label(window, text="")
resultado_label.grid(row=4, columnspan=3)

# Iniciar loop da aplicação
window.mainloop()
