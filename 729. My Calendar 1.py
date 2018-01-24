class MyCalendar(object):

    def __init__(self):
        self.arr=[]
        # self.end_arr=[]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if (not self.arr):
            self.arr.append(tuple((start, end)))
            # self.end_arr.append(end)
            return True
        for i, j in self.arr:
            if (i < end and start < j):
                return False
        self.arr.append(tuple((start, end)))
        return True
        # if(not self.start_arr and not self.end_arr):
        #     self.start_arr.append(start)
        #     self.end_arr.append(end)
        #     return True
        # for i,j in zip(self.start_arr,self.end_arr):
        #     if ((start<=i and end<=i) or (start>=j and end>=j)):
        #         self.start_arr.append(start)
        #         self.end_arr.append(end)
        #         return True
        # return False
temp=MyCalendar()
# for i,j in [(10,20),(15,25),(20,30)]:
for i,j in [(47,50),(33,41),(39,45),(33,42),(25,32),(26,35),(19,25),(3,8),(8,13),(18,27)]:
    print(temp.book(i,j))