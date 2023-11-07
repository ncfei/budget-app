# Code written by Chooi Fei Ng
class Category:

    def __init__(self,name):
        # Initialise name of the class, ledger and balance
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self,amount,description=""):
        # Deposit an amount with the description into the ledger
        self.ledger.append({"amount": amount,"description": description})
        # Add onto the balance as money was deposited
        self.balance = self.balance + amount

    def check_funds(self, amount):
        #Check whether there is sufficient funds for withdrawal or transfer
        if (amount > self.balance):
            # There is insufficient funds, return False
            return False
        else:
            # There is sufficient funds, return True
            return True

    def withdraw(self,amount,description=""):
        if(self.check_funds(amount) == True):
            # Withdraw an amount with the description into the ledger
            # Only do the withdrawal if there is sufficient funds and return True
            self.ledger.append({"amount": amount*-1, "description": description})
            # Deduct from the balance as money was withdrawn
            self.balance = self.balance - amount

        # Return the check funds Boolean value
        return self.check_funds(amount)

    def get_balance(self):
        # Return the balance calculated
        return self.balance

    def transfer(self, amount, other_category):
        # Method to transfer money from one category to another
        if(self.check_funds(amount) == True):
            # Withdraw money from self category to other category
            self.ledger.append({"amount": amount * -1, "description": "Transfer to " + other_category.name})
            # Deduct from the self balance as money was withdrawn
            self.balance = self.balance - amount

            # Transfer money to other category from self category
            other_category.ledger.append({"amount": amount,"description": "Transfer from " + self.name})
            # Deduct from the self balance as money was withdrawn
            other_category.balance = other_category.balance + amount

        # Return the check funds Boolean value
        return self.check_funds(amount)


    def __str__(self):
        # This function is used to print the budget object
        # The first title line in the output is the category that is in the center
        line = '{0:*^30}\n'.format(self.name)
        line2 = ''
        # Determine the amount of things in the ledger
        j = len(self.ledger)

        for i in range(j):
            # Go through each item in the ledger
            # Display the description and the amount of the ledger
            line2 = line2 + '{0:<23}'.format(self.ledger[i]['description'][0:23]) + '{0:7.2f}\n'.format(float(self.ledger[i]['amount']))

        # Display the category total
        line3 = 'Total: {}\n'.format(self.balance)

        # Return the lines to be printed
        return line + line2 + line3

def create_spend_chart(categories):
    # Determine how many categories there are
    k = len(categories)
    # Initialise the list for withdrawals
    spent_cat = []
    #print(k)
    #print(len(categories[0].ledger))
    for l in range(k):
        # Go through each category
        m = len(categories[l].ledger)
        # Determine the length of the ledger for each category
        #print(m)
        total_spent = 0
        for n in range(m):
            # Go through the ledger
            if (categories[l].ledger[n]['amount'] < 0):
                # Add up the total withdrawals for each category
                total_spent = total_spent + categories[l].ledger[n]['amount']

        # Put the withdrawals for each category into a list
        spent_cat.append(total_spent)

    #print(spent_cat)
    # Calculate the total spent for all teh categories
    sum_spent = sum(spent_cat)
    #print(sum_spent)
    # Initialise the percentage spent
    Percentage_spent = []
    for o in range(len(spent_cat)):
        # Go through each spending category and determine the percentage spent for each category
        Percentage_spent.append(spent_cat[o]/sum_spent * 100)

    # Initialise the printout for the barchart
    Multiline = 'Percentage spent by category \n'
    # The percentage spent
    Per = [100,90,80,70,60,50,40,30,20,10,0]
    for q in range(len(Per)):
        # For every single line, start with the percentages
        Singleline = '{0:3}| '.format(Per[q])
        for p in range(len(Percentage_spent)):
            # Then, plot the o character for the bar chart, only if the percentages spent satisfies each category
            if(Percentage_spent[p] >= Per[q]):
                Singleline = Singleline + ' o '
            else:
                Singleline = Singleline + '   '

        # Compile the bar chart
        Multiline = Multiline + Singleline + '\n'

    # Place dashes underneath the bar chart
    dashes = 3*k+1
    Multiline = Multiline + '    ' + '-'*dashes + '\n'

    maxi = 0
    for r in range(len(categories)):
    # Determine the maximum characters for all the categories
        if(len(categories[r].name) > maxi):
            maxi = len(categories[r].name)

    Titleline = ' '*5
    # Place a 5 spaces in front of the Title printout

    for s in range(maxi):
        # Iterate through each categories name
        Single_titleline = ''
        for t in range(k):
            # Iterate through each letter in the category
            #print(len(categories[t].name))
            if(len(categories[t].name) > s):
                # Print out the category name if its length is greater than s
                Single_titleline = Single_titleline + '{0:^3}'.format(categories[t].name[s])
            else:
                # Print out blank spaces if the category name if its length is less than s
                Single_titleline = Single_titleline + ' '*3
        # Compile the title line
        Titleline = Titleline + Single_titleline + '\n' + ' '*5

    #for r in range(maxi)
    # Add the title line to the bar chart
    Multiline = Multiline + Titleline
    # Return the bar chart
    return Multiline