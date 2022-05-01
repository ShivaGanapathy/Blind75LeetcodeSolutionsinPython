class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Initialize the priority queue used for Dijkstra's
        heap = []
        heappush(heap, (0, k))
        # Set up an adjacency map representation of the given graph
        hashmap = {}
   
        for edge in times:
            if edge[0] not in hashmap:
                hashmap[edge[0]] = []
            
            hashmap[edge[0]].append((edge[1], edge[2]))
            
        # Make a set to keep track of the visited vertices
        visited = set()
        
        # Create a variable that keeps track of each the cost to get to the most recently visited vertex
        latest_cost = 0
        
        # While there are still paths to a vertex
        while heap:
            
            # Pop from the heap to find the cost to get to the current vertex and the vertex itself
            this_cost, node = heappop(heap)
            
            # Set the cost of the latest visited vertex to this vertex's cost
            latest_cost = this_cost
            
            # Now that we are exploring this node, we can mark it as visited
            visited.add(node)
                
            # If we have already explored all the vertices in the graph, we are done
            if len(visited) == n:
                break
                
            # Iterate through all outgoing edges from the current vertex
            for outgoing_edge in hashmap.get(node, []):
                end_node = outgoing_edge[0]
                edge_cost = outgoing_edge[1]
                
                # If there is an outgoing edge to a node we haven't visited yet
                if end_node not in visited:
                    # Push the new edge and edge weight to the heap
                    heappush(heap, (this_cost + edge_cost, end_node))
                    
                    
        # Return the final computed value, or -1 if we couldn't reach every vertex in the graph
        return latest_cost if len(visited) == n else -1
                
            
            
            
