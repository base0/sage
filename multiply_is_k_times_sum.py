var('x k')

for k in range(3,20):
    for n in range(3,30):
        f=k*(x+(x-n))
        g=(x)*(x-n)
        h = g-f

        sol = solve(h==0, x)
        sol = sol[0].rhs()
        try:
            if sol.n() == int(sol.n()):
                print(n, k, sol)
                break
        except:
            pass
            
