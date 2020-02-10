from nsimulator import nsimulator

nsim = nsimulator(1)

nsim.set_Ie(0, 0)

nsim.set_mpotential(0, 0)

nsim.animate_integration(0.2, 200, [0])