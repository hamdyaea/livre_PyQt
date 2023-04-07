from PyQt6.QtSql import QSqlDatabase                                                                                                                                                                                                          
                                                                                                                                                                                                                                              
# Création de la base de données                                                                                                                                                                                                              
db = QSqlDatabase.addDatabase('QSQLITE')                                                                                                                                                                                                      
db.setDatabaseName('example.db')                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
# Ouverture de la base de données                                                                                                                                                                                                             
if not db.open():                                                                                                                                                                                                                             
    print('Impossible d\'ouvrir la base de données')                                                                                                                                                                                          
    exit(1)                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                              
# Fermeture de la base de données                                                                                                                                                                                                             
db.close()          
