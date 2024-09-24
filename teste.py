import tkinter as tk
from tkinter import messagebox
import random
import sqlite3

class Player:
    def __init__(self, name, nationality, age, position, money_level):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.position = position
        self.money = {'Baixo': 1000, 'Médio': 5000, 'Alto': 10000}[money_level]
        self.strength = random.randint(50, 100)
        self.popularity = random.randint(0, 100)
        self.happiness = 100
        self.attributes = {'Força': 50, 'Chute': 50, 'Cabeceio': 50, 'Velocidade': 50, 'Drible': 50, 'Passe': 50}
        self.relationships = {'Treinador': 50, 'Amigos': 50, 'Família': 50}
        self.statistics = {'Partidas': 0, 'Gols': 0, 'Assistências': 0, 'Nota Média': 0}
        self.year = 2021

        # Conecta ao banco de dados e atribui o time inicial
        self.conn = sqlite3.connect('football.db')
        self.cursor = self.conn.cursor()
        self.team, self.team_strength = self.assign_initial_team()

    def assign_initial_team(self):
        # Seleciona times com base na nacionalidade do jogador
        query = "SELECT team_name, strength FROM teams WHERE nationality = ?"
        self.cursor.execute(query, (self.nationality,))
        teams = self.cursor.fetchall()

        if teams:
            team = random.choice(teams)
            return team[0], team[1]  # Retorna o nome do time e sua força
        else:
            # Pequena chance de ser um clube do exterior
            self.cursor.execute("SELECT team_name, strength FROM teams")
            all_teams = self.cursor.fetchall()
            team = random.choice(all_teams)
            return team[0], team[1]

    def train(self, focus):
        if focus in self.attributes:
            improvement = random.randint(1, 5)
            self.attributes[focus] += improvement
            self.strength += improvement * 0.2  # Aumento pequeno na força geral
            self.attributes[focus] = min(100, self.attributes[focus])
            self.strength = min(100, self.strength)

    def simulate_season_statistics(self):
        # Simula as estatísticas do jogador para a temporada atual
        # Inclui a força do time no cálculo
        base_matches = random.randint(20, 38)  # Número de partidas na temporada

        # Normaliza a força do time entre 0 e 1
        team_strength_normalized = self.team_strength / 100

        performance_factor = (
            (self.strength * 0.3) +
            (self.happiness * 0.1) +
            (self.relationships['Treinador'] * 0.1) +
            (self.popularity * 0.1) +
            (team_strength_normalized * 100 * 0.4)
        ) / 100

        # Determina o número de partidas jogadas
        matches_played = int(base_matches * (performance_factor + random.uniform(-0.1, 0.1)))
        matches_played = max(0, min(base_matches, matches_played))

        # Calcula gols e assistências com base nos atributos relevantes
        if self.position.lower() in ['atacante', 'ponta', 'meia']:
            goal_chance = (self.attributes['Chute'] + self.attributes['Força'] * 0.5) / 150
            assist_chance = (self.attributes['Passe'] + self.attributes['Drible']) / 200
        elif self.position.lower() in ['volante', 'meia defensivo']:
            goal_chance = (self.attributes['Chute'] + self.attributes['Força'] * 0.3) / 200
            assist_chance = (self.attributes['Passe'] + self.attributes['Força'] * 0.2) / 150
        elif self.position.lower() in ['zagueiro', 'lateral']:
            goal_chance = (self.attributes['Cabeceio'] + self.attributes['Força'] * 0.2) / 250
            assist_chance = (self.attributes['Passe'] + self.attributes['Velocidade'] * 0.1) / 200
        else:
            goal_chance = 0.01
            assist_chance = 0.01

        # A força do time aumenta as chances de gols e assistências
        goal_chance *= team_strength_normalized
        assist_chance *= team_strength_normalized

        goals = 0
        assists = 0
        ratings = []

        for _ in range(matches_played):
            match_performance = performance_factor + random.uniform(-0.2, 0.2)
            match_performance = max(0, min(1, match_performance))

            # Probabilidade de marcar gol ou assistência em uma partida
            if random.random() < goal_chance * match_performance:
                goals += 1
            if random.random() < assist_chance * match_performance:
                assists += 1

            # Nota da partida baseada na performance
            rating = 6 + (match_performance * 4)  # Notas entre 6 e 10
            ratings.append(rating)

        # Atualiza as estatísticas da temporada
        self.statistics['Partidas'] += matches_played
        self.statistics['Gols'] += goals
        self.statistics['Assistências'] += assists
        if ratings:
            average_rating = sum(ratings) / len(ratings)
            self.statistics['Nota Média'] = round(average_rating, 2)
        else:
            self.statistics['Nota Média'] = 0

        # Atualiza a popularidade com base no desempenho
        self.popularity += int((goals + assists) * 0.5)
        self.popularity = max(0, min(100, self.popularity))

    def advance_year(self):
        self.age += 1
        self.year += 1

        # Diminui a força com a idade
        if self.age > 30:
            decline = random.uniform(0.5, 1.5)
            self.strength -= decline
            for attr in self.attributes:
                self.attributes[attr] -= decline
                self.attributes[attr] = max(0, self.attributes[attr])
            self.strength = max(0, self.strength)

        # Simula a temporada
        self.simulate_season_statistics()

        # Atualiza a felicidade (pode ser afetada por vários fatores)
        happiness_change = random.randint(-5, 5)
        self.happiness += happiness_change
        self.happiness = max(0, min(100, self.happiness))

    def __del__(self):
        # Fecha a conexão com o banco de dados ao destruir o objeto
        self.conn.close()

class CareerSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simulador de Carreira de Futebol")
        self.geometry("500x500")
        self.player = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Nome do Jogador:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        tk.Label(self, text="Nacionalidade:").pack()
        self.nationality_entry = tk.Entry(self)
        self.nationality_entry.pack()

        tk.Label(self, text="Idade Inicial:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        tk.Label(self, text="Posição Inicial:").pack()
        self.position_entry = tk.Entry(self)
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
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text=f"Ano: {self.player.year}").pack()
        tk.Label(self, text=f"Jogador: {self.player.name}, {self.player.age} anos, Força: {self.player.strength:.2f}").pack()
        tk.Label(self, text=f"Time Atual: {self.player.team} (Força do Time: {self.player.team_strength})").pack()
        tk.Button(self, text="Treinar", command=self.train_player).pack()
        tk.Button(self, text="Avançar Ano", command=self.advance_year).pack()
        tk.Button(self, text="Ver Estatísticas", command=self.show_statistics).pack()
        tk.Button(self, text="Ver Relações", command=self.show_relationships).pack()
        tk.Button(self, text="Sair", command=self.quit).pack()

    def train_player(self):
        training_window = tk.Toplevel(self)
        training_window.title("Treinar Jogador")
        tk.Label(training_window, text="Escolha o foco do treino:").pack()
        for attribute in self.player.attributes.keys():
            tk.Button(training_window, text=attribute, command=lambda attr=attribute: self.perform_training(attr, training_window)).pack()

    def perform_training(self, focus, window):
        self.player.train(focus)
        messagebox.showinfo("Treino", f"Você treinou {focus}! Novo valor: {self.player.attributes[focus]:.2f}")
        window.destroy()
        self.show_main_menu()

    def advance_year(self):
        self.player.advance_year()
        messagebox.showinfo("Ano Avançado", f"Agora é o ano {self.player.year}. Você tem {self.player.age} anos.")
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
            f"Nota Média: {stats['Nota Média']}\n"
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
