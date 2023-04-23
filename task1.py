from collections import Counter

# Filter rows containing 'bot' in user_agent field
bot_logs = df[df['user_agent'].str.contains("bot", case=False, na=False)]

# Count the occurrences of each user_agent
bot_counts = Counter(bot_logs['user_agent'])

# Get the top 10 busiest spiders
top_bots = bot_counts.most_common(10)

# Print the top 10 busiest spiders
for bot, count in top_bots:
    unique_ips = bot_logs[bot_logs['user_agent'] == bot]['ip'].nunique()
    print(f"User-Agent: {bot}\nUnique Addresses: {unique_ips}\nAssociated Search Engine: (provide details)\n")
# Filter rows containing suspicious User-Agent strings
suspicious_logs = df[df['user_agent'].str.contains('<\?system|\*bot\*', case=False, na=False, regex=True)]

# Print the suspicious IP addresses
suspicious_ips = suspicious_logs['ip'].unique()
print("Suspicious IP addresses:")
for ip in suspicious_ips:
    print(ip)
import matplotlib.pyplot as plt

# Filter rows containing 'googlebot' in user_agent field
googlebot_logs = df[df['user_agent'].str.contains("googlebot", case=False, na=False)]

# Convert the 'dtg' field to a datetime object and extract the month and year
googlebot_logs['dtg'] = pd.to_datetime(googlebot_logs['dtg'], format='%d/%b/%Y:%H:%M:%S %z')
googlebot_logs['month_year'] = googlebot_logs['dtg'].dt.to_period('M')

# Count the number of requests per month
monthly_requests = googlebot_logs['month_year'].value_counts().sort_index()

# Plot the timeline
plt.plot(monthly_requests.index.astype(str), monthly_requests.values)
plt.xlabel('Month-Year')
plt.ylabel('Number of Requests')
plt.title('Googlebot Activity')
plt.xticks(rotation=45)
plt.show()
