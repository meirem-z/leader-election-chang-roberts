from node import Node


def create_ring(node_ids):
    nodes = [Node(i) for i in node_ids]

    for i in range(len(nodes)):
        nodes[i].next = nodes[(i + 1) % len(nodes)]

    return nodes


def chang_roberts(nodes):
    counter = {"messages": 0}

    for node in nodes:
        node.next.receive_election(node.id, counter)

    leader = None
    for node in nodes:
        if node.is_leader:
            leader = node
            break

    return leader.id, counter["messages"]


if __name__ == "__main__":
    node_ids = [3, 7, 12, 5, 9]
    nodes = create_ring(node_ids)

    leader_id, message_count = chang_roberts(nodes)

    print("Node IDs:", node_ids)
    print("Elected Leader:", leader_id)
    print("Total messages exchanged:", message_count)
