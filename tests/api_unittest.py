from deepnlpf.server import app, socketio

# TODO Remover IP e Port daqui e colocar em um aqruivo de configuração.
socketio.run(app, host="0.0.0.0", port=5000)