class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Helper function to convert "MM-DD" to day of the year
        def convert_to_days(date_str: str) -> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            total_days = day
            for m in range(month - 1):
                total_days += days_in_months[m]
            return total_days
        
        alice_start = convert_to_days(arriveAlice)
        alice_end = convert_to_days(leaveAlice)
        bob_start = convert_to_days(arriveBob)
        bob_end = convert_to_days(leaveBob)
        
        # Find the overlapping period
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)
        
        # Calculate the number of days spent together (inclusive)
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        
        return 0