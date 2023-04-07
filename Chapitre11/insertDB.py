from PyQt6.QtSql import QSqlDatabase, QSqlQuery

# Création de la base de données
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('example.db')

# Ouverture de la base de données
if not db.open():
    print('Impossible d\'ouvrir la base de données')
    exit(1)

# Insertion de données dans la table 'personnes'
query = QSqlQuery()
query.exec("INSERT INTO personnes (nom, age) VALUES ('Alice', 25)")
query.exec("INSERT INTO personnes (nom, age) VALUES ('Bob', 30)")

# Fermeture de la base de données
db.close()

