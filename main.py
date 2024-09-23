import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random

class Player:
    def __init__(self, name, nationality, age, position, money_level):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.position = position
        self.money = {'Baixo': random.randint(0, 1000), 'Médio': random.randint(3000, 5000), 'Alto': random.randint(8000, 10000)}[money_level]
        self.strength = random.randint(5, 15)
        self.popularity = random.randint(0, 100)
        self.happiness = 100
        self.attributes = {'Força': 50, 'Chute': 50, 'Cabeceio': 50}
        self.relationships = {'Treinador': 50, 'Amigos': 50, 'Família': 50}
        self.statistics = {'Partidas': 0, 'Gols': 0, 'Assistências': 0}
        self.team = self.assign_initial_team()
        self.year = 2021
        if self.age < 20:
            self.strength += random.randint(0, 60)
        elif self.age > 20:
            self.strength += random.randint(20, 65)

    def assign_initial_team(self):
        # Simplifica a atribuição do time inicial com base na nacionalidade
        teams = {
            'Brasil': ['Flamengo', 'Palmeiras', 'São Paulo'],
            'Argentina': ['River Plate', 'Boca Juniors'],
            'Espanha': ['Real Madrid', 'Barcelona'],
            'Inglaterra': ['Manchester United', 'Liverpool']
        }
        if self.nationality in teams:
            return random.choice(teams[self.nationality])
        else:
            return 'Clube Genérico'

    def train(self, focus):
        # Melhora os atributos com base no foco do treino
        if focus in self.attributes:
            self.attributes[focus] += random.randint(1, 5)
            self.strength += random.randint(1, 3)
            if self.attributes[focus] > 100:
                self.attributes[focus] = 100
            if self.strength > 100:
                self.strength = 100

    def advance_year(self):
        self.age += 1
        self.year += 1
        # Diminui a força com a idade
        if self.age > 30:
            self.strength -= random.randint(1, 3)
        # Simula as estatísticas da temporada com base na força e posição do jogador
        partidas = random.randint(20, 40)
        gols = 0
        assistencias = 0

        if self.position == 'Goleiro':
            gols = random.randint(0, 2) if self.strength > 50 else random.randint(0, 1)
            assistencias = random.randint(0, 5) if self.strength > 50 else random.randint(0, 3)
        elif self.position == 'Defensor':
            gols = random.randint(0, 5) if self.strength > 50 else random.randint(0, 3)
            assistencias = random.randint(0, 10) if self.strength > 50 else random.randint(0, 5)
        elif self.position == 'Meio-campista':
            gols = random.randint(0, 10) if self.strength > 50 else random.randint(0, 5)
            assistencias = random.randint(0, 15) if self.strength > 50 else random.randint(0, 10)
        elif self.position == 'Atacante':
            gols = random.randint(0, 30) if self.strength > 50 else random.randint(0, 20)
            assistencias = random.randint(0, 10) if self.strength > 50 else random.randint(0, 5)

        self.statistics['Partidas'] += partidas
        self.statistics['Gols'] += gols
        self.statistics['Assistências'] += assistencias
        # Atualiza a popularidade
        self.popularity += random.randint(-5, 5)
        self.popularity = max(0, min(100, self.popularity))
        # Atualiza a felicidade
        self.happiness += random.randint(-5, 5)
        self.happiness = max(0, min(100, self.happiness))

class CareerSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Carreira de Futebol")
        self.geometry("500x400")
        self.player = None
        self.create_widgets()

    def create_widgets(self):
        # Campos de entrada para informações do jogador
        tk.Label(self, text="Nome do Jogador:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Nacionalidade:").pack()
        self.nationality_var = tk.StringVar()
        self.nationality_entry = tk.ttk.Combobox(self, textvariable=self.nationality_var)
        self.nationality_entry['values'] = ('Brasil', 'Argentina', 'Espanha', 'Inglaterra')
        self.nationality_entry.pack()

        tk.Label(self, text="Idade Inicial:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Posição Inicial:").pack()
        self.position_var = tk.StringVar()
        self.position_entry = tk.ttk.Combobox(self, textvariable=self.position_var)
        self.position_entry['values'] = ('Goleiro', 'Defensor', 'Meio-campista', 'Atacante')
        self.position_entry.pack()

        tk.Label(self, text="Quantidade de Dinheiro Inicial:").pack()
        self.money_var = tk.StringVar(value='Baixo')
        tk.Radiobutton(self, text='Baixo', variable=self.money_var, value='Baixo').pack()
        tk.Radiobutton(self, text='Médio', variable=self.money_var, value='Médio').pack()
        tk.Radiobutton(self, text='Alto', variable=self.money_var, value='Alto').pack()

        tk.Button(self, text="Iniciar Carreira", command=self.start_career).pack()

    def start_career(self):
        name = self.name_entry.get()
        nationality = self.nationality_entry.get()
        try:
            age = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Idade deve ser um número.")
            return
        position = self.position_entry.get()
        money_level = self.money_var.get()
        self.player = Player(name, nationality, age, position, money_level)
        messagebox.showinfo("Carreira Iniciada", f"Bem-vindo, {self.player.name}! Você começará no time {self.player.team}.")
        self.show_main_menu()

    def show_main_menu(self):
        # Limpa a janela
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text=f"Ano: {self.player.year}").pack()
        tk.Label(self, text=f"Jogador: {self.player.name}, {self.player.age} anos, Força: {self.player.strength}").pack()
        tk.Label(self, text=f"Time Atual: {self.player.team}").pack()
        tk.Button(self, text="Treinar", command=self.train_player).pack()
        tk.Button(self, text="Avançar Ano", command=self.advance_year).pack()
        tk.Button(self, text="Ver Estatísticas", command=self.show_statistics).pack()
        tk.Button(self, text="Ver Relações", command=self.show_relationships).pack()
        tk.Button(self, text="Sair", command=self.quit).pack()

    def train_player(self):
        # Opções simples de treino
        training_window = tk.Toplevel(self)
        training_window.title("Treinar Jogador")
        tk.Label(training_window, text="Escolha o foco do treino:").pack()
        for attribute in self.player.attributes.keys():
            tk.Button(training_window, text=attribute, command=lambda attr=attribute: self.perform_training(attr, training_window)).pack()

    def perform_training(self, focus, window):
        self.player.train(focus)
        messagebox.showinfo("Treino", f"Você treinou {focus}! Novo valor: {self.player.attributes[focus]}")
        window.destroy()
        self.show_main_menu()

    def advance_year(self):
        self.player.advance_year()
        stats = self.player.statistics
        stats_message = (
            f"Partidas: {stats['Partidas']}\n"
            f"Gols: {stats['Gols']}\n"
            f"Assistências: {stats['Assistências']}\n"
            f"Popularidade: {self.player.popularity}\n"
            f"Felicidade: {self.player.happiness}"
        )
        messagebox.showinfo("Ano Avançado", f"Agora é o ano {self.player.year}. Você tem {self.player.age} anos.\n\nEstatísticas do Ano:\n{stats_message}")
        # Verifica aposentadoria
        if self.player.age >= 35:
            messagebox.showinfo("Aposentadoria", "Você se aposentou da carreira de jogador!")
            self.quit()
        else:
            self.show_main_menu()

    def show_statistics(self):
        stats = self.player.statistics
        stats_message = (
            f"Partidas: {stats['Partidas']}\n"
            f"Gols: {stats['Gols']}\n"
            f"Assistências: {stats['Assistências']}\n"
            f"Popularidade: {self.player.popularity}\n"
            f"Felicidade: {self.player.happiness}"
        )
        messagebox.showinfo("Estatísticas", stats_message)

    def show_relationships(self):
        relationships = self.player.relationships
        rel_message = '\n'.join([f"{k}: {v}" for k, v in relationships.items()])
        messagebox.showinfo("Relações", rel_message)

if __name__ == "__main__":
    app = CareerSimulator()
    app.mainloop()
