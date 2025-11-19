print("Program : Water Usage Tracker & Conservation Helper")

# List to store daily water usage (in liters)
water_usage = []
conservation_tips = {
    "shower": "Take shorter showers to reduce water consumption.",
    "leak": "Fix leaking taps and pipes to avoid water wastage.",
    "garden": "Water your garden early in the morning or late evening.",
    "washing": "Run full loads in washing machines to save water.",
    "reuse": "Reuse rainwater for gardening or cleaning floors."}
    
print("=== Water Usage Tracker ===")
print("Enter daily water usage for 7 days (in liters):")

for i in range(7):
    usage = float(input("Day 1 to 7 usage:" ))
    i=i+1
    water_usage.append(usage)

total_usage = sum(water_usage)
average_usage = total_usage / len(water_usage)

print("\n=== Water Usage Summary ===")
print("Daily usage values:", water_usage)
print("Total weekly water usage:", total_usage)
print("Average daily usage:", average_usage)

threshold = float(input("\nEnter a threshold (liters/day) to detect high usage: "))

print("\nDays exceeding threshold:")
for i, usage in enumerate(water_usage):
    if usage > threshold:
        print("Day {i+1}:", usage)
        
print("\n=== Water Conservation Tips ===")
for topic, tip in conservation_tips.items():
    print(tip)
