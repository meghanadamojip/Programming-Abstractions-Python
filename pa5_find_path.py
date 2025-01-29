def find_paths(connection: List[List[int]], source: int, destination: int) ->
List[List[int]]:
connections_list = {} #create list of connections for efficiency
for u, v in connection: #iterate through connections
#add v to the list of neighbors of the node u in the list
if u not in connections_list:
connections_list[u] = []
connections_list[u].append(v) #append v
# depth first search to find all paths from source to destination
all_possibilities = [] #all possible paths
stack = [(source, [source])] #stack for the sources and all its destinations
while stack:
node, path = stack.pop() #if stack is not empty, then pop a node and its
path
if node == destination:
all_possibilities.append(path)
else:
if node in connections_list: #if it's in the destination then add the
path
for next in connections_list[node]:
if next not in path:
stack.append((next, path + [next])) #if not add all nodes
to the stack
return all_possibilities #return paths
#===== Your implementation ends here
#===== Problem B function ends
#===== Testing scripts main function section begins
# follow the instruction below
# DO NOT add any statement outside of main() function
def main():
# you may add your own testing code within this function while you're
# working on your assignment;
# however, please remember to remove them, and re-run this testing script
# right before you submit your work, in order to ensure your code is
# free from syntax error
connection = [[0,1],[0,4],[1,2],[2,3],[3,4]]
expected_output = []
source, destination = 2, 1
output = find_paths(connection, source, destination)
expected_set = set(tuple(path) for path in expected_output)
output_set = set(tuple(path) for path in output)
print("expected_output: ", expected_output)
print("Your result : ", output)
if output == expected_output:
print("test1 passed")
else:
print("test1 failed")
print()
connection = [[0,1],[1,2],[1,3],[1,5],[2,3],[2,4],[3,4],[4,5],[0,5]]
expected_output = [[1,2,3,4,5], [1,2,4,5], [1,3,4,5], [1,5]]
source, destination = 1, 5
output = find_paths(connection, source, destination)
expected_set = set(tuple(path) for path in expected_output)
output_set = set(tuple(path) for path in output)
print("expected_output: ", expected_output)
print("Your result : ", output)
if output_set == expected_set:
print("test2 passed")
else:
print("test2 failed")
print()
if __name__ == "__main__":
main()
