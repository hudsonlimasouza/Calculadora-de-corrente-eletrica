import tkinter as tk
from tkinter import messagebox

def calcular_corrente():
    try:
        # Obtém os valores inseridos pelo usuário
        tensao = float(entry_tensao.get())
        resistencia = float(entry_resistencia.get())
        
        # Verifica se a resistência é zero
        if resistencia == 0:
            messagebox.showerror("Erro", "A resistência não pode ser zero.")
            return
        
        # Calcula a corrente elétrica
        corrente = tensao / resistencia
        label_resultado.config(text=f"Corrente: {corrente:.2f} A")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calcular Corrente Elétrica,")

# Layout da interface
tk.Label(janela, text="Digite a Tensão (V):").grid(row=0, column=0, padx=10, pady=20)
entry_tensao = tk.Entry(janela)
entry_tensao.grid(row=0, column=5, padx=10, pady=5)

tk.Label(janela, text="Digite a Resistência (Ω):").grid(row=1, column=0, padx=10, pady=15)
entry_resistencia = tk.Entry(janela)
entry_resistencia.grid(row=1, column=5, padx=10, pady=3)

btn_calcular = tk.Button(janela, text="Calcular", command=calcular_corrente)
btn_calcular.grid(row=2, column=3, columnspan=2, pady=10)

label_resultado = tk.Label(janela, text="Corrente: .....")
label_resultado.grid(row=3, column=0, columnspan=2, pady=60)


# Executa o loop principal da interface
janela.mainloop()
