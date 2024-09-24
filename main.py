import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# -------------------------------------------- Jogador --------------------------------------------
class Player:
    def __init__(self, name, nationality, age, position, money_level, team, team_strength):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.position = position
        self.attributes = {'Reflexo': 0, 'Posicionamento de goleiro': 0, 'Elasticidade': 0, 'Marcação': 0, 'Desarme': 0, 'Passe curto': 0, 'Passe longo': 0, 'Visão': 0, 'Controle de Bola': 0, 'Drible': 0, 'Força': 0, 'Chute': 0, 'Cabeceio': 0, 'Velocidade': 0, 'Técnica': 0, 'Posicionamento em campo': 0, 'Aptidão física': 0}
        self.money = {'Baixo': random.randint(0, 2000), 'Médio': random.randint(3000, 6000), 'Alto': random.randint(8000, 10000)}[money_level]
        self.team = team
        self.popularity = random.randint(0, 100)
        self.relationships = {'Treinador': random.randint(50, 65), 'Amigos': random.randint(0, 100), 'Família': random.randint(40, 100)}
        self.happiness = (self.relationships['Treinador'] + self.relationships['Amigos'] + self.relationships['Família']) // 3 + random.randint(0, 10)
    
        self.team_strength = team_strength
        
        # Atributos iniciais com base na posição
        if self.position == 'Goleiro':
            self.attributes['Reflexo'] = random.randint(50, 100) 
            self.attributes['Posicionamento de goleiro'] = random.randint(50, 100)
            self.attributes['Elasticidade'] = random.randint(50, 100)
            self.attributes['Marcação'] = random.randint(0, 50)
            self.attributes['Desarme'] = random.randint(0, 50)
            self.attributes['Passe curto'] = random.randint(0, 50)
            self.attributes['Passe longo'] = random.randint(0, 50)
            self.attributes['Visão'] = random.randint(0, 50)
            self.attributes['Controle de Bola'] = random.randint(0, 50)
            self.attributes['Drible'] = random.randint(0, 50)
            self.attributes['Força'] = random.randint(0, 50)
            self.attributes['Chute'] = random.randint(0, 50)
            self.attributes['Cabeceio'] = random.randint(0, 50)
            self.attributes['Velocidade'] = random.randint(0, 50)
            self.attributes['Técnica'] = random.randint(0, 50)
            self.attributes['Posicionamento em campo'] = random.randint(0, 50)
            self.attributes['Aptidão física'] = random.randint(0, 50)
        elif self.position == 'Lateral':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Zagueiro':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Volante':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Meia-defensivo':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Meia-ofensivo':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Ponta':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        elif self.position == 'Centroavante':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Passe curto'] = random.randint(50, 100)
            self.attributes['Passe longo'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Velocidade'] = random.randint(50, 100)
            self.attributes['Técnica'] = random.randint(50, 100)
            self.attributes['Posicionamento em campo'] = random.randint(50, 100)
            self.attributes['Aptidão física'] = random.randint(50, 100)
        
        self.strength = self.calculate_strength()

        # Estatísticas iniciais
        self.statistics = {'Partidas': 0, 'Gols': 0, 'Assistências': 0, 'Nota Média': 0}
        self.yearly_statistics = []
        
        # Escolha do ano inicial
        self.year = 2024

    def calculate_strength(self):
        # Define os pesos dos atributos com base na posição
        # Pesos dos atributos por posição
        ATTRIBUTE_WEIGHTS = {
            'Goleiro': {
            'Reflexo': 0.3,
            'Posicionamento de goleiro': 0.25,
            'Elasticidade': 0.2,
            'Marcação': 0.05,
            'Desarme': 0.05,
            'Passe curto': 0.05,
            'Passe longo': 0.05,
            'Visão': 0.05,
            'Controle de Bola': 0.1,
            'Drible': 0.05,
            'Força': 0.05,
            'Chute': 0.05,
            'Cabeceio': 0.0,
            'Velocidade': 0.05,
            'Técnica': 0.05,
            'Posicionamento em campo': 0.05,
            'Aptidão física': 0.05
            },
            'Lateral': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.15,
            'Desarme': 0.15,
            'Passe curto': 0.1,
            'Passe longo': 0.1,
            'Visão': 0.05,
            'Controle de Bola': 0.1,
            'Drible': 0.1,
            'Força': 0.05,
            'Chute': 0.05,
            'Cabeceio': 0.05,
            'Velocidade': 0.1,
            'Técnica': 0.1,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Zagueiro': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.2,
            'Desarme': 0.2,
            'Passe curto': 0.05,
            'Passe longo': 0.05,
            'Visão': 0.05,
            'Controle de Bola': 0.05,
            'Drible': 0.0,
            'Força': 0.15,
            'Chute': 0.05,
            'Cabeceio': 0.1,
            'Velocidade': 0.05,
            'Técnica': 0.05,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Volante': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.15,
            'Desarme': 0.15,
            'Passe curto': 0.1,
            'Passe longo': 0.1,
            'Visão': 0.1,
            'Controle de Bola': 0.1,
            'Drible': 0.05,
            'Força': 0.1,
            'Chute': 0.05,
            'Cabeceio': 0.05,
            'Velocidade': 0.05,
            'Técnica': 0.1,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Meia-defensivo': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.1,
            'Desarme': 0.1,
            'Passe curto': 0.15,
            'Passe longo': 0.15,
            'Visão': 0.15,
            'Controle de Bola': 0.1,
            'Drible': 0.05,
            'Força': 0.1,
            'Chute': 0.05,
            'Cabeceio': 0.05,
            'Velocidade': 0.05,
            'Técnica': 0.1,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Meia-ofensivo': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.05,
            'Desarme': 0.05,
            'Passe curto': 0.2,
            'Passe longo': 0.2,
            'Visão': 0.2,
            'Controle de Bola': 0.15,
            'Drible': 0.15,
            'Força': 0.1,
            'Chute': 0.1,
            'Cabeceio': 0.05,
            'Velocidade': 0.1,
            'Técnica': 0.1,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Ponta': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.05,
            'Desarme': 0.05,
            'Passe curto': 0.1,
            'Passe longo': 0.1,
            'Visão': 0.1,
            'Controle de Bola': 0.15,
            'Drible': 0.2,
            'Força': 0.1,
            'Chute': 0.15,
            'Cabeceio': 0.05,
            'Velocidade': 0.15,
            'Técnica': 0.15,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            },
            'Centroavante': {
            'Reflexo': 0.0,
            'Posicionamento de goleiro': 0.0,
            'Elasticidade': 0.0,
            'Marcação': 0.05,
            'Desarme': 0.05,
            'Passe curto': 0.05,
            'Passe longo': 0.05,
            'Visão': 0.05,
            'Controle de Bola': 0.1,
            'Drible': 0.1,
            'Força': 0.15,
            'Chute': 0.3,
            'Cabeceio': 0.1,
            'Velocidade': 0.1,
            'Técnica': 0.1,
            'Posicionamento em campo': 0.1,
            'Aptidão física': 0.1
            }
        }
        
        weights = ATTRIBUTE_WEIGHTS.get(self.position, None)
        if not weights:
            # Se a posição não estiver definida, usar pesos iguais
            total_strength = sum(self.attributes.values()) / len(self.attributes)
            return min(total_strength, 100)

        total_strength = 0
        for attr, value in self.attributes.items():
            weight = weights.get(attr, 0)
            total_strength += value * weight
        return min(int(total_strength), 100)

    def train(self, focus):
        # Melhora os atributos com base no foco do treino
        if focus in self.attributes:
            self.attributes[focus] += random.randint(1, 5)
            self.strength += random.randint(1, 3)
            if self.attributes[focus] > 100:
                self.attributes[focus] = 100
            if self.strength > 100:
                self.strength = 100

    def simulate_season_statistics(self):
        # Simula as estatísticas do jogador para a temporada atual
        # Inclui a força do time no cálculo
        base_matches = random.randint(0, 38)  # Número de partidas na temporada

        # Puxando força do time do banco de dados
        cursor.execute("SELECT strength FROM teams WHERE name = ?", (self.team,))
        result = cursor.fetchone()
        self.team_strength = result[0] if result else print("Time não encontrado.")

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
        if self.position.lower() in ['Centroavante', 'Ponta', 'Meia-ofensivo']:
            goal_chance = (self.attributes['Chute'] + self.attributes['Força'] * 0.5) / 150
            assist_chance = (self.attributes['Passe'] + self.attributes['Drible']) / 200
        elif self.position.lower() in ['Volante', 'Meia-defensivo']:
            goal_chance = (self.attributes['Chute'] + self.attributes['Força'] * 0.3) / 200
            assist_chance = (self.attributes['Passe'] + self.attributes['Força'] * 0.2) / 150
        elif self.position.lower() in ['Zagueiro', 'Lateral']:
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
        if self.age > random.randint(25, 30):
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

        # Armazena as estatísticas anuais
        self.yearly_statistics.append({
            'Ano': self.year,
            'Partidas': self.statistics['Partidas'],
            'Gols': self.statistics['Gols'],
            'Assistências': self.statistics['Assistências'],
            'Nota Média': self.statistics['Nota Média']
        })

    def __del__(self):
        # Fecha a conexão com o banco de dados ao destruir o objeto
        self.conn.close()



    def get_total_statistics(self):
        total_stats = {'Partidas': 0, 'Gols': 0, 'Assistências': 0, 'Nota Média': 0}
        for year_stats in self.yearly_statistics:
            total_stats['Partidas'] += year_stats['Partidas']
            total_stats['Gols'] += year_stats['Gols']
            total_stats['Assistências'] += year_stats['Assistências']
        if total_stats['Partidas'] > 0:
            total_stats['Nota Média'] = min((total_stats['Gols'] + total_stats['Assistências']) / total_stats['Partidas'] * 10, 10)
        return total_stats


