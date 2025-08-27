# IPL 2025 Statistics Analyzer

A comprehensive Python project for analyzing IPL 2025 cricket statistics using pandas and matplotlib.

## Project Overview

This project provides a complete data analysis toolkit for the IPL (Indian Premier League) 2025 season. It includes real statistical data from the tournament and offers various visualization and analysis capabilities.

## Features

- **Comprehensive Statistics**: Batting, bowling, fielding, and team performance data
- **Data Visualization**: Interactive charts and graphs using matplotlib and seaborn
- **Performance Analytics**: Player comparisons, team rankings, and trend analysis
- **Export Capabilities**: Generate reports and save visualizations
- **Real IPL 2025 Data**: Based on actual tournament statistics

## Dataset Information

The project includes four main datasets:

### 1. Batting Statistics (`ipl_2025_batting_stats.csv`)
- **Top Performers**: Sai Sudharsan (GT) leads with 759 runs, followed by Suryakumar Yadav (MI) with 717 runs
- **Fields**: Player, Team, Matches, Runs, Average, Strike Rate, Fours, Sixes, Highest Score
- **Key Insights**: 15 top batsmen across all IPL teams

### 2. Bowling Statistics (`ipl_2025_bowling_stats.csv`)
- **Purple Cap Winner**: Prasidh Krishna (GT) with 25 wickets
- **Fields**: Player, Team, Matches, Wickets, Economy, Average, Strike Rate, Best Figures
- **Key Insights**: Top 15 bowlers including pace and spin specialists

### 3. Fielding Statistics (`ipl_2025_fielding_stats.csv`)
- **Best Fielder**: Shimron Hetmyer (RR) with 13 catches
- **Fields**: Player, Team, Matches, Catches, Run Outs, Dismissals
- **Key Insights**: Top 10 fielders showcasing safe hands

### 4. Team Statistics (`ipl_2025_team_stats.csv`)
- **Champions**: Royal Challengers Bengaluru defeated Punjab Kings in the final
- **Fields**: Team, Position, Matches, Won, Lost, Points, NRR, Total Runs, Wickets, Highest Total
- **Key Insights**: Complete league standings and performance metrics

## Installation Requirements

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
```

## Quick Start Guide

### 1. Load the Data
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
batting_df = pd.read_csv('ipl_2025_batting_stats.csv')
bowling_df = pd.read_csv('ipl_2025_bowling_stats.csv')
fielding_df = pd.read_csv('ipl_2025_fielding_stats.csv')
team_df = pd.read_csv('ipl_2025_team_stats.csv')

print("Data loaded successfully!")
print(f"Batting data shape: {batting_df.shape}")
print(f"Bowling data shape: {bowling_df.shape}")
```

### 2. Basic Analysis Examples

#### Top Run Scorers Analysis
```python
# Display top 10 run scorers
top_batsmen = batting_df.nlargest(10, 'Runs')[['Player', 'Team', 'Runs', 'Average', 'Strike_Rate']]
print("Top 10 Run Scorers:")
print(top_batsmen)

# Visualize top scorers
plt.figure(figsize=(12, 6))
plt.bar(top_batsmen['Player'], top_batsmen['Runs'])
plt.title('IPL 2025 - Top 10 Run Scorers')
plt.xlabel('Players')
plt.ylabel('Runs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

#### Bowling Analysis
```python
# Top wicket takers
top_bowlers = bowling_df.nlargest(10, 'Wickets')[['Player', 'Team', 'Wickets', 'Economy', 'Average']]
print("Top 10 Wicket Takers:")
print(top_bowlers)

# Economy vs Wickets scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(bowling_df['Economy'], bowling_df['Wickets'], alpha=0.7)
plt.xlabel('Economy Rate')
plt.ylabel('Wickets')
plt.title('Economy Rate vs Wickets - IPL 2025')
for i, player in enumerate(bowling_df['Player']):
    plt.annotate(player, (bowling_df['Economy'][i], bowling_df['Wickets'][i]), 
                xytext=(5, 5), textcoords='offset points', fontsize=8)
plt.tight_layout()
plt.show()
```

#### Team Performance Analysis
```python
# Team standings visualization
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.bar(team_df['Team'], team_df['Points'])
plt.title('IPL 2025 Points Table')
plt.xlabel('Teams')
plt.ylabel('Points')
plt.xticks(rotation=45)

plt.subplot(2, 2, 2)
plt.bar(team_df['Team'], team_df['NRR'])
plt.title('Net Run Rate by Team')
plt.xlabel('Teams')
plt.ylabel('Net Run Rate')
plt.xticks(rotation=45)

plt.subplot(2, 2, 3)
plt.bar(team_df['Team'], team_df['Total_Runs'])
plt.title('Total Runs by Team')
plt.xlabel('Teams')
plt.ylabel('Total Runs')
plt.xticks(rotation=45)

plt.subplot(2, 2, 4)
plt.bar(team_df['Team'], team_df['Won'])
plt.title('Matches Won by Team')
plt.xlabel('Teams')
plt.ylabel('Matches Won')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

### 3. Advanced Analysis Functions

#### Player Performance Comparison
```python
def compare_batsmen(player1, player2):
    """Compare two batsmen's performance"""
    p1_data = batting_df[batting_df['Player'] == player1].iloc[0]
    p2_data = batting_df[batting_df['Player'] == player2].iloc[0]
    
    metrics = ['Runs', 'Average', 'Strike_Rate', 'Fours', 'Sixes']
    p1_values = [p1_data[metric] for metric in metrics]
    p2_values = [p2_data[metric] for metric in metrics]
    
    x = range(len(metrics))
    width = 0.35
    
    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], p1_values, width, label=player1)
    plt.bar([i + width/2 for i in x], p2_values, width, label=player2)
    
    plt.xlabel('Metrics')
    plt.ylabel('Values')
    plt.title(f'Performance Comparison: {player1} vs {player2}')
    plt.xticks(x, metrics)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Example usage
compare_batsmen('Sai Sudharsan', 'Suryakumar Yadav')
```

