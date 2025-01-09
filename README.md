# Restaurant Bill Splitter

---
## Description
Ever been stuck figuring out who owes what after putting your card down at a restaurant with friends? The Restaurant Bill Splitter is here to save the day! Built for practicality and accuracy, it ensures everyone pays their fair share, without the awkward math debates in the group chat. After using this program, your wallet will thank you!

The Restaurant Bill Splitter is a Python-based program designed to simplify the process of splitting a restaurant bill, including tax and tip, among a group of people. Users can input their bill details, assign items to individuals or groups, and the program will calculate each person’s total share, including their portions of tax and tip.

The program also features interactive prompts for error correction, allowing users to edit their inputs and ensure accuracy. It uses the tabulate library to present a detailed, easy-to-read table of itemized costs and individual totals.


---

## Features
- **User-Friendly Interface:** Interactively guides users through inputting the bill, tax, tip, and itemized orders.
- **Custom Splitting Options:** Split items among individuals or groups, evenly or unevenly.
- **Tax and Tip Allocation:** Automatically distributes tax and tip proportionally.
- **Editable Inputs:** Allows users to correct errors in the bill, tax, tip, and participant details.
- **Detailed Table Output:** Displays a summary table of itemized costs, individual totals, and the final total.
---
## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the required dependency using pip:

   ```bash 
   pip install tabulate

3. Download or clone the repository containing the bill_splitter.py file.
---
# Usage
1. Run the program:

   ```bash
   python bill_splitter.py

2. Follow the on-screen prompts to:
- Enter the bill amount (excluding tax and tip).
- Input the tax and tip values.
- Verify and edit these amounts as needed.
- Specify the number of people splitting the bill.
- Enter the names of participants.
- Assign items to individuals or groups, specifying amounts and split details.

3. Once all items are entered, the program will calculate:
- Each person’s share of the bill (including tax and tip).
- The total amount for the entire bill.
4. View the itemized bill summary in a formatted table.

---
## Example Output

      ╒══════════════════════╤═══════╤═════════════╤═══════════╤══════════╤═══════════════╕
      │                      │ Kat   │ Escarleth   │ Vanessa   │ Alexia   │   Total Check │
      ╞══════════════════════╪═══════╪═════════════╪═══════════╪══════════╪═══════════════╡
      │ Chicken Sandwich     │ 21.0  │             │           │ 21.0     │         42    │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Pancakes             │       │ 16.0        │           │          │         16    │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Korean Fried Chicken │       │             │ 34.0      │          │         34    │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Silver Needle        │ 6.0   │ 6.0         │           │          │         12    │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Tuna Crispy Rice     │       │             │ 16.0      │ 16.0     │         32    │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Tax                  │ 3.02  │ 3.02        │ 3.02      │ 3.02     │         12.07 │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Tip                  │ 6.12  │ 6.12        │ 6.12      │ 6.12     │         24.48 │
      ├──────────────────────┼───────┼─────────────┼───────────┼──────────┼───────────────┤
      │ Total                │ 36.14 │ 31.14       │ 59.14     │ 46.14    │        172.56 │
      ╘══════════════════════╧═══════╧═════════════╧═══════════╧══════════╧═══════════════╛

---
## Future Improvements

- Add functionality to save the table as a csv file and functionality to load bill data csv for revision
- Create a check functionality that verifies if the total bill matches the table total and informs user of an error if the total does not tie
- Create a web-based version for easy use inside a restaurant
- Add a color to each person's column to easily differentiate between each person

---
## Dependencies
- **Python 3.x**
- **Tabulate:** Used to generate formatted tables for displaying the bill summary.

Install the required dependency using pip:
      

      pip install tabulate

---
## Created by Darren Manalastas
Because splitting the bill should not split friendships!

As a former financial analyst, I developed expert-level proficiency in Microsoft Excel. This expertise sparked a hobby of creating spreadsheets to solve everyday problems in my life. One recurring issue was splitting bills among friends, which often led to confusion and awkward conversations. This led me to create a spreadsheet that calculates how much everyone owes in a nice easy to read format. My spreadsheets became so popular, my friends and family have been asking me to create bill spreadsheets for them since they face this problem in their liffe as well.

Naturally, once I learned Python, this was the first project I wanted to transform from a spreadsheet into a fully functioning program.
This tool has made the bill-splitting process seamless and stress-free for me and my friends. Now that this program exists, my friends and family can easily create nice tables for themselves.

---
## Feedback
Got suggestions or found a bug? Please don't hesitate to reach out! I love learning new things and I would love to improve this project