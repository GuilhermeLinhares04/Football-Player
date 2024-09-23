import random
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Classe para representar o Jogador
class Player:
    def __init__(self, name, nationality, age, position, money_level):
        self.name = name
        self.nationality = nationality
        self.age = age
        self.position = position
        self.money = self.set_initial_money(money_level)
        self.strength = random.randint(0, 100)
        self.popularity = random.randint(0, 100)
        self.happiness = 100  # barra de felicidade inicial
        self.relationships = {
            "coach": random.randint(50, 100),
            "friends": random.randint(50, 100),
            "family": random.randint(50, 100),
            "girlfriend": random.randint(0, 1) * random.randint(50, 100),  # Relacionamento com namorada/noiva
        }
        self.stats = {"matches": 0, "goals": 0, "assists": 0, "average_rating": 0.0}
        self.training_focus = None

    def set_initial_money(self, level):
        if level == "low":
            return random.randint(5000, 15000)
        elif level == "medium":
            return random.randint(20000, 50000)
        elif level == "high":
            return random.randint(60000, 100000)

    def train(self, focus):
        self.training_focus = focus
        if focus == "strength":
            self.strength += random.randint(1, 5)
        elif focus == "shooting":
            self.strength += random.randint(1, 3)
        elif focus == "heading":
            self.strength += random.randint(1, 4)
        elif focus == "speed":
            self.strength += random.randint(1, 5)
        elif focus == "stamina":
            self.strength += random.randint(1, 4)

        # Treino afetando felicidade e força
        self.happiness -= random.randint(0, 2)
        messagebox.showinfo("Treino", f"{self.name} treinou {focus}!")

    def update_stats(self, matches, goals, assists, average_rating):
        self.stats["matches"] += matches
        self.stats["goals"] += goals
        self.stats["assists"] += assists
        self.stats["average_rating"] = (self.stats["average_rating"] + average_rating) / 2

    def get_summary(self):
        return (f"{self.name}, {self.age} anos\nForça: {self.strength}, Popularidade: {self.popularity}\n"
                f"Felicidade: {self.happiness}%\nPartidas: {self.stats['matches']}, Gols: {self.stats['goals']}, "
                f"Assistências: {self.stats['assists']}, Nota Média: {self.stats['average_rating']:.2f}\n")

# Classe para representar os Times
class Team:
    def __init__(self, name, country, strength):
        self.name = name
        self.country = country
        self.strength = strength
        self.players = []

    def add_player(self, player):
        self.players.append(player)