#### Team Analysis Function
```python
def analyze_team_performance(team_name):
    """Analyze a specific team's performance"""
    team_info = team_df[team_df['Team'] == team_name].iloc[0]
    team_batsmen = batting_df[batting_df['Team'] == team_name]
    team_bowlers = bowling_df[bowling_df['Team'] == team_name]
    team_fielders = fielding_df[fielding_df['Team'] == team_name]
    
    print(f"=== {team_name} Performance Analysis ===")
    print(f"Position: {team_info['Position']}")
    print(f"Points: {team_info['Points']} | Won: {team_info['Won']} | Lost: {team_info['Lost']}")
    print(f"Net Run Rate: {team_info['NRR']}")
    print(f"Total Runs: {team_info['Total_Runs']}")
    
    print(f"\nTop Batsmen:")
    if not team_batsmen.empty:
        print(team_batsmen[['Player', 'Runs', 'Average', 'Strike_Rate']].to_string(index=False))
    
    print(f"\nTop Bowlers:")
    if not team_bowlers.empty:
        print(team_bowlers[['Player', 'Wickets', 'Economy', 'Average']].to_string(index=False))
    
    print(f"\nTop Fielders:")
    if not team_fielders.empty:
        print(team_fielders[['Player', 'Catches', 'Matches']].to_string(index=False))

# Example usage
analyze_team_performance('GT')
```

### 4. Statistical Insights and Trends

#### Strike Rate vs Average Analysis
```python
def batting_efficiency_analysis():
    """Analyze batting efficiency (Strike Rate vs Average)"""
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot
    colors = plt.cm.Set3(range(len(batting_df)))
    scatter = plt.scatter(batting_df['Average'], batting_df['Strike_Rate'], 
                         c=colors, s=batting_df['Runs']/10, alpha=0.7)
    
    # Add player labels
    for i, player in enumerate(batting_df['Player']):
        plt.annotate(player, (batting_df['Average'][i], batting_df['Strike_Rate'][i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.xlabel('Batting Average')
    plt.ylabel('Strike Rate')
    plt.title('IPL 2025: Batting Efficiency Analysis\n(Bubble size represents total runs)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

batting_efficiency_analysis()
```

#### Economy vs Wickets for Bowlers
```python
def bowling_efficiency_analysis():
    """Analyze bowling efficiency"""
    plt.figure(figsize=(12, 8))
    
    # Create scatter plot
    colors = plt.cm.viridis(range(len(bowling_df)))
    scatter = plt.scatter(bowling_df['Economy'], bowling_df['Wickets'], 
                         c=colors, s=100, alpha=0.7)
    
    # Add bowler labels
    for i, bowler in enumerate(bowling_df['Player']):
        plt.annotate(bowler, (bowling_df['Economy'][i], bowling_df['Wickets'][i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    plt.xlabel('Economy Rate')
    plt.ylabel('Wickets Taken')
    plt.title('IPL 2025: Bowling Efficiency Analysis')
    plt.grid(True, alpha=0.3)
    
    # Add efficiency quadrants
    plt.axhline(y=bowling_df['Wickets'].median(), color='red', linestyle='--', alpha=0.5)
    plt.axvline(x=bowling_df['Economy'].median(), color='red', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.show()

bowling_efficiency_analysis()
```

## Key Tournament Highlights

### Tournament Summary
- **Winner**: Royal Challengers Bengaluru (first title after 18 years)
- **Runner-up**: Punjab Kings
- **Orange Cap**: Sai Sudharsan (GT) - 759 runs
- **Purple Cap**: Prasidh Krishna (GT) - 25 wickets
- **MVP**: Suryakumar Yadav (MI)

### Notable Records
- **Highest Individual Score**: Abhishek Sharma (SRH) - 141
- **Highest Team Total**: SRH - 286/6 vs RR
- **Best Bowling Figures**: Multiple players with 5-wicket hauls
- **Most Catches**: Shimron Hetmyer (RR) - 13 catches

### Team Performance Insights
- **Punjab Kings** and **RCB** topped the league stage with 19 points each
- **Mumbai Indians** had the highest NRR (+1.142) despite finishing 4th
- **SRH** scored the most runs in a single innings (286/6)
- **Tournament was suspended** briefly due to India-Pakistan crisis

## Project Extensions

### Possible Enhancements
1. **Predictive Modeling**: Predict player performance for next season
2. **Interactive Dashboards**: Create web-based dashboards using Plotly/Dash
3. **Real-time Updates**: Connect to live APIs for current match data
4. **Advanced Analytics**: Machine learning models for team selection
5. **Comparison Tools**: Historical IPL data comparison

### Additional Visualizations
1. **Heatmaps**: Team vs team performance
2. **Radar Charts**: Player skill comparison
3. **Timeline Analysis**: Performance trends throughout the season
4. **Network Graphs**: Player-team relationships

## Data Sources

This project uses real IPL 2025 statistics compiled from:
- ESPN Cricinfo
- NDTV Sports
- Cricbuzz
- Official IPL sources

## License

This project is for educational and analytical purposes. All IPL data rights belong to their respective owners.

---

**Happy Analyzing! 🏏📊**