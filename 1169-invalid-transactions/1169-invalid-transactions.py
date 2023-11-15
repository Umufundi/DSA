from collections import defaultdict

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalids = []

        transactionDict = defaultdict(list)

        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            transactionDict[name].append((time, city))
        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)

            if amount > 1000:
                invalids.append(transaction)
            else:
                for other_time, other_city in transactionDict[name]:
                    if abs(time - other_time) <= 60 and city != other_city:
                        invalids.append(transaction)
                        break


        return invalids