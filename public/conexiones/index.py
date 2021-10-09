import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
MONGO_URI= "mongodb://"+ MONGO_HOST+ ":"+ MONGO_PUERTO +"/"
try:
    cliente=pymongo.mongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexion Exitosa")
    cliente.close()
    except pymongo.errors.serverSelectionTimeoutError  expression as ErrorTiempo:
    print("Tiempo Fuer"+ErrorTiempo)
    except pymongo.error.conectionFailure as errorConexion:
    print("La conexion Fallo" +errorConexion)