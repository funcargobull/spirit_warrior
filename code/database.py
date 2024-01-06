import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

    def create_tables(self):
        # Текущие показатели игрока
        self.cur.execute("""
        create table if not exists current_stats (
        hero TEXT
        hp INTEGER
        shield INTEGER
        energy INTEGER
        wave INTEGER
        weapon TEXT
        )
        """)

        # Данные по волнам
        self.cur.execute("""
        create table if not exists waves_stats (
        wave INT
        enemy_count INT
        )
        """)

        self.conn.commit()

    def get_wave(self):
        self.cur.execute("select wave from current_stats")
        return self.cur.fetchall()[0]

    def start_new_game(self):
        pass
        # self.cur.execute("delete from current_stats")
        #
        # with open("tmp.txt") as f:
        #     hero_name = f.read()
        #
        # hero = eval(f"characters.{hero_name}()")
        #
        # self.cur.execute("""
        # insert into current_stats values (?, ?, ?, ?, 1, "Machete")
        # """, (hero_name, hero.health, hero.armor, hero.energy))