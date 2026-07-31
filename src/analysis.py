import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_trends(csv_path):
    if not os.path.exists(csv_path):
        print("Data file not found.")
        return
    
    df = pd.read_csv(csv_path)
    
    # Calculate 5-year moving average
    df['Moving_Avg'] = df['Anomaly'].rolling(window=5).mean()
    
    # Plotting
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    
    plt.plot(df['Year'], df['Anomaly'], label='Annual Anomaly', alpha=0.5, color='gray')
    plt.plot(df['Year'], df['Moving_Avg'], label='5-Year Moving Average', color='red', linewidth=2)
    
    plt.title('Global Temperature Anomalies (1880-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Temperature Anomaly (°C)', fontsize=12)
    plt.legend()
    
    os.makedirs('results', exist_ok=True)
    plt.savefig('results/temp_anomaly_plot.png')
    print("Analysis complete. Plot saved to results/temp_anomaly_plot.png")

if __name__ == "__main__":
    analyze_trends('data/global_temp_anomalies.csv')
