var('x k')

for k in range(3,1000):
    for n in range(3,1000):
        f=k*(x+(x-n))
        g=(x)*(x-n)
        h = g-f

        sol = solve(h==0,x)
        sol = sol[0].rhs()
        try:
            if sol.n() == int(sol.n()):
                print(sol, n,k)
                break
        except:
            pass
            
