from typing import List

def get_order_of_courses(relationships: List[List[str]]) -> List[str]:
    # Create two dictionaries
    connections = {}  # Keeping track of the number of connections each node has
    graph = {}  # The node graph
    
    # Build the graph and connections
    for relationship in relationships:  # Iterate through the input
        prereq, course = relationship  # Look for prereq and course to add to the graph
        if prereq not in graph:
            graph[prereq] = set()
        if course not in graph:
            graph[course] = set()
        # Keeps track of how many prereqs each course has
        graph[prereq].add(course)
        connections[course] = connections.get(course, 0) + 1  # Increment course node
    
    # Get all the nodes with 0 indegrees and add them to the queue
    no_prereqs = []  # Classes with no prereqs (is a queue)
    for node in graph:
        if node not in connections:
            no_prereqs.append(node)  # Append courses with no prereqs
    
    # Topological sorting
    course_order = []
    while no_prereqs:
        node = no_prereqs.pop(0)  # If node is in the queue
        course_order.append(node)  # Add to list
        for next in graph[node]:
            connections[next] -= 1  # Take away from the node
            if connections[next] == 0:  # If node is 0 then add to the queue
                no_prereqs.append(next)
    
    if len(course_order) != len(graph):  # If length of list is not equal to the nodes in the graph
        return []  # Return an empty list
    
    return course_order  # Return the courses

#===== Testing scripts main function section begins
# Follow the instruction below
# DO NOT add any statement outside of main() function

def main():
    # You may add your own testing code within this function while you're
    # working on your assignment;
    # However, please remember to remove them, and re-run this testing script
    # right before you submit your work, in order to ensure your code is
    # free from syntax error
    
    # Test case 1
    relations = [['CSE-11', 'CSE-22'], ['CSE-22', 'CSE-33']]
    output = get_order_of_courses(relations)
    expected_output = ['CSE-11', 'CSE-22', 'CSE-33']
    print("expected_output: ", expected_output)
    print("Your result : ", output)
    if output == expected_output:
        print("test1 passed")
    else:
        print("test1 failed")
    print()
    
    # Test case 2
    relations = [['ART-212', 'ART-232'], ['ART-232', 'HIST-194'], ['HIST-194', 'ART-212']]
    output = get_order_of_courses(relations)
    expected_output = []
    print("expected_output: ", expected_output)
    print("Your result : ", output)
    if output == expected_output:
        print("test2 passed")
    else:
        print("test2 failed")
    print()

if __name__ == "__main__":
    main()
#===== Testing scripts main function section ends

