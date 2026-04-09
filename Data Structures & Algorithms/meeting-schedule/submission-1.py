"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for i in range(0,len(intervals)-1):
            cur = intervals[i]
            next1 = intervals[i+1]
            if(cur.end>next1.start):
                return False
        return True