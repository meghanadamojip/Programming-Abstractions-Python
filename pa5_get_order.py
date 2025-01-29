def get_order_of_courses(relationships: List[List[str]]) -> List[str]:
#create two dictionaries
connections = {} #keeping track of the number of connections each node has
graph = {} #the node graph
# build the graph and connections
for relationship in relationships: #iterate through the input
prereq, course = relationship #look for prereq and course to add to the
graph
if prereq not in graph:
graph[prereq] = set()
if course not in graph:
graph[course] = set()
#keeps track of how many prereqs each course has
graph[prereq].add(course)
connections[course] = connections.get(course, 0) + 1 #increment course node
# get all the nodes with 0 indegrees and add them to the queue
no_prereqs = [] #classes with no prereqs (is a queue)
for node in graph:
if node not in connections:
no_prereqs.append(node) #append courses with no prereqs
# topological sorting
course_order = []
while no_prereqs:
node = no_prereqs.pop(0) #if node is in the queue
course_order.append(node) #add to list
for next in graph[node]:
connections[next] -= 1 #take away from the node
if connections[next] == 0: #if node is 0 then add to the queue
no_prereqs.append(next)
if len(course_order) != len(graph): #if length of list is not equal to the
nodes in the graph
return [] #return an empty list
return course_order #return the courses
#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main():
# you may add your own testing code within this function while you're
# working on your assignment;
# however, please remember to remove them, and re-run this testing script
# right before you submit your work, in order to ensure your code is
# free from syntax error
# test case 1
relations = [['CSE-11','CSE-22'],['CSE-22','CSE-33']]
output = get_order_of_courses(relations)
expected_output = ['CSE-11', 'CSE-22', 'CSE-33']
print("expected_output: ", expected_output)
print("Your result : ", output)
if output == expected_output:
print("test1 passed")
else:
print("test1 failed")
print()
# test case 2
relations = [['ART-212','ART-232'],['ART-232','HIST-194'],['HIST-194','ART-212']]
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
