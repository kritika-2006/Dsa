class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the closest x and y coordinates on the rectangle to the circle's center
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate the distance from the closest point to the circle's center
        distance_x = xCenter - closest_x
        distance_y = yCenter - closest_y
        
        # Check if the distance is less than or equal to the radius squared
        return (distance_x ** 2 + distance_y ** 2) <= (radius ** 2)