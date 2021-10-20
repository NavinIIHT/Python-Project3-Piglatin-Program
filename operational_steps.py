

def count_steps(N):
    if type(N)==type(1):
        steps=0
        if 1<=N<=100000:
            while N!=1:
                if N%2==0:
                    N=N/2
                else:
                    N=N+1
                steps+=1
        else:
            print("Please enter value in the given range")
        return steps
    else:
        raise ValueError("Input value should be integer")


if __name__=="__main__":
    N=int(input("Enter the N (1<=N<=100000)"))
    steps=count_steps(N)
    print("Number of operations are",steps)