# -------------------------------------------- Interface gráfica --------------------------------------------
class CareerSimulator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Football Player Career Simulator")
        self.geometry("500x400")
        self.player = None
        self.create_widgets()

    def create_widgets(self):
        # Campos de entrada para informações do jogador
        tk.Label(self, text="Nome do Jogador:").pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        # Campo de seleção para nacionalidade
        tk.Label(self, text="Nacionalidade:").pack()
        self.nationality_var = tk.StringVar()
        self.nationality_entry = tk.ttk.Combobox(self, textvariable=self.nationality_var)
        cursor.execute("SELECT DISTINCT name FROM countries ORDER BY name ASC")
        nationalities = [row[0] for row in cursor.fetchall()]
        self.nationality_entry['values'] = nationalities
        self.nationality_entry.pack()

        # Campo de entrada para idade
        tk.Label(self, text="Idade Inicial:").pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        # Campo de seleção para posição inicial
        tk.Label(self, text="Posição Inicial:").pack()
        self.position_var = tk.StringVar()
        self.position_entry = tk.ttk.Combobox(self, textvariable=self.position_var)
        self.position_entry['values'] = ('Goleiro', 'Lateral', 'Zagueiro', 'Volante', 'Meia-defensivo', 'Meia-ofensivo', 'Ponta', 'Centroavante')
        self.position_entry.pack()

        # Campo de seleção para dinheiro inicial
        tk.Label(self, text="Quantidade de Dinheiro Inicial:").pack()
        self.money_var = tk.StringVar(value='Baixo')
        tk.Radiobutton(self, text='Baixo', variable=self.money_var, value='Baixo').pack()
        tk.Radiobutton(self, text='Médio', variable=self.money_var, value='Médio').pack()
        tk.Radiobutton(self, text='Alto', variable=self.money_var, value='Alto').pack()

        # Botão para iniciar a carreira
        tk.Button(self, text="Iniciar Carreira", command=self.start_career).pack()

    def assign_initial_team(self):
        cursor.execute("SELECT id FROM countries WHERE name = ?", (self.nationality_var.get(),))
        country_id = cursor.fetchone()
        if country_id:
            cursor.execute("SELECT name, strength FROM teams WHERE country_id = ?", (country_id[0],))
            teams = cursor.fetchall()
            if teams:
                team = random.choice(teams)
                self.team_strength = team[1]
                return team[0]
        self.team_strength = 0
        return "Time Desconhecido"
    
    def func_team_strength(self):
        return self.team_strength
        
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
        team = self.assign_initial_team()
        team_strength = self.func_team_strength()
        self.player = Player(name, nationality, age, position, money_level, team, team_strength)
        messagebox.showinfo("Carreira Iniciada", f"Bem-vindo, {self.player.name}! Você começará no time {self.player.team}.")
        self.show_main_menu()

    def show_main_menu(self):
        # Limpa a janela
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text=f"Ano: {self.player.year}", fg="blue").pack()
        tk.Label(self, text=f"Jogador: {self.player.name}, {self.player.age} anos, Força total: {self.player.strength}", fg="green").pack()
        tk.Label(self, text=f"Time Atual: {self.player.team}, (Força Atual: {self.player.team_strength})", fg="red").pack()
        tk.Label(self, text=f"Posição: {self.player.position}", fg="purple").pack()
        tk.Label(self, text=f"Dinheiro: {self.player.money}", fg="orange").pack()
        tk.Button(self, text="Avançar Ano", command=self.advance_year).pack()
        tk.Button(self, text="Treinar", command=self.train_player).pack()
        tk.Button(self, text="Ver Atributos", command=lambda: messagebox.showinfo("Atributos", '\n'.join([f"{k}: {v}" for k, v in self.player.attributes.items()]))).pack()
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
        last_year_stats = self.player.yearly_statistics[-1] if self.player.yearly_statistics else stats
        stats_message = (
            f"\nEstatísticas do Ano {last_year_stats['Ano'] - 1}:\n"
            f"Partidas: {last_year_stats['Partidas']}\n"
            f"Gols: {last_year_stats['Gols']}\n"
            f"Assistências: {last_year_stats['Assistências']}\n"
            f"Nota Média: {last_year_stats['Nota Média']}\n\n"
        )
        messagebox.showinfo("Ano Avançado", f"Agora é o ano {self.player.year}. Você tem {self.player.age} anos.\n{stats_message}\n")
        # Verifica aposentadoria
        if self.player.age >= 35:
            messagebox.showinfo("Aposentadoria", "Você se aposentou da carreira de jogador!")
            self.quit()
        else:
            self.show_main_menu()

    def show_statistics(self):
        total_stats = self.player.get_total_statistics()
        total_stats_message = (
            f"Partidas: {total_stats['Partidas']}\n"
            f"Gols: {total_stats['Gols']}\n"
            f"Assistências: {total_stats['Assistências']}\n"
            f"Nota Média: {total_stats['Nota Média']}\n"
            f"Popularidade: {self.player.popularity}\n"
            f"Felicidade: {self.player.happiness}"
        )
        yearly_stats_message = "\n".join(
            [f"Ano {stats['Ano'] - 1}: Partidas: {stats['Partidas']}, Gols: {stats['Gols']}, Assistências: {stats['Assistências']}, Nota Média: {stats['Nota Média']}" for stats in self.player.yearly_statistics]
        )
        messagebox.showinfo("Estatísticas", f"Estatísticas Totais:\n{total_stats_message}\n\nEstatísticas Anuais:\n{yearly_stats_message}")

    def show_relationships(self):
        relationships = self.player.relationships
        rel_message = '\n'.join([f"{k}: {v}" for k, v in relationships.items()])
        messagebox.showinfo("Relações", rel_message)

if __name__ == "__main__":
    app = CareerSimulator()
    app.mainloop()
