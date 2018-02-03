# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary that
#  has the smallest lexical order when read as a single string. For example,
# the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#  But it is larger in lexical order.

from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        ticket_map = defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            print a, b
            ticket_map[a] += b,
        route = []

        def visit(airport):
            while ticket_map[airport]:
                visit(ticket_map[airport].pop())
            route.append(airport)
            print route
        visit('JFk')
        return route[::-1]

    def findItinerary1(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            print a, b
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            print route

        visit('JFK')
        return route[::-1]


if __name__ == '__main__':
    s =Solution()
    print s.findItinerary1([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])

class Solution1():
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]