# Função para simular uma temporada
def simulate_season(player, team):
    # Simulação simples de desempenho com base na posição do jogador e sua força
    matches = 0
    goals = 0
    assists = 0
    average_rating = 0.0
    
    if player.position == "Goleiro":
        matches = random.randint(0, player.strength // 10)
        goals = random.randint(0, player.strength // 10)
        assists = random.randint(0, player.strength // 20)
        average_rating = random.uniform(6, 8)
    elif player.position == "Zagueiro":
        matches = random.randint(0, player.strength // 7)
        goals = random.randint(0, player.strength // 8)
        assists = random.randint(0, player.strength // 15)
        average_rating = random.uniform(6, 8.5)
    elif player.position == "Lateral":
        matches = random.randint(0, player.strength // 6)
        goals = random.randint(0, player.strength // 6)
        assists = random.randint(0, player.strength // 12)
        average_rating = random.uniform(6.5, 8.5)
    elif player.position == "Volante":
        matches = random.randint(0, player.strength // 5)
        goals = random.randint(0, player.strength // 5)
        assists = random.randint(0, player.strength // 10)
        average_rating = random.uniform(6.5, 9)
    elif player.position == "Meia":
        matches = random.randint(0, player.strength // 4)
        goals = random.randint(0, player.strength // 4)
        assists = random.randint(0, player.strength // 8)
        average_rating = random.uniform(7, 9.5)
    elif player.position == "Ponta":
        matches = random.randint(0, player.strength // 3)
        goals = random.randint(0, player.strength // 3)
        assists = random.randint(0, player.strength // 6)
        average_rating = random.uniform(7.5, 9.5)
    elif player.position == "Atacante":
        matches = random.randint(0, player.strength // 2)
        goals = random.randint(0, player.strength // 2)
        assists = random.randint(0, player.strength // 4)
        average_rating = random.uniform(8, 10)
    
    player.update_stats(matches, goals, assists, average_rating)
    messagebox.showinfo("Temporada Finalizada", f"Estatísticas de {player.name}:\n"
                                               f"Partidas: {player.stats['matches']}\n"
                                               f"Gols: {player.stats['goals']}\n"
                                               f"Assistências: {player.stats['assists']}\n"
                                               f"Nota Média: {player.stats['average_rating']:.2f}")

    # Aumentar a idade do jogador
    player.age += 1
    
    # Exibir propostas no final da temporada
    if player.popularity > 70:
        messagebox.showinfo("Propostas", f"{player.name} recebeu propostas de transferência de outros times!")
    else:
        messagebox.showinfo("Sem Propostas", f"{player.name} permanecerá no time atual.")

# Interface gráfica (GUI)
class FootballCareerSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Carreira de Futebol")
        self.player = None

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Labels e Entradas
        tk.Label(self.root, text="Nome do Jogador:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nacionalidade:").grid(row=1, column=0, padx=10, pady=5)
        self.nationality_entry = ttk.Combobox(self.root, values=["Brasil", "Argentina", "Uruguai", "Chile", "Colômbia"])
        self.nationality_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Idade:").grid(row=2, column=0, padx=10, pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Posição:").grid(row=3, column=0, padx=10, pady=5)
        self.position_entry = ttk.Combobox(self.root, values=["Goleiro", "Zagueiro", "Lateral", "Volante", "Meia", "Ponta", "Atacante"])
        self.position_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Nível de Dinheiro:").grid(row=4, column=0, padx=10, pady=5)
        self.money_level = ttk.Combobox(self.root, values=["low", "medium", "high"])
        self.money_level.grid(row=4, column=1, padx=10, pady=5)

        # Botão para criar jogador
        self.create_player_button = tk.Button(self.root, text="Criar Jogador", command=self.create_player)
        self.create_player_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Botão para simular temporada
        self.simulate_button = tk.Button(self.root, text="Simular Temporada", command=self.simulate_season)
        self.simulate_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Botão para treino
        self.train_button = tk.Button(self.root, text="Treinar", command=self.train_player)
        self.train_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Área de exibição de informações do jogador
        self.player_info = tk.Text(self.root, width=40, height=10, state='disabled')
        self.player_info.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    def create_player(self):
        # Criar jogador com os dados fornecidos
        name = self.name_entry.get()
        nationality = self.nationality_entry.get()
        age = int(self.age_entry.get())
        position = self.position_entry.get()
        money_level = self.money_level.get()

        if name and nationality and age and position and money_level:
            self.player = Player(name, nationality, age, position, money_level)
            self.update_player_info()
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    def simulate_season(self):
        if self.player:
            team = Team("Flamengo", "Brasil", 80)  # Time de exemplo
            team.add_player(self.player)
            simulate_season(self.player, team)
            self.update_player_info()
        else:
            messagebox.showerror("Erro", "Nenhum jogador foi criado ainda.")

    def train_player(self):
        if self.player:
            # Seleção de treino
            focus_options = ["strength", "shooting", "heading", "speed", "stamina"]
            focus = ttk.Combobox(self.root, values=focus_options)
            focus.current(0)
            focus_dialog = tk.Toplevel(self.root)
            focus_dialog.title("Escolha o foco do treino")
            focus_dialog.geometry("200x100")
            focus_dialog.resizable(False, False)
            focus_label = tk.Label(focus_dialog, text="Foco do treino:")
            focus_label.pack()
            focus.pack()
            confirm_button = tk.Button(focus_dialog, text="Confirmar", command=lambda: self.confirm_training(focus.get(), focus_dialog))
            confirm_button.pack()
        else:
            messagebox.showerror("Erro", "Nenhum jogador foi criado ainda.")

    def confirm_training(self, focus, focus_dialog):
        if focus in ["strength", "shooting", "heading", "speed", "stamina"]:
            self.player.train(focus)
            self.update_player_info()
            focus_dialog.destroy()
        else:
            messagebox.showerror("Erro", "Opção de treino inválida.")

    def update_player_info(self):
        # Exibir informações do jogador
        self.player_info.config(state='normal')
        self.player_info.delete(1.0, tk.END)
        self.player_info.insert(tk.END, self.player.get_summary())
        self.player_info.config(state='disabled')


# Inicializar a aplicação
root = tk.Tk()
app = FootballCareerSimulatorApp(root)
root.mainloop()
