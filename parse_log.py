import sys
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

def main(args):
    log_file = args[0]

    df = pd.read_csv(log_file, sep=r'\s(?=(?:[^"]*"[^"]*")*[^"]*$)(?![^\[]*\])', header=None, engine='python')
    df.columns = ['ip', 'dtg', 'request', 'status_code', 'response_size', 'user_id', 'user_agent']
    
    # Task 4
    bot_logs = df[df['user_agent'].str.contains("bot", case=False, na=False)]
    bot_counts = Counter(bot_logs['user_agent'])
    top_bots = bot_counts.most_common(10)
    print("Task 4: Top 10 busiest spiders")
    for bot, count in top_bots:
        unique_ips = bot_logs[bot_logs['user_agent'] == bot]['ip'].nunique()
        print(f"User-Agent: {bot}\nUnique Addresses: {unique_ips}\nAssociated Search Engine: (provide details)\n")
    
    # Task 5
    suspicious_logs = df[df['user_agent'].str.contains('<\?system|\*bot\*', case=False, na=False, regex=True)]
    suspicious_ips = suspicious_logs['ip'].unique()
    print("Task 5: Suspicious IP addresses")
    for ip in suspicious_ips:
        print(ip)
    
    # Task 6
    googlebot_logs = df[df['user_agent'].str.contains("googlebot", case=False, na=False)]
    googlebot_logs['dtg'] = pd.to_datetime(googlebot_logs['dtg'], format='[%d/%b/%Y:%H:%M:%S %z]')
    googlebot_logs['month_year'] = googlebot_logs['dtg'].dt.to_period('M')
    monthly_requests = googlebot_logs['month_year'].value_counts().sort_index()
    plt.plot(monthly_requests.index.astype(str), monthly_requests.values)
    plt.xlabel('Month-Year')
    plt.ylabel('Number of Requests')
    plt.title('Googlebot Activity')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
