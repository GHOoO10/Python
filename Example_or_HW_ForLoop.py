def Welcome():
    print("*_* --------------------------------------------------------------- *_*")
    print("\tThis is my home work \t- FOR LOOP - \n\tWelcome to Ghamdan Al-Yamani Program ")
    print(":) --------------------------------------------------------------- :( \nLet\'s Go -> \n" )
def end_program():
    print("*_* --------------------------------------------------------------- *_*")
    print("\tThink You For Using My Program  \n\tDone By: Ghamdan Mohammed Al-Yamani  ")
    print(":) --------------------------------------------------------------- :( " )
#GHAMDAN MOHAMMED MOHAMMED AL-YAMANI - GO -
Welcome()

names = input("Enter five names of Offers (Separate names with a comma )=>").split(",")
prices = input("Enter the Offers prices in order (Separate prices with a comma)=>").split(",")

rates = []
accepted_names = []
accepted_prices = []
g = 0
if len(names) != 5 and len(prices) != 5:
    print("the names or prices not = 5  ")
else:
    for n in range(5):
        rate = float(input(f"Enter The rate of '{names[g].title()}' with cost ({prices[g]}) :  "))
        if rate <= 5:
            accepted_names.append(names[g])
            accepted_prices.append(float(prices[g]))
            rates.append(rate)
        g += 1
    winner_cost = min(accepted_prices)
    accepted_offer = accepted_prices.index(winner_cost)

    print("=========================================")
    print(f"All  offers is ({len(names)})")
    print("=========================================")
    print(f"The accepted is ({len(accepted_names)})")
    print(
        f"The winner is {accepted_names[accepted_offer]} with cost {accepted_prices[accepted_offer]}"
        f" and the rate is {rates[ accepted_offer]}")
    

end_program()