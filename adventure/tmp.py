from player import Player
from room import Room
from world import World
from queue import Queue

world = World()
player = Player(world.starting_room)
inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

graph = {}

new_room = {}

for direction in player.current_room.get_exits():
    new_room[direction] = "?"
graph[world.starting_room.id] = new_room

moves_queue = Queue()

total_moves = []

# build the graph
enqueue_moves(player, moves_queue)

# traverse the graph
# while there are still moves on the queue
while moves_queue.size() > 0:
    # set a start room to the current room id of the player
    start_room = player.current_room.id

    # dequeue the next move from the moves queue
    next_move = moves_queue.dequeue()

    # move the player on the next move
    player.travel(next_move)
    
    # add the next move to the total moves
    total_moves.append(next_move)

    # after the move set the end room to the players current room id
    end_room = player.current_room.id

    # update graph to hold the move data (this is an edge)
    graph[start_room][next_move] = end_room

    # check if the end room is in the graph
    if end_room not in graph:
        # add an empty dictionary to the graph at the end room
        graph[end_room] = {}
        # add "?" to the exits of the end room in the graph
        for exit in player.current_room.get_exits():
            graph[end_room][exit] = "?"
    
    # set up the inverse directions for the end room exits (this is an other edge)
    graph[end_room][inverse_directions[next_move]] = start_room

    # once we empty the moves_queue we can enqueue the moves again
    if moves_queue.size() == 0:
        enqueue_moves(player, moves_queue)






def enqueue_moves(player, moves_queue):
    # add all the moves to the moves queue
    pass


