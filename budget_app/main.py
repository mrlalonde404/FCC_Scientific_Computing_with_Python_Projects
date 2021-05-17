class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=None):
        if description is None:
            description = ""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=None):
        if self.check_funds(amount):
            if description is None:
                description = ""
            if amount > 0:  # make the amount appear negative
                amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        bal = 0
        for i in range(len(self.ledger)):
            bal += self.ledger[i]["amount"]
        self.balance = bal
        return self.balance

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other.name}")
            other.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        # 30 characters with self.name as the center of a bunch of *'s
        name_length = len(self.name)
        num_asterisks = 30 - name_length
        ret_string = ""
        ret_string += ("*" * int((num_asterisks / 2)))
        ret_string += self.name
        ret_string += ("*" * int((num_asterisks / 2))) + "\n"
        for i in range(len(self.ledger)):
            # add the description and include at most 23 characters of it, get the amount of spaces that fill in the
            # rest of the 23 characters
            desc = self.ledger[i]['description'][:23]
            spaces_amount = 23 - len(desc)
            ret_string += desc

            # get the right amount of spaces based on how long the description is
            if spaces_amount > 0:
                ret_string += (" " * spaces_amount)

            # format the amount and get the spaces right based on how long the amount is
            new_amount = str("{:.2f}".format(self.ledger[i]['amount']))
            if len(new_amount) != 7:
                ret_string += (" " * (7 - len(new_amount)))

            ret_string += new_amount + "\n"
        ret_string += "Total: " + str(self.get_balance())
        return ret_string


# input should be a list of categories
def create_spend_chart(list_of_categories):
    totals = []
    percentages = []
    num_hyphens = 1 + (3 * len(list_of_categories))
    categories_withdraws = dict()

    # get all the ledgers from the categories and put them into the dictionary with the name of the category as the key
    for cat in list_of_categories:
        categories_withdraws[cat.name] = []
        for line in cat.ledger:
            if line['amount'] < 0:
                categories_withdraws[cat.name].append(line['amount'])

    # add up all the withdraws from each ledger and append them to totals as the positive version
    for cat_key in categories_withdraws.keys():
        total = 0
        for withdraw in categories_withdraws[cat_key]:
            total += withdraw
        if total < 0:
            total *= -1
        totals.append(total)

    # get the overall total of adding up all the totals together
    overall_total = 0
    for t in totals:
        overall_total += t
    # print(overall_total)
    # print(totals)

    # get each totals percentage in relation to the total amount spent
    for t in totals:
        percentage = (t / overall_total) * 100
        # print(percentage)
        percentage = round(percentage // 10) * 10
        percentages.append(percentage)

    # print(percentages)

    bar_chart = ""
    bar_chart += "Percentage spent by category\n"

    for percentage in range(100, -10, -10):
        if len(str(percentage)) < 3:
            bar_chart += (" " * (3 - len(str(percentage))))
        bar_chart += str(percentage) + "| "
        for i in range(len(list_of_categories)):
            if percentages[i] >= percentage:
                bar_chart += "o"
            else:
                bar_chart += " "
            bar_chart += "  "
        bar_chart += "\n"

    bar_chart += "    " + ("-" * num_hyphens) + "\n"
    lengths = [len(list_of_categories[i].name) for i in range(len(list_of_categories))]
    longest = max(lengths)

    letter = 0
    num_categories = 0
    while letter < longest:
        for cat in list_of_categories:
            if num_categories == 0:
                bar_chart += "     "
            if letter < len(cat.name):
                bar_chart += cat.name[letter] + "  "
            else:
                bar_chart += "   "
            num_categories += 1
            if num_categories == len(list_of_categories):
                if letter == longest:
                    continue
                else:
                    bar_chart += "\n"
                num_categories = 0
                letter += 1

    return bar_chart


def main():
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    actual = create_spend_chart([business, food, entertainment])
    print(actual)

if __name__ == '__main__':
    main()
