import sqlite3

def connect():
    conn = sqlite3.connect('crud.db')
    return conn

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    );
    ''')

    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO users (name, age) VALUES (?, ?);
        ''', (name, age)
    )
    
    conn.commit() 

def get_all_users():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(''' SELECT * FROM users; ''')
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_user(user_id, name, age):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE users SET name = ?, age = ? WHERE id = ?;
        ''', (name, age, user_id)
    )

    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users WHERE id = ?;', (user_id,))
    
    conn.commit()
    conn.close()

def menu():
    while True:
        print("\n--- CRUD com SQLite ---")
        print("1. Inserir usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Deletar usuário")
        print("5. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Digite o nome: ")
            age = int(input("Digite a idade: "))
            insert_user(name, age)
        elif choice == '2':
            users = get_all_users()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = int(input("Digite o ID do usuário: "))
            name = input("Digite o novo nome: ")
            age = int(input("Digite a nova idade: "))
            update_user(user_id, name, age)
        elif choice == '4':
            user_id = int(input("Digite o ID do usuário: "))
            delete_user(user_id)
        elif choice == '5':
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    create_table()
    menu()
