day_data = ["1st", "2nd", "3rd", "4th", '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th',
       '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th',
       "30th", "31st"]

month_data = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

class Solution:
    def reformatDate(self, date: str) -> str:

        format = date.split()
        day = day_data.index(format[-3])+1
        month = month_data.index(format[-2])+1
        year = format[-1]
        return f"{year}-{'' if month >= 10 else 0}{month}-{'' if day >= 10 else 0}{day}"

if __name__ == '__main__':
    b = "20th Feb 2052"
    a = Solution()
    print(a.reformatDate(b))
