import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import random
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# -------------------------------------------- Jogador --------------------------------------------
class Player:
    def __init__(self, name, nationality, age, position, money_level, team):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.position = position
        self.attributes = {'Reflexo': 0, 'Posicionamento': 0, 'Marcação': 0, 'Desarme': 0, 'Passe': 0, "Visão": 0, 'Controle de Bola': 0, 'Drible': 0, 'Força': 0, 'Chute': 0, 'Cabeceio': 0}
        self.money = {'Baixo': random.randint(0, 2000), 'Médio': random.randint(3000, 6000), 'Alto': random.randint(8000, 10000)}[money_level]
        self.team = team
        self.strength = self.calculate_strength()
        self.popularity = random.randint(0, 100)
        self.relationships = {'Treinador': random.randint(50, 65), 'Amigos': random.randint(0, 100), 'Família': random.randint(40, 100)}
        self.happiness = (self.relationships['Treinador'] + self.relationships['Amigos'] + self.relationships['Família']) // 3 + random.randint(0, 20)
        
        # Atributos iniciais com base na posição
        if self.position == 'Goleiro':
            self.attributes['Reflexo'] = random.randint(50, 100)
            self.attributes['Posicionamento'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Marcação'] = random.randint(0, 50)
            self.attributes['Desarme'] = random.randint(0, 50)
            self.attributes['Passe'] = random.randint(0, 50)
            self.attributes['Visão'] = random.randint(0, 50)
            self.attributes['Controle de Bola'] = random.randint(0, 50)
            self.attributes['Drible'] = random.randint(0, 50)
        elif self.position == 'Defensor':
            self.attributes['Marcação'] = random.randint(50, 100)
            self.attributes['Desarme'] = random.randint(50, 100)
            self.attributes['Força'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Reflexo'] = random.randint(0, 50)
            self.attributes['Posicionamento'] = random.randint(0, 50)
            self.attributes['Passe'] = random.randint(0, 50)
            self.attributes['Visão'] = random.randint(0, 50)
            self.attributes['Controle de Bola'] = random.randint(0, 50)
            self.attributes['Drible'] = random.randint(0, 50)
        elif self.position == 'Meio-campista':
            self.attributes['Passe'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(50, 100)
            self.attributes['Marcação'] = random.randint(0, 50)
            self.attributes['Desarme'] = random.randint(0, 50)
            self.attributes['Força'] = random.randint(0, 50)
            self.attributes['Cabeceio'] = random.randint(0, 50)
            self.attributes['Reflexo'] = random.randint(0, 50)
            self.attributes['Posicionamento'] = random.randint(0, 50)
        elif self.position == 'Atacante':
            self.attributes['Passe'] = random.randint(50, 100)
            self.attributes['Visão'] = random.randint(50, 100)
            self.attributes['Controle de Bola'] = random.randint(50, 100)
            self.attributes['Drible'] = random.randint(50, 100)
            self.attributes['Chute'] = random.randint(80, 100)
            self.attributes['Cabeceio'] = random.randint(50, 100)
            self.attributes['Marcação'] = random.randint(0, 50)
            self.attributes['Desarme'] = random.randint(0, 50)
            self.attributes['Força'] = random.randint(0, 50)
            self.attributes['Reflexo'] = random.randint(0, 50)
            self.attributes['Posicionamento'] = random.randint(0, 50)
        
        # Estatísticas iniciais
        self.statistics = {'Partidas': 0, 'Gols': 0, 'Assistências': 0, 'Nota Média': 0}
        self.yearly_statistics = []
        
        # Escolha do ano inicial
        self.year = 2024
        
        # Força inicial de acordo com a idade
        if self.age < 16:
            self.strength += random.randint(0, 10)
        elif self.age >= 16 and self.age < 18:
            self.strength += random.randint(10, 35)
        elif self.age >= 18:
            self.strength += random.randint(20, 50)

    def calculate_strength(self):
        # Define os pesos dos atributos com base na posição
        weights = {
            'Goleiro': {'Reflexo': 0.3, 'Posicionamento': 0.2, 'Marcação': 0.05, 'Desarme': 0.05, 'Passe': 0.05, 'Visão': 0.05, 'Controle de Bola': 0.05, 'Drible': 0.05, 'Força': 0.1, 'Chute': 0.05, 'Cabeceio': 0.05},
            
            'Defensor': {'Reflexo': 0.05, 'Posicionamento': 0.1, 'Marcação': 0.2, 'Desarme': 0.2, 'Passe': 0.05, 'Visão': 0.05, 'Controle de Bola': 0.05, 'Drible': 0.05, 'Força': 0.1, 'Chute': 0.05, 'Cabeceio': 0.1},
            
            'Meio-campista': {'Reflexo': 0.05, 'Posicionamento': 0.05, 'Marcação': 0.1, 'Desarme': 0.1, 'Passe': 0.2, 'Visão': 0.2, 'Controle de Bola': 0.1, 'Drible': 0.1, 'Força': 0.05, 'Chute': 0.05, 'Cabeceio': 0.05},
            
            'Atacante': {'Reflexo': 0.05, 'Posicionamento': 0.05, 'Marcação': 0.05, 'Desarme': 0.05, 'Passe': 0.1, 'Visão': 0.1, 'Controle de Bola': 0.1, 'Drible': 0.1, 'Força': 0.05, 'Chute': 0.2, 'Cabeceio': 0.15}
        }
        
        # Calcula a força do jogador com base nos atributos e pesos
        total = 0
        for attribute, value in self.attributes.items():
            total += value * weights[self.position].get(attribute, 0)
        
        return int(total)

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
        if self.age > random.randint(25, 30):
            self.strength -= random.randint(0, 5)
        # Simula as estatísticas da temporada com base na força e posição do jogador
        partidas = 0
        gols = 0
        assistencias = 0

        # Simula as estatísticas da temporada com base na força e posição do jogador e do time
        cursor.execute("SELECT strength FROM teams WHERE name = ?", (self.team,))
        result = cursor.fetchone()
        team_strength = result[0] if result else print("Time não encontrado.")

        if self.position == 'Goleiro':
            if self.strength > 50 and self.strength >= team_strength:
                partidas = random.randint(0, 40)
                gols = random.randint(0, 2)
                assistencias = random.randint(0, 5)
            else:
                partidas = random.randint(0, 5)
                gols = random.randint(0, 0)
                assistencias = random.randint(0, 3)
                
        elif self.position == 'Defensor':
            if self.strength > 50 and self.strength >= team_strength:
                partidas = random.randint(0, 40)
                gols = random.randint(0, 5)
                assistencias = random.randint(0, 10)
            else:
                partidas = random.randint(0, 10)
                gols = random.randint(0, 3)
                assistencias = random.randint(0, 5)
                
        elif self.position == 'Meio-campista':
            if self.strength > 50 and self.strength >= team_strength:
                partidas = random.randint(0, 40)
                gols = random.randint(0, 10)
                assistencias = random.randint(0, 15)
            else:
                partidas = random.randint(0, 20)
                gols = random.randint(0, 5)
                assistencias = random.randint(0, 10)
                
        elif self.position == 'Atacante':
            if self.strength >= team_strength:
                partidas = random.randint(0, 40)
                gols = random.randint(0, 30)
                assistencias = random.randint(0, 10)
            else:
                partidas = random.randint(0, 20)
                gols = random.randint(0, 15)
                assistencias = random.randint(0, 5)

        self.statistics['Partidas'] += partidas
        self.statistics['Gols'] += gols
        self.statistics['Assistências'] += assistencias
        if partidas > 0:
            if gols > 0 or assistencias > 0:
                self.statistics['Nota Média'] = min((gols + assistencias) / partidas * 10, 10)
            else:
                self.statistics['Nota Média'] = min(self.strength / 10, 10)
        else:
            self.statistics['Nota Média'] = 0
        
        # Atualiza a popularidade
        self.popularity += random.randint(-5, 5)
        self.popularity = max(0, min(100, self.popularity))
        
        # Atualiza a felicidade
        self.happiness += random.randint(-5, 5)
        self.happiness = max(0, min(100, self.happiness))

        # Armazena as estatísticas anuais
        self.yearly_statistics.append({
            'Ano': self.year,
            'Partidas': partidas,
            'Gols': gols,
            'Assistências': assistencias,
            'Nota Média': self.statistics['Nota Média'],
            'Popularidade': self.popularity,
            'Felicidade': self.happiness
        })

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
        self.position_entry['values'] = ('Goleiro', 'Defensor', 'Meio-campista', 'Atacante')
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
            cursor.execute("SELECT name FROM teams WHERE country_id = ?", (country_id[0],))
            teams = [row[0] for row in cursor.fetchall()]
            if teams:
                return random.choice(teams)
        return "Time Desconhecido"

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
        self.player = Player(name, nationality, age, position, money_level, team)
        messagebox.showinfo("Carreira Iniciada", f"Bem-vindo, {self.player.name}! Você começará no time {self.player.team}.")
        self.show_main_menu()

    def show_main_menu(self):
        # Limpa a janela
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text=f"Ano: {self.player.year}", fg="blue").pack()
        tk.Label(self, text=f"Jogador: {self.player.name}, {self.player.age} anos, Força total: {self.player.strength}", fg="green").pack()
        tk.Label(self, text=f"Time Atual: {self.player.team}", fg="red").pack()
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
        stats_message = (
            f"Partidas: {stats['Partidas']}\n"
            f"Gols: {stats['Gols']}\n"
            f"Assistências: {stats['Assistências']}\n"
            f"Nota Média: {stats['Nota Média']}\n"
            f"Popularidade: {self.player.popularity}\n"
            f"Felicidade: {self.player.happiness}"
        )
        messagebox.showinfo("Ano Avançado", f"Agora é o ano {self.player.year}. Você tem {self.player.age} anos.\n\nEstatísticas totais:\n{stats_message}")
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
        messagebox.showinfo("Estatísticas", f"Estatísticas Totais:\n{total_stats_message}\nEstatísticas Anuais:\n{yearly_stats_message}")

    def show_relationships(self):
        relationships = self.player.relationships
        rel_message = '\n'.join([f"{k}: {v}" for k, v in relationships.items()])
        messagebox.showinfo("Relações", rel_message)

if __name__ == "__main__":
    app = CareerSimulator()
    app.mainloop()
