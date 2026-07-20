class Solution(object):
    def detectCycle(self, head):
        visited = set()
        curr = head
        
        while curr:
            # If we see this node again, it's the start of the cycle
            if curr in visited:
                return curr
            
            visited.add(curr)
            curr = curr.next
            
        return None
