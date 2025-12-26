class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.next = None
        self.is_leader = False

    def receive_election(self, received_id, counter):
        counter["messages"] += 1

        if received_id > self.id:
            self.next.receive_election(received_id, counter)

        elif received_id == self.id:
            # This node is the leader
            self.is_leader = True
            self.next.receive_leader(self.id, counter)

        # If received_id < self.id → message is dropped (Chang–Roberts rule)

    def receive_leader(self, leader_id, counter):
        counter["messages"] += 1

        if self.id != leader_id:
            self.next.receive_leader(leader_id, counter)

