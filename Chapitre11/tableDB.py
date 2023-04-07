from PyQt6.QtSql import QSqlDatabase, QSqlQuery                                                                                                                                                                                               
                                                                                                                                                                                                                                              
# Création de la base de données                                                                                                                                                                                                              
db = QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('example.db')

# Ouverture de la base de données
if not db.open():
    print('Impossible d\'ouvrir la base de données')
    exit(1)

# Création de la table 'personnes'
query = QSqlQuery()
query.exec('CREATE TABLE personnes (nom TEXT, age INT)')

# Fermeture de la base de données
db.close()

