# Distributed Leader Election – Chang–Roberts Algorithm

## Description
This project simulates a distributed leader election algorithm
(Chang–Roberts) in a ring network.

Each node has a unique identifier (ID), and the node with the highest ID
is elected as the leader through message passing.

## Algorithm
- Ring topology
- Chang–Roberts leader election algorithm
- Leader is the node with the highest ID
- Message cost is measured and displayed

## Project Structure
.
├── main.py
├── node.py
└── README.md

perl
Copy code

> Both `main.py` and `node.py` must be in the same folder for the program to run correctly.

## How to Run
Make sure Python 3 is installed, then run:

```bash
python main.py
