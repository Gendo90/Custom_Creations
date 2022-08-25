# Enter your code here. Read input from STDIN. Print output to STDOUT

# n = int(input())
# x_input = [a for a in input().split(" ") if not a == '\r']
# y_input = [a for a in input().split(" ") if not a == '\r']


# calculates the correlation between two different sets of data
# if the standard dev. is zero for either dataset, default result is 0 (not correlated)
def calcCorr(x_arr, y_arr, n):

    # confirm data is in the correct format
    x = [float(a) for a in x_arr]
    y = [float(a) for a in y_arr]

    #calc means of x and y
    u_x = sum(x)/n
    u_y = sum(y)/n

    x_diff_squared = [(a - u_x)**2 for a in x]
    y_diff_squared = [(a - u_y)**2 for a in y]

    st_dev_x = (sum(x_diff_squared)/n)**0.5
    st_dev_y = (sum(y_diff_squared)/n)**0.5

    r_numerator = [(x[i] - u_x)*(y[i] - u_y) for i in range(n)]

    # st_dev should have a non-zero value for to prevent a "divide by zero error"
    # when calculating r
    if(st_dev_y == 0 or st_dev_x == 0):
        return 0
    r = sum(r_numerator)/(n*st_dev_x*st_dev_y)

    return r
