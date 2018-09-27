from kmip.services.server import KmipServer

server = KmipServer(config_path='server.conf', log_path='./log')
with server:
    server.serve()
