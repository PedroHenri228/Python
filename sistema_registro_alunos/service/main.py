import sqlite3


def connect():
    conn = sqlite3.connect("db/alunos.db")
    return conn


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `alunos` (
            `id` integer primary key NOT NULL UNIQUE,
            `nome` TEXT NOT NULL,
            `email` TEXT NOT NULL,
            `contato` REAL NOT NULL,
            `sexo` TEXT NOT NULL,
            `data_nascimento` REAL NOT NULL,
            `endereco` TEXT NOT NULL,
            `curso` TEXT NOT NULL,
            `foto` TEXT NOT NULL
        );
        """
    )
    conn.commit()
    conn.close()

def insert_student(nome, email, contato, sexo, data_nascimento, endereco, curso):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO alunos (name, email, contato, sexo, data_nascimento, endereco, curso) VALUES (?, ?, ?, ?, ?, ?, ?);
        ''', (nome, email, contato, sexo, data_nascimento, endereco, curso)
    )
    
    conn.commit() 

def get_all_students():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(''' SELECT * FROM alunos; ''')
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_student(student_id, nome, email, contato, sexo, data_nascimento, endereco, curso):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE alunos SET nome = ?, email = ?, contato = ?, sexo = ?,  data_nascimento = ?, endereco = ?, curso = ? WHERE id = ?;
        ''', (nome, email, contato, sexo, data_nascimento, endereco, curso, student_id)
    )

    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM alunos WHERE id = ?;', (student_id,))
    
    conn.commit()
    
    conn.close()

if __name__ == '__main__':
    create_table()