# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and
# top right corner as shown in the figure.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        total = (C - A) * (D - B) + (G - E) * (H - F)
        if E >= C or G <= A or B >= H or D <= F:
            return total
        h = min(C, G) - max(A, E)
        v = min(D, H) - max(B, F)
        area = h * v
        return total - area
