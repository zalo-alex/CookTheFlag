ws_clients = []

def broadcast(message):
    # Loop through latest clients because they have more chance to be connected
    for client in ws_clients[::-1].copy():
        try:
            client.send(message)
        except Exception as e:
            ws_clients.remove(client)