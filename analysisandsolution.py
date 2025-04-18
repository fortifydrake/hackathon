def Model():
  #importing libraries
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  Date=[]
  Description=[]
  Category=[]
  Amount=[]

  #taking necessary inputs
  n=int(input("enter the no. of transaction:"))
  income=float(input("enter your monthly income ;  "))
  for i in range(n):
    date=input("enter the date[mm/dd/yyyy]: ")
    des=input("enter the description:")
    cat=input("enter the category:")
    amt=float(input("enter the amount:"))
    Date.append(date)
    Description.append(des)
    Category.append(cat)
    Amount.append(amt)

  #making dataframe
  df1={
      "Date":Date,
      "Description":Description,
      "Category":Category,
      "Amount":Amount
  }
  df1=pd.DataFrame(df1)
  df1['Date'] = pd.to_datetime(df1['Date'])


  #calculating savings
  Samt=df1['Amount'].sum()
  saving=income-Samt
  print("your saving is",saving)
  sp=(saving/income)*100
  print("you saved",sp)
  
  #gruping data on the basis of category
  df2=df1.groupby(['Category'])['Amount'].sum()
  merge_map = {
    'Food & Dining': ['Alcohol & Bars','Coffee Shops', 'Fast Food', 'Food & Dining', 'Restaurants','Groceries','Cuisine', 'Culinary', 'Gastronomy', 'питание', 'Foodservice', 'Nourishment', 'Refreshments', 'Victuals', 'Provisions', 'Fare', 'Comestibles', 'Edibles', 'Tableware', 'Cookware', 'Cutlery', 'Crockery', 'Condiments', 'Ingredients', 'Recipe', 'Menu', 'Diet', 'Nutrition', 'Beverages', 'Catering', 'Hospitality', 'Appetizers', 'Entrees', 'Main courses', 'Side dishes', 'Desserts', 'Snacks', 'Brunch', 'Buffet', 'A la carte', 'Haute cuisine', 'Comfort food', 'Fusion cuisine', 'Fast food', 'Street food', 'Specialty dishes', 'Regional cuisine', 'Ethnic food', 'Organic food', 'Vegan', 'Vegetarian', 'Gluten-free', 'Raw food', 'Baking', 'Boiling', 'Frying', 'Grilling', 'Roasting', 'Sautéing', 'Steaming', 'Simmering', 'Poaching', 'Braising', 'Stewing', 'Marinating', 'Sous vide', 'Fermenting', 'Curing', 'Pickling', 'Infusion', 'Restaurant', 'Café', 'Bistro', 'Diner', 'Eatery', 'Food court', 'Pizzeria', 'Tavern', 'Pub', 'Bar', 'Lounge', 'Mess hall', 'Canteen', 'Food truck', 'Fast-food chain', 'Fine dining', 'Takeout', 'Delivery', 'Buffet', 'Banquet hall', 'Ambience', 'Service', 'Reservation', 'Table', 'Bill', 'Tip', 'Customer service', 'Dining etiquette', 'Wine pairing', 'Tasting menu', 'Prix fixe', 'All-you-can-eat', 'Happy hour', 'Sunday brunch', 'Chef', 'Cook', 'Waiter/Waitress', 'Bartender', 'Sommelier', 'Host/Hostess', 'Maitre d', 'Food critic', 'Restaurateur'],
    'Utilities': ['Mortgage & Rent', 'Utilities', 'Home Improvement','Electricity', 'Water', 'Sewage', 'Waste Management', 'Internet Service', 'Cable Television', 'Telephone Service', 'Natural Gas', 'Heating Oil', 'Propane', 'Trash Collection', 'Recycling Services', 'Sanitation', 'Public Utilities', 'Energy', 'Fuel', 'Broadband', 'Telecom',],
    'Transportation': ['Gas & Fuel', 'Auto Insurance','Car', 'Bus', 'Train', 'Airplane', 'Taxi', 'Uber', 'Lyft', 'Subway', 'Metro', 'Vehicle', 'Automobile', 'Motorcycle', 'Bicycle', 'Scooter', 'Truck', 'Ferry', 'Boat', 'Ship', 'Flight', 'Journey', 'Commute', 'Travel', 'Transit', 'Transportation', 'Public Transportation', 'Private Transportation', 'Mass Transit', 'Rail Transport', 'Road Transport', 'Air Transport', 'Water Transport', 'Freight Transport', 'Passenger Transport', 'Logistics', 'Navigation', 'Traffic', 'Roads', 'Highways', 'Streets', 'Bridges', 'Tunnels', 'Airports', 'Stations', 'Ports', 'Terminals', 'Parking', 'Toll', 'Fuel', 'Gasoline', 'Diesel', 'Electricity', 'EV Charging', 'Maintenance', 'Repair', 'Service', 'Insurance', 'Registration', 'License', 'Permit', 'Ticket', 'Fare', 'Schedule', 'Timetable', 'Route', 'Direction', 'Map', 'GPS', 'Navigation System', 'Traffic Jam', 'Congestion', 'Rush Hour', 'Accident', 'Safety', 'Regulations', 'Emissions', 'Carbon Footprint', 'Sustainable Transport', 'Public Transit', 'Ridesharing', 'Carpooling', 'Bike Sharing', 'E-scooter Sharing', 'Autonomous Vehicles', 'Self-driving Cars', 'Electric Vehicles', 'Hybrid Vehicles', 'Fuel Efficiency', 'Mileage', 'Infrastructure', 'Urban Planning', 'Accessibility', 'Mobility', 'Connectivity', 'Logistics', 'Supply Chain', 'Distribution', 'Shipping', 'Hauling', 'Dispatch', 'Delivery', 'Cargo', 'Freight', 'Goods', 'Commodities'],
    'Entertainment': ['Music', 'Movies & DVDs', 'Television', 'Entertainment','Internet', 'Mobile Phone','Modern Dance', 'Hobbies', 'PC Games', 'Stand-up Comedy', 'Amusement Parks', 'Television', 'Reading', 'Super Bowl', 'Orchestra', 'Culture', 'Blues', 'Pastimes', 'Jazz', 'World Cup', 'Crafts', 'Opera', 'Online Videos', 'College Sports', 'Leisure', 'Musicals', 'Painting', 'Rock Music', 'Cartoons', 'Plays', 'Entertainment Industry', 'Sitcoms', 'Radio', 'Theme Parks', 'Mobile Phone', 'Dramas', 'Mobile Games', 'NBA Finals', 'Video Games', 'Theater', 'Arcades', 'Museum Exhibitions', 'Console Games', 'Improv Comedy', 'Electronic Music', 'Off-Broadway', 'Talk Shows', 'Internet', 'Sports', 'Gaming', 'Documentaries', 'Comedy', 'Music', 'Art Exhibitions', 'Dance Competitions', 'DJ', 'Movies', 'Streaming', 'Folk Music', 'Social Media', 'Online Games', 'Live Music', 'Dance Performances', 'E-sports', 'Music Festivals', 'Competitive Sports', 'Arts', 'Fun', 'Virtual Reality', 'Cultural Festivals', 'Blockbusters', 'Concerts', 'Photography', 'Festivals', 'Sculpture', 'Classical Music', 'Anime', 'Enjoyment', 'Podcasts', 'Film Festivals', 'News', 'Augmented Reality', 'Hip Hop', 'Indie Films', 'Broadway', 'Spectator Sports', 'Media', 'Reality TV', 'Sketch Comedy', 'Exhibitions', 'Writing', 'Professional Sports', 'Comedy Clubs', 'Web Series', 'Ballet', 'Cinema', 'Country Music', 'Folk Dance', 'Olympics', 'Dance', 'Recreation', 'Pop Music'],
    'Debt Payment': ['Credit Card Payment','Student Loan Payment', 'Auto Loan Payment', 'Debit Card Payment','Medical Debt Payment', 'линии кредита', 'Alimony Payment', 'Overdue Utility Bills', 'Tax Debt Payment', 'Rent Payment', 'Personal Loan Payment', 'Payday Loan Payment', 'Balance Transfer Payment', 'Debt Consolidation Loan Payment', 'Title Loan Payment', 'Home Equity Line of Credit (HELOC) Payment', 'Legal Debt Payment', 'Home Equity Loan Payment', 'Installment Loan Payment', 'Child Support Payment', 'Mortgage Payment', 'Business Loan Payment'],
    'Others': ['Shopping','Haircut','Cash Payment', 'Check Payment', 'Electronic Funds Transfer (EFT)', 'Direct Deposit', 'Online Payment', 'Mobile Payment', 'Wire Transfer', 'Money Order', "Traveler's Check", 'Cryptocurrency Payment', 'Payment by Barter', 'Payment in Kind', 'Escrow Payment', 'Insurance Premium Payment', 'Retirement Contribution', 'Royalty Payment', 'Subscription Payment', 'Donation', 'Grant Payment', 'Invoice Payment', 'Reimbursement', 'Settlement Payment', 'Pension Payment', 'Annuity Payment', 'Deferred Payment', 'Partial Payment', 'Advance Payment', 'Recurring Payment', 'Installment Payment', 'Lump Sum Payment', 'Final Payment', 'Overpayment', 'Underpayment', 'Prepayment', 'Postpayment', 'Back Payment', 'Retroactive Payment', 'Severance Pay', 'Bonus Payment', 'Commission Payment', 'Salary Payment', 'Wage Payment', 'Stipend Payment', 'Fee Payment', 'Tithe', 'Offering', 'Tribute']
  }
  grouped_data = []
  grouped_categories = set()

  for new_cat, old_cats in merge_map.items():
    amount_sum = df2[df2.index.isin(old_cats)].sum()
    grouped_data.append((new_cat, amount_sum))
    grouped_categories.update(old_cats)
  ungrouped = df2[~df2.index.isin(grouped_categories)]
  for i, row in ungrouped.items():
    grouped_data.append((i, row))
  merged_df = pd.DataFrame(grouped_data, columns=['Category', 'Amount'])
  merged_df = merged_df.sort_values(by='Amount', ascending=False)

  categories = merged_df['Category']
  amounts = merged_df['Amount']


  #showing analysis
  #pie chart(amount vs category)
  plt.figure(figsize=(6, 6))
  plt.pie(
    amounts,
    labels=categories,
    autopct='%1.1f%%',
    startangle=140,
    wedgeprops={'edgecolor': 'white'}
  )

  plt.title("Spending Breakdown by Category")
  plt.axis('equal')
  plt.show()
  
  #graph(amount vs date)
  # Add a new 'Month' column in the dataframe using full month names
  df1['Month'] = df1['Date'].dt.strftime('%B')
  df1 = df1.sort_values('Date')
  plt.figure(figsize=(12, 6))
  plt.plot(df1['Month'], df1['Amount'], marker='o', linestyle='-', alpha=0.7)
  plt.title('Amount vs Month')
  plt.xlabel('Month')
  plt.ylabel('Amount')
  plt.grid(True)
  plt.tight_layout()
  plt.xticks(rotation=45)
  plt.show()

  #bars(Amount vs Month)
  plt.figure(figsize=(10,10))
  plt.bar(df1.Month,df1.Amount)
  plt.show()
  #showing where the expenditure is focused on and giving their solution
  max_row_index = merged_df['Amount'].idxmax()
  max_category = merged_df.loc[max_row_index, 'Category']
  max_amount = merged_df['Amount'].max()



  if max_category == 'Paycheck':
    print("your expense on paycheck is highest by ",max_amount,""".So try to control it by doing following things
       1. Check if Payroll Is Sustainable
      If payroll (salaries) takes up a large chunk of your total expenses or income:

      Review: Is your team scaled correctly?

      Use this rough rule: Payroll should usually be 30–50% of business revenue depending on the industry.

      If it’s too high: consider outsourcing, automating, or optimizing team structure.

      2. Track ROI on Team Members
      Not every expense = investment. Ask:

      Is each role directly or indirectly adding value?

      For sales roles: Are they bringing in more than they cost?

      For support/admin: Are they saving you time or increasing efficiency?

      3. Avoid Over-Hiring Early
    Especially for startups or small businesses:

      Don’t overstaff just to “look big.”

      Start lean, then scale up as needed.

      Consider freelancers or contractors for flexible costs.

      4. Use Payroll Software or Services
      Paying high salaries means you’re managing a team. Use tools to:

    Automate payslips, tax calculations, PF/ESI/TDS compliance (India-specific)

      Track hours, bonuses, and leave

    Examples: Zoho Payroll, QuickBooks, Gusto, Keka

      5. Budget for Benefits and Bonuses
      Beyond salary, remember to account for:

      Annual bonuses

      Insurance and perks

      Appraisals or raises

    Budgeting for this ahead keeps you from running short at year-end.

      6. Plan for Taxes (Both Sides)
      If you're the employer:

      Factor in employer’s share of taxes/benefits.

      Offer tax-efficient salary structures to employees (meal cards, health benefits, allowances).

      Ensure compliance with labor laws, PF, ESI, TDS.

    7. Build an Emergency Buffer
      Imagine a slow month or bad quarter — can you still pay salaries?

      Keep 3–6 months of payroll expenses in a separate emergency fund.

      It protects your team and your reputation during tough times.

      8. Invest in Team Growth — Wisely
    Paying well is great. But also:

    Invest in training, performance tools, wellbeing.

      Encourage output-driven culture: pay more where it matters, not just to keep people. """)
  elif max_category == 'Utilities':
    print("your expense on Utilities is highest by ",max_row_index,""". So try to control it by doing following things
  ⚡ 1. Audit Your Bills
Go through the last 3–6 months of bills.

Look for sudden spikes or patterns — maybe a device, appliance, or habit is draining more than you think.

🔍 2. Identify Utility Hogs
Electricity: ACs, geysers, old fridges, washing machines, heaters, and gaming setups can eat up power.

Water: Leaky taps, running toilets, long showers.

Gas: Overuse in kitchens, especially old burners.

🧠 3. Change Usage Habits
Turn off appliances completely (not standby mode).

Run heavy appliances (like washing machines) during off-peak hours if your provider charges time-based rates.

Lower geyser temp to 50–55°C — saves energy.

Use ceiling fans instead of AC when possible.

💡 4. Switch to Energy-Efficient Appliances
Look for 5-star rated appliances (BEE certified in India).

LED bulbs instead of CFL or halogen — they use 80% less energy.

Smart plugs or timers for devices like geysers.

💸 5. Negotiate or Switch Providers (if possible)
Internet or cable bills: Call and ask for lower plans or discounts.

In deregulated electricity/gas markets (like some US/UK regions), you can compare and switch suppliers.

🧾 6. Use Smart Meters or Monitors
Devices like Wattmeters or smart plugs can show real-time consumption.

Some energy companies offer detailed usage reports—ask them for insights.

💧 7. Water Saving Tips
Install aerators on taps.

Fix leaks quickly.

Use dual-flush toilets or a bottle trick in the cistern to reduce water per flush.

🧊 8. AC Optimization
Set the temp between 24°C–26°C — energy efficient and still comfortable.

Use curtains/blinds to block sunlight during peak heat.

Clean AC filters monthly — it reduces power draw significantly.

💼 Bonus: Claim Tax Rebates (if business use)
If the utilities are partly for a home office or business, you may be able to claim deductions or write-offs on your tax return.""")
  elif max_category == 'Transportation':
    print("your expense on Transportation is highest by ",max_row_index,""". So try to control it by doing following things
  🔍 1. Track What’s Driving the Cost
Break it down:

Fuel

Maintenance/repairs

Car loan/EMI

Insurance

Tolls & parking

Ride-hailing (Uber/Ola)

Public transport

You can’t fix what you haven’t measured.

⛽ 2. Cut Down on Fuel Expenses
Drive smarter: Gentle acceleration and maintaining steady speed saves fuel.

Avoid idling: Wastes fuel quickly (especially with AC on).

Check tire pressure: Under-inflated tires reduce mileage.

Carpool or ride-share: Even a few days a week helps.

Use fuel rewards apps or credit cards to save.

🚘 3. Consider Downsizing the Vehicle
If you drive solo but own a big car/SUV, switching to a smaller vehicle can:

Save on fuel

Lower insurance

Cost less to maintain

🛞 4. Optimize Maintenance
Stick to the manufacturer-recommended schedule.

Don’t get upsold at service centers — always check what’s actually needed.

Use local trusted mechanics vs. dealerships if out of warranty.

💳 5. Evaluate Ownership vs. Alternatives
If you rarely drive, it might be cheaper to:

Use Uber/Ola occasionally

Rent a vehicle when needed

Use a bike/scooter subscription service

Monthly car ownership costs can exceed ₹15,000–₹20,000 when you include EMI, insurance, fuel, maintenance.

🚲 6. Use Alternative Transport (When Possible)
Public transport (metro, bus) saves thousands monthly.

E-bikes or cycles for short trips: one-time cost, zero fuel.

Walking short distances adds steps and saves cash.

📱 7. Use Tech to Your Advantage
Google Maps shows real-time traffic & alternate routes.

Apps like Fuelio or Drivvo help track fuel efficiency.

Ride-share apps sometimes have subscriptions (e.g., Uber Pass) to lower regular fare costs.

🚦 8. Re-evaluate Commute
If you're commuting long distances daily:

Can you move closer to work?

Explore remote/hybrid work options if your job allows.

Try carpooling groups (many companies support it internally).

Bonus: Tax Deductions (for business use)
If you’re self-employed or using your vehicle for work, part of your fuel and maintenance can be tax deductible (check with a tax advisor).

""")
  elif max_category == "Entertainment":
    print("your expense on Entertainment is highest by ",max_row_index,""". So try to control it by doing following things
  📊 1. Audit All Entertainment Spending
Go through your bank and wallet:

Streaming services (Netflix, Prime, Disney+, etc.)

Subscriptions (Spotify, Xbox Live, Book clubs)

Dining out, movies, concerts, events

In-app purchases, games

Weekend getaways

You’ll be shocked how much you’re spending for things you’ve forgotten about.

💡 2. Set a Fun Budget (and Stick to It)
Use the 50/30/20 rule:

30% of your income is for "wants" — entertainment falls here.

Set a monthly cap — say ₹4,000 or ₹5,000 — and spend freely within that.

Use budgeting apps like:

Walnut, Money Manager, YNAB, or even a Google Sheet

🔄 3. Rotate or Share Subscriptions
No one needs 6 streaming platforms at once — rotate monthly.

Share family plans with friends or family (most allow it legally).

Cancel the ones you haven’t used in the last 30 days.

🍿 4. Free & Low-Cost Alternatives
Use public events, free concerts, or community programs.

Watch parties with friends (instead of each person subscribing).

YouTube has amazing free content for all interests.

🍴 5. Cut Down on Overpriced Outings
Skip ₹500 popcorn at the theater — go after eating or bring your own snacks.

Limit weekend parties or dinners out to 2x a month.

Explore free or low-cost spots: lakes, hikes, art galleries, or cafes with free events.

🎮 6. Gaming & Hobbies? Budget it too
If gaming or a hobby is your jam — no shame!

Just assign a specific monthly budget: “₹2,000 for gaming-related stuff” and track it.

🔁 7. Cash or Prepaid Cards Trick
Withdraw your entertainment budget in cash — once it’s gone, you stop. Or use a prepaid card with ₹X loaded monthly just for fun stuff.

📅 8. Delay Before Spending
Use the 24-hour rule: wait a day before buying any non-urgent entertainment item (game, concert ticket, fancy dinner). You’ll skip a lot of impulse buys.

Bonus: Make Entertainment Productive Too
Try hobbies that are both fun and skill-building: music, painting, creative writing, coding games, editing videos, etc.

Some hobbies can even earn money later.

""")
  elif max_category == "Debt Payment":
   print("your expense on Debt payment is highest by ",max_row_index,""". So try to control it by doing following things

📊 1. Know Your Total Debt Load
Make a quick list:

Type of debt (credit card, personal loan, car, education, etc.)

Outstanding amount

Monthly payment

Interest rate

This shows which debt is the most dangerous and which can be tackled fast.

🚨 2. Prioritize High-Interest Debt
Credit cards usually have 30–40% interest 😱 — these should be your top target.

Choose a strategy:

🧊 Avalanche Method (Best for saving money):
Pay off the highest interest rate debt first.

Saves the most money long-term.

🧱 Snowball Method (Best for motivation):
Pay off the smallest balance first.

Creates quick wins and momentum.

💳 3. Stop Adding More Debt
Freeze credit card usage until balances are paid down.

Avoid new loans — especially BNPL (Buy Now, Pay Later).

Delay big purchases unless essential.

🧠 4. Consider Debt Consolidation
Merge multiple debts into one lower-interest loan, like a personal loan or balance transfer credit card.

Benefits:

One payment instead of five

Lower monthly burden

Less mental stress

But: only works if you stop using the old credit lines.

🏦 5. Negotiate with Lenders
Don’t be afraid to:

Ask for a lower interest rate (especially if you’ve been paying on time).

Restructure the loan to extend term (lower monthly EMI, though total interest increases).

Consider settlement (only if you’re truly unable to pay, and accept a credit score dip).

🧾 6. Build a Debt Repayment Plan
Break your income like this (until you're in the clear):

50% Essentials

30–40% Debt Payments

10–20% Emergency Fund + Needs

If debt takes more than 40–50% of your income, it’s time to make bigger moves (e.g., downsizing expenses, side income).

💸 7. Boost Repayment with Side Hustles
Even ₹5,000–₹10,000/month extra can slash your repayment timeline.

Freelance, tutoring, delivery, online tasks — short-term hustle can create long-term freedom.

🧯 8. Emergency Fund = Safety Net
It sounds backwards, but building a small emergency fund (₹5,000–₹10,000) can prevent falling back into debt every time something unexpected pops up.

📈 Bonus: Track Progress — Celebrate Wins
Use a tracker to watch your balance drop. Every ₹1,000 closer to freedom is a win. It makes the process less depressing and more empowering.""")
  elif max_category == "Others":
   print("your expense on other expenses is highest by ",max_row_index,""". So try to control it by doing following things
  🧾 1. Define What "Other" Actually Means
This is usually a catch-all bucket that includes:

Gifts (weddings, birthdays)

Tips

Donations

Subscriptions you forgot about

Pet costs

Office/home supplies

One-time emergency purchases

Fines or late fees 😬

Start by reviewing your last 2–3 months of expenses and list what’s hiding under “Other.”

💡 2. Create Mini-Categories
Split “Other” into smaller, meaningful groups like:

🎁 Gifts & Celebrations

🐶 Pet Expenses

🛠 Repairs & Misc

💳 Fees/Fines

🤷‍♂️ Random (One-Time Stuff)

This gives you clarity on which kind of “Other” is being wasteful.

📉 3. Cap It — Set a Monthly Limit
Decide how much you're okay spending on non-essential, unpredictable stuff.

For example:

“I’ll allow ₹1,000/month max for random stuff.”

Anything above that, you defer or find alternatives.

💳 4. Watch Out for Auto-Charges
This includes:

App subscriptions

Membership renewals

Annual charges These often fall into “Other” because they happen quietly in the background.

Check bank and credit card statements — cancel anything you forgot you were paying for.

⚠️ 5. Delay Non-Urgent One-Offs
See something random you want to buy? Use the 24–48 hour rule:

Wait a day or two — if you still want it, go for it.

Often, the “want” fades and you save money.

📊 6. Track & Review Monthly
Add a simple "Other" tracking section to your budget:

plaintext
Copy
Edit
Month: April
Gifts – ₹500
Fixing broken fan – ₹750
Pet food – ₹1,200
Random Amazon buy – ₹800
TOTAL: ₹3,250
This shows you where to cut back next month.

💵 7. Build a "Misc Fund"
Instead of letting “Other” surprise you, create a separate bucket:

Call it “Flex Fund” or “Buffer Fund.”

Put ₹1,000–₹2,000/month into it.

It acts like a personal safety net for unplanned, weird stuff.

🧘‍♂️ Bonus: Forgive Yourself for One-Offs
Not every “other” expense is bad — some are life things:

Last-minute gift for a loved one

A surprise event

Emergency home fix

Just don’t let it be a habit — plan for it.""")
  elif max_category == "Food & Dining":
    print("your expense on Food &Dinng expenses is highest by ",max_row_index,""". So try to control it by doing following things
  📊 1. Split Food Into 2 Buckets
Break it down:

🍲 Groceries – Necessary, cheaper per meal

🍕 Eating Out / Ordering In – Fun, but adds up FAST

Now track both. You might find you're spending more at Swiggy/Zomato than at your grocery store. 💸

💡 2. Set a Monthly Food Budget
Figure out your safe spending zone:

Groceries: 10–15% of income

Dining out/Ordering: 5–8% max

If you make ₹30,000, aim for:

₹3,000–₹4,000 groceries

₹1,500–₹2,000 on takeout

Use apps or a basic Excel sheet to track this weekly.

🥡 3. Cut Down on Takeout (Without Going Cold Turkey)
Here’s how:

Limit ordering to once or twice a week, not daily

Use restaurant coupons or cards with cashback

Choose pickup instead of delivery to avoid delivery & service charges

Share meals or buy combos instead of individual orders

🧑‍🍳 4. Batch Cook or Meal Prep
Cooking once for 2–3 days saves:

Time ⏱️

Money 💸

Decision fatigue 🧠

Keep simple go-to meals that you like. Even basic rice + dal + sabzi or sandwiches can save tons.

🛒 5. Shop Smart for Groceries
Make a list & stick to it (impulse buys kill your budget)

Buy in bulk for staples (rice, dal, oil)

Choose local markets or discount stores

Avoid “fancy” imported items unless it’s a treat

Also: compare online grocery deals — sometimes BigBasket, Blinkit, or DMart Ready has crazy discounts.

👨‍👩‍👧 6. Eat Out Less, Eat Together More
Invite friends over for potluck or house dinners. Costs way less than going out — and you still get the social joy.

📱 7. Track It with an App or Simple Table
Example:


Date	Type	Amount	Notes
Apr 3	Grocery	₹1,200	Monthly veg & rice
Apr 6	Zomato	₹560	Pizza night 🍕
Apr 8	Grocery	₹900	Fruits & milk
Apr 10	Café visit	₹300	Coffee & muffin ☕
By the end of the month, you'll spot what’s draining you.

Bonus: DIY Treats Save Big
Craving something fancy? Try:

Homemade iced coffee instead of Starbucks

DIY burgers/pasta

Make popcorn + movie night at home = same fun, less ₹₹₹""")


  print("\tTHANK YOU FOR VISITING US\t")
