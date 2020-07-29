from player import Player
from room import Room
from world import World
from queue import Queue
from ast import literal_eval

map_file = "maps/test_line.txt"

def enqueue_moves(player, moves_queue):
    # add all the moves to the moves queue
    # set up some current rooms exits
    # create a list of unexplored exits

    # for each direction in the current rooms exits
        # check if the data at the current rooms exit is a "?"
            # if so append the direction to unexplored exits
    
    # if the unexplored exits are empty
        # create a path to enexplored by backtracking
        # room on path will be current room id
        # for each next room in the path to the unexplored room
            # for each direction in the room on path (exits)
                # check if we have found a room to traverse (next room)
                 # if so append the direction to the moves queue
                 # increment the room on path to the next room
                 # and break out of the loop
    # otherwise
        # enqueue the unexplored exits with random sample to the moves queue to move in a random direction
        
    pass

world = World()
# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
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

print(graph)





