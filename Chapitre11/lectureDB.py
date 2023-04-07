from PyQt6.QtSql import QSqlDatabase, QSqlQuery

# Création de la base de données
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('example.db')

# Ouverture de la base de données
if not db.open():
    print('Impossible d\'ouvrir la base de données')
    exit(1)

# Sélection de toutes les données de la table 'personnes'
query = QSqlQuery()
query.exec('SELECT * FROM personnes')

# Parcours des données et affichage
while query.next():
    nom = query.value(0)
    age = query.value(1)
    print(f'Nom : {nom}, Age : {age}')

# Fermeture de la base de données
db.close()
