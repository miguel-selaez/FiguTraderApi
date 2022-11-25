from flask import Flask, jsonify, request

app = Flask(__name__)

from album import album
from usuario_album import usuarioAlbumTx

@app.route('/api/album', methods=['GET'])
def getAlbum():
    return jsonify(album)

@app.route('/api/usuario/<string:usuarioId>/album', methods=['GET'])
def getUserAlbum(usuarioId):
    figusUsuario = [usuarioAlbum for usuarioAlbum in usuarioAlbumTx if usuarioAlbum['usuarioId'] == usuarioId]
    return jsonify(figusUsuario)

@app.route('/api/usuario/<string:usuarioId>/album', methods=['POST'])
def addFigu(usuarioId):
    figuId = request.json['figuId']
    cantidad = request.json['cantidad']
    figuUsuario = [usuarioAlbum for usuarioAlbum in usuarioAlbumTx if usuarioAlbum['usuarioId'] == usuarioId and usuarioAlbum['figuId'] == figuId]
    if (len(figuUsuario) > 0):
        figuUsuario[0]['cantidad'] = cantidad
    else:
        nuevaFigu = {
            "id": getNextId(),
            "usuarioId": usuarioId,
            "figuId": figuId,
            "cantidad" : cantidad
        }
        usuarioAlbumTx.append(nuevaFigu)

    nuevafigusUsuario = [usuarioAlbum for usuarioAlbum in usuarioAlbumTx if usuarioAlbum['usuarioId'] == usuarioId]
    return jsonify(nuevafigusUsuario)

def getNextId():
    return len(usuarioAlbumTx) + 1

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)