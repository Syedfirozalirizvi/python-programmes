#  Pattren Loops Programme.


class Loops:

    def pattern(self):

        for rows in range(0,10):
            for columns in range(1,rows):
                print(" ",end = "")
                print('*',end = "")
            print()

# Using Another Loops .

        for lower_rows in range(10,0,-1):
            for lower_columns in range(1,lower_rows):
                    print(" ",end = "")
                    print('*',end = "")
            print()

obj = Loops()
obj . pattern()  