import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.type == "diff":
    if args.payment is not None or args.interest is None or \
            (len(vars(args)) < 4):
        print("Incorrect parameters")
    else:
        interest = float(args.interest)
        principal = int(args.principal)
        periods = int(args.periods)
        nominal_interest = interest / 1200
        total_payment = 0
        for i in range(1, periods + 1):
            differential_payment = math.ceil((principal / periods) + (
                        nominal_interest * (principal - ((principal * (i - 1)) / periods))))
            print("Month {}: payment is {}".format(i, differential_payment))
            total_payment = total_payment + differential_payment
        overpayment = total_payment - principal
        print("\nOverpayment = {}".format(overpayment))
elif args.type == "annuity":
    if args.interest is None or (len(vars(args)) < 4):
        print("Incorrect parameters")
    elif args.payment is None:
        principal = int(args.principal)
        periods = int(args.periods)
        interest = float(args.interest)
        nominal_interest = interest / 1200
        payment = principal * ((nominal_interest * ((nominal_interest + 1) ** periods)) / (((1 + nominal_interest) **
                                                                                            periods) - 1))
        print("Your annuity payment = {}!".format(math.ceil(payment)))
        overpayment = math.ceil(payment) * periods - principal
        print("Overpayment = {}".format(overpayment))
    elif args.principal is None:
        payment = int(args.payment)
        periods = int(args.periods)
        interest = float(args.interest)
        nominal_interest = interest / 1200
        principal = payment / (
                    (nominal_interest * ((1 + nominal_interest) ** periods)) /
                    (((1 + nominal_interest) ** periods) - 1))
        print("Your loan principal = {}!".format(principal))
        overpayment = payment * periods - principal
        print("Overpayment = {}".format(overpayment))
    elif args.periods is None:
        principal = int(args.principal)
        payment = int(args.payment)
        interest = float(args.interest)
        nominal_interest = interest / 1200
        number_of_payments = math.ceil(math.log(payment / (payment - nominal_interest * principal),
                                                1 + nominal_interest))
        years = number_of_payments // 12
        months = number_of_payments % 12
        if years == 0:
            if months == 1:
                print("It will take {} month to repay this loan!".format(months))
            else:
                print("It will take {} months to repay this loan!".format(months))
        elif months == 0:
            if years == 1:
                print("It will take {} year to repay this loan!".format(years))
            else:
                print("It will take {} years to repay this loan!".format(years))
        else:
            print("It will take {} years and {} months to repay this loan!".format(years, months))
        overpayment = payment * number_of_payments - principal
        print("Overpayment = {}".format(overpayment))
else:
    print("Incorrect parameters")
