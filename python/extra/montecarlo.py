########################## COFFEES ##########################

coffees_ = interactive(mc_normal_hist,
                        mean=(500,600,1),
                        std_dev=(50,80,1),
                        samples=(4000,6000,1),
                        bins=(200,300,1),
                        title='coffees_sim',
                        color='green',
                        );
display(coffees_)

##########################  BREACKFAST  #####################

breakfasts_ = interactive(mc_normal_hist,
                        mean=(200,400,1),
                        std_dev=(25,50,1),
                        samples=(4000,6000,1),
                        bins=(200,300,1),
                        title='breakfasts_sim',
                        color='green',
                        );
display(breakfasts_)

###########################  SNACKS  ########################

snacks_ = interactive(mc_normal_hist,
                        mean=(100,180,1),
                        std_dev=(18,40,1),
                        samples=(4000,6000,1),
                        bins=(200,300,1),
                        title='snacks_sim',
                        color='green',
                        );
display(snacks_)

###########################  BEVERAGES  ########################

beverages_ = interactive(mc_normal_hist,
                        mean=(100,180,1),
                        std_dev=(18,40,1),
                        samples=(4000,6000,1),
                        bins=(200,300,1),
                        title='beverages_sim',
                        color='green',
                        );
display(beverages_)


fixedCosts = 374000
costOfCapital = 0.15
investment = 120000

coffeePrice = 1
coffeeCM = 0.82
breakfastPrice = 2.2
breakfastCM = 0.80
snackPrice = 3.5
snackCM = 0.65
beveragePrice = 2
beverageCM = 0.70

coffees = coffees_.result
breakfasts = breakfasts_.result
snacks = snacks_.result
beverages = beverages_.result
################################################
dailyTickets = coffees + breakfasts + snacks + beverages
dailyRevenue = coffees * coffeePrice + breakfasts * breakfastPrice + snacks * snackPrice + beverages * beveragePrice
dailyIncome  = coffees * coffeePrice * coffeeCM + breakfasts * breakfastPrice * breakfastCM + snacks * snackPrice * snackCM + beverages * beveragePrice * beverageCM

plot_hist(dailyTickets,'Daily Tickets','blue')
test(dailyTickets)

plot_hist(dailyRevenue,'Daily Revenue','blue')
test(dailyRevenue)

plot_hist(dailyIncome,'Daily Income','blue')
test(dailyIncome)

days = 310

yearlyTickets = dailyTickets * days
yearlyRevenues = dailyRevenue * days
yearlyOperatingIncome = dailyIncome * days


plot_hist(yearlyTickets,'Yearly Tickets','red')
test(yearlyTickets)

plot_hist(yearlyRevenues,'Yearly Revenue','red')
test(yearlyRevenues)

plot_hist(yearlyOperatingIncome,'Yearly Income','red')
test(yearlyOperatingIncome)

fixedCosts = 374000
investment = 120000

yearlyNetIncome = yearlyOperatingIncome - fixedCosts
roi = yearlyNetIncome / investment * 100
roi

print("Investment      : ", round(investment,2),                    "€")
print("Daily tickets   : ", round(dailyTickets.mean(),0),          "tickets")
print("Revenues        : ", round(yearlyRevenues.mean(),2),        "€")
print("Operating Income: ", round(yearlyOperatingIncome.mean(),2), "€")
print("Fixed cost      : ", round(fixedCosts,2),                    "€")
print("Net Income      : ", round(yearlyNetIncome.mean(),2),       "€")
print("ROI             : ", round(roi.mean(),2),                   "%")