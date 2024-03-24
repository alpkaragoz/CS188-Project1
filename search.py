# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Picking stack DS for frontier because DFS is implemented (LIFO)
    frontier = util.Stack()

    # Using set DS to track visited nodes (prevent duplicate entries)
    visited = set()

    # Pushing start state to frontier as tuple, storing location and moves thus far.
    frontier.push((problem.getStartState(), []))

    # Loop until frontier is empty
    while not frontier.isEmpty():
        # Get the current state
        current_state = frontier.pop()

        # Return moves if current node is goal state
        if problem.isGoalState(current_state[0]):
            return current_state[1]

        # Do not re-visit a node again
        if current_state[0] in visited:
            continue

        # Getting next moves, and adding them to frontier in given order.
        next_state_array = problem.getSuccessors(current_state[0])
        for next in next_state_array:
            # Pushing then next states to frontier and tracking the moves made thus far.
            frontier.push((next[0], current_state[1] + [next[1]]))
        visited.add(current_state[0])

    # Returning empty list i.e. failed to find the solution
    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Picking Queue DS for frontier because BFS is implemented (FIFO)
    frontier = util.Queue()

    # Using set DS to track visited nodes (prevent duplicate entries)
    visited = set()

    # Pushing start state to frontier as tuple, storing location and moves thus far.
    frontier.push((problem.getStartState(), []))

    # Loop until frontier is empty
    while not frontier.isEmpty():
        # Get the current state
        current_state = frontier.pop()

        # Return moves if current node is goal state
        if problem.isGoalState(current_state[0]):
            return current_state[1]

        # Do not re-visit a node again
        if current_state[0] in visited:
            continue

        # Getting next moves, and adding them to frontier in given order.
        next_state_array = problem.getSuccessors(current_state[0])
        for next in next_state_array:
            # Pushing then next states to frontier and tracking the moves made thus far.
            frontier.push((next[0], current_state[1] + [next[1]]))
        visited.add(current_state[0])

    # Returning empty list i.e. failed to find the solution
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Picking PriorityQueue DS for frontier because each node has different value.
    frontier = util.PriorityQueue()

    # Using set DS to track visited nodes (prevent duplicate entries)
    visited = set()

    # Pushing start state to frontier as tuple tracking also accumulated cost.
    frontier.push((problem.getStartState(), [], 0), 0)

    # Loop until frontier is empty
    while not frontier.isEmpty():
        # Get the current state
        current_state = frontier.pop()

        # Return moves if current node is goal state
        if problem.isGoalState(current_state[0]):
            return current_state[1]

        # Do not re-visit a node again
        if current_state[0] in visited:
            continue

        # Getting next moves, and adding them to frontier.
        next_state_array = problem.getSuccessors(current_state[0])
        for next in next_state_array:
            # Pushing then next states to frontier and tracking the moves and cost thus far.
            frontier.push((next[0], current_state[1] + [next[1]], current_state[2] + next[2]), current_state[2] + next[2])
        visited.add(current_state[0])

    # Returning empty list i.e. failed to find the solution
    return []



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Defining f(s) = g(s) + h(s)
    fs = lambda item: item[2] + heuristic(item[0], problem)

    # Using PQ with fn to calculate f(s) = g(s) + h(s)
    frontier = util.PriorityQueueWithFunction(fs)

    # Using set DS to track visited nodes (prevent duplicate entries)
    visited = set()

    # Pushing start state to frontier as tuple tracking also accumulated cost.
    frontier.push((problem.getStartState(), [], 0))

    # Loop until frontier is empty
    while not frontier.isEmpty():
        # Get the current state
        current_state = frontier.pop()

        # Return moves if current node is goal state
        if problem.isGoalState(current_state[0]):
            return current_state[1]

        # Do not re-visit a node again
        if current_state[0] in visited:
            continue

        # Getting next moves, and adding them to frontier.
        next_state_array = problem.getSuccessors(current_state[0])
        for next in next_state_array:
            # Pushing then next states to frontier and tracking the moves and cost thus far.
            frontier.push((next[0], current_state[1] + [next[1]], current_state[2] + next[2]))
        visited.add(current_state[0])

    # Returning empty list i.e. failed to find the solution
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
