import primer as pr

@pr.clock
def new_func():
    for i in range(5):
        print(i)

if __name__=='__main__':
    print(pr.func_wrap)
    print(pr.func_clock)
