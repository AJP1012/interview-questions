import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import numba
import pandas as pd

@numba.njit
def betting(principal, f):
    N = 100
    bankroll = principal
    for i in range(N):
        bet = f * bankroll
        if np.random.rand() > 0.5:
            bankroll += 3 * bet
        else:
            bankroll -= bet
        if bankroll <= 0:
            bankroll = 0
            break

    growth_rate = (bankroll / principal)**(1/N) - 1
    return bankroll , growth_rate

def run_simulations(principal, f, sims):
    outcomes = np.empty(sims)
    growth_rates = np.empty(sims)
    for i in range(sims):
        outcomes[i], growth_rates[i] = betting(principal, f)
    return outcomes, growth_rates

if __name__ == "__main__":

    f_values = [0.125, 0.25, 0.5, 0.75, 1.0]
    principal = 100
    sims = 1000000
    outcomes_total = np.empty(len(f_values))
    growth_rates_total = np.empty(len(f_values))

    for i in range(len(f_values)):
        outcomes, growth_rates = run_simulations(principal, f_values[i], sims)
        outcomes_total[i] = np.sum(outcomes) / sims
        growth_rates_total[i] = np.sum(growth_rates) / sims

    df = pd.DataFrame({
        'Betting Fraction': [str(f) for f in f_values],
        'Average Log Growth Rate': growth_rates_total
    })

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Betting Fraction', y='Average Log Growth Rate', data=df, palette="viridis")
    plt.xlabel("Betting Fraction")
    plt.ylabel("Average Logarithmic Growth Rate")
    plt.title("Average Log Growth Rate vs. Betting Fraction")
    plt.savefig("growth_rates.png", dpi=300, bbox_inches="tight")
    plt.show()