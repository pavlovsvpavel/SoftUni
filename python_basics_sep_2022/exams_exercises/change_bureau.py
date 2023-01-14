bitcoins = int(input())
yans = float(input())
commission = float(input())

bitcoins_in_bgn = bitcoins * 1168
yans_in_usd = yans * 0.15
yans_in_bgn = yans_in_usd * 1.76

bitcoins_in_eur = bitcoins_in_bgn / 1.95
yans_in_eur = yans_in_bgn / 1.95

total_eur = bitcoins_in_eur + yans_in_eur
commission_sum = total_eur * (commission / 100)
total_eur_without_commission = total_eur - commission_sum
print(f"{total_eur_without_commission:.2f}")
