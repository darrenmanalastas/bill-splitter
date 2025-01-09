from tabulate import tabulate

class BillSplitter:
    def __init__(self):
        self._starting_dict = {'bill': 0.00,
                               'tax': 0.00,
                               'tip': 0.00}
        self._people_list = [' ']
        self._rows = []
        self._total_people = 0
        self.initial()

    @property
    def total_bill(self):
        return sum(self._starting_dict.values())

    def initial(self):
        total_dict = self._starting_dict
        bill = float(input("How much is the bill without tax and tip?: "))
        total_dict['bill'] = bill
        tax = float(input("How much tax did you pay?: "))
        total_dict['tax'] = tax
        tip = float(input("How much tip did you pay?: "))
        total_dict['tip'] = tip
        self.double_check_totals()

    def double_check_totals(self):
        print("\n_________________________________________")
        print(f"\nYour total bill is: {self.total_bill:.2f}")
        double_check = input("Is this correct?: ").lower()
        if double_check == 'no':
            self.edit_initial()
        elif double_check == 'yes':
            self.people()
        else:
            print("Invalid input. Please enter a valid response")
            self.double_check_totals()

    def edit_initial(self):
        change = input("Which would you like to change?: ").lower()
        if change not in self._starting_dict:
            print("Invalid entry. Try again")
            self.double_check_totals()
        amount = float(input("What is the new amount?: "))
        self._starting_dict[change] = amount
        print(f"Got it. The new {change} is {self._starting_dict[change]}")
        self.double_check_totals()

    def people(self):
        print("\n_________________________________________")
        self._total_people = int(input(f"\nHow many people should we split {self.total_bill:.2f} by?: "))
        check_people = input(f"Just to make sure: There are {self._total_people} people. "
                             f"\nIs this correct?: ").lower()
        if check_people != 'yes':
            self.people()
        print("\n_________________________________________")
        for num in range(1, self._total_people+1):
            person = input(f"What is the name of person {num}?: ")
            self._people_list.append(person)
        self.double_check_people()

    def print_name_list(self):
        print("\nThese are the list of names:")
        for index in range (1, self._total_people + 1):
            print(f"{index}. {self._people_list[index]}")

    def double_check_people(self):
        self.print_name_list()
        double_check = input("Is this correct? ")
        if double_check == 'no':
            self.edit_people()
        elif double_check == 'yes':
            self.enter_item()
        else:
            self.double_check_people()

    def edit_people(self):
        print("\nWhich name would you like to edit? ")
        name_index = int(input("Give number or type 0 to go back: "))
        if name_index == 0:
            self.double_check_people()
        new_name = input(f"What would you like to change {self._people_list[name_index]} to? ")
        self._people_list[name_index] = new_name
        self.double_check_people()

    def enter_item(self):
        item = ''
        iteration = 1
        while item != 'done':
            item_list = [''] * len(self._people_list)
            print("\n_________________________________________")
            item = input(f"What is the name of item {iteration}? (Type 'done' if done): ")
            if item.lower() == 'done':
                break
            item_list[0] = item
            amount = float(input("What is the amount?: "))
            split = int(input("How many people is this item split by?: "))
            if split == 1:
                self.print_name_list()
                name = int(input(f"Who ordered it? Please give number: "))
                item_list[name] = amount
            elif split == self._total_people:
                for index in range(1, split+1):
                    item_list[index] = amount/split
            elif split > self._total_people:
                print("Invalid number. Try again")
                continue
            else:
                self.print_name_list()
                for index in range(1, split+1):
                    name = int(input(f"Who is person {index}? Please give number: "))
                    item_list[name] = amount/split
            iteration +=1
            self._rows.append(item_list)
        self.add_tax_tip()

    def add_check_totals(self):
        total_row = ['Total']
        for index in range(1, len(self._people_list)):
            total = 0
            for row in self._rows:
                if row[index] != '':
                    total += row[index]
            total_row.append(round(total,2))
        self._rows.append(total_row)
        self._people_list.append('Total Check')
        for item in self._rows:
            total_column = 0
            for index in range(1, len(item)):
                if item[index] != '':
                    total_column += item[index]
            item.append(round(total_column,2))
        self.print_table()

    def add_tax_tip(self):
        tax_row = ['Tax']
        tip_row = ['Tip']
        tax = self._starting_dict['tax']/(len(self._people_list)-1)
        tip = self._starting_dict['tip']/(len(self._people_list)-1)
        for index in range(1, len(self._people_list)):
            tax_row.append(tax)
            tip_row.append(tip)
        self._rows.append(tax_row)
        self._rows.append(tip_row)
        self.add_check_totals()

    def print_table(self):
        for item in range(0, len(self._rows)-1):
            for amount in range(1, len(self._people_list)):
                if self._rows[item][amount] != '':
                    self._rows[item][amount] = round(self._rows[item][amount], 2)
        self._rows[-1] = [
            f"\033[1;33m{item}\033[0m" if isinstance(item, (str, float, int)) else item
            for item in self._rows[-1]]
        print(tabulate(self._rows, self._people_list, tablefmt='fancy_grid', numalign = 'center'))


if __name__ == "__main__":
    print(r"""    
    ██████  ███████ ███████ ████████  █████  ██    ██ ██████   █████  ███    ██ ████████ 
    ██   ██ ██      ██         ██    ██   ██ ██    ██ ██   ██ ██   ██ ████   ██    ██    
    ██████  █████   ███████    ██    ███████ ██    ██ ██████  ███████ ██ ██  ██    ██    
    ██   ██ ██           ██    ██    ██   ██ ██    ██ ██   ██ ██   ██ ██  ██ ██    ██    
    ██   ██ ███████ ███████    ██    ██   ██  ██████  ██   ██ ██   ██ ██   ████    ██                                                            

    ██████  ██ ██      ██          ███████ ██████  ██      ██ ████████ ████████ ███████ ██████  
    ██   ██ ██ ██      ██          ██      ██   ██ ██      ██    ██       ██    ██      ██   ██ 
    ██████  ██ ██      ██          ███████ ██████  ██      ██    ██       ██    █████   ██████  
    ██   ██ ██ ██      ██               ██ ██      ██      ██    ██       ██    ██      ██   ██ 
    ██████  ██ ███████ ███████     ███████ ██      ███████ ██    ██       ██    ███████ ██   ██ 


    """)
    obj = BillSplitter()


