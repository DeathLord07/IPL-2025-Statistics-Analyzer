#!/usr/bin/env python3
"""
IPL 2025 Statistics Analyzer
============================

A comprehensive Python project for analyzing IPL 2025 cricket statistics
using pandas and matplotlib.

Author: IPL Analytics Team
Date: August 2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set plotting style
plt.style.use('default')
sns.set_palette("husl")

class IPLAnalyzer:
    """Main class for IPL 2025 statistics analysis"""

    def __init__(self):
        """Initialize the analyzer and load data"""
        self.load_data()
        print("🏏 IPL 2025 Statistics Analyzer Initialized!")
        print(f"📊 Loaded data for {len(self.batting_df)} batsmen, {len(self.bowling_df)} bowlers")
        print(f"🥅 {len(self.fielding_df)} fielders, and {len(self.team_df)} teams")

    def load_data(self):
        """Load all IPL 2025 datasets"""
        try:
            self.batting_df = pd.read_csv('ipl_2025_batting_stats.csv')
            self.bowling_df = pd.read_csv('ipl_2025_bowling_stats.csv')
            self.fielding_df = pd.read_csv('ipl_2025_fielding_stats.csv')
            self.team_df = pd.read_csv('ipl_2025_team_stats.csv')
            print("✅ All datasets loaded successfully!")
        except FileNotFoundError as e:
            print(f"❌ Error loading data: {e}")
            print("Please ensure all CSV files are in the current directory")

    def display_summary(self):
        """Display tournament summary and key statistics"""
        print("\n" + "="*60)
        print("🏆 IPL 2025 TOURNAMENT SUMMARY")
        print("="*60)

        # Tournament winner
        print("🥇 Champion: Royal Challengers Bengaluru")
        print("🥈 Runner-up: Punjab Kings")
        print("🏃 Final Margin: 6 runs")

        # Individual awards
        orange_cap = self.batting_df.loc[self.batting_df['Runs'].idxmax()]
        purple_cap = self.bowling_df.loc[self.bowling_df['Wickets'].idxmax()]
        best_fielder = self.fielding_df.loc[self.fielding_df['Catches'].idxmax()]

        print(f"\n🟠 Orange Cap: {orange_cap['Player']} ({orange_cap['Team']}) - {orange_cap['Runs']} runs")
        print(f"🟣 Purple Cap: {purple_cap['Player']} ({purple_cap['Team']}) - {purple_cap['Wickets']} wickets")
        print(f"🥅 Best Fielder: {best_fielder['Player']} ({best_fielder['Team']}) - {best_fielder['Catches']} catches")

        # Team standings top 4
        print("\n📊 POINTS TABLE (Top 4):")
        top_4 = self.team_df.head(4)
        for _, team in top_4.iterrows():
            print(f"{team['Position']}. {team['Team']} - {team['Points']} pts (NRR: {team['NRR']:+.3f})")

    def top_performers(self, category='batting', n=10):
        """Display top performers in different categories"""
        print(f"\n🌟 TOP {n} {category.upper()} PERFORMERS")
        print("-" * 50)

        if category.lower() == 'batting':
            top = self.batting_df.nlargest(n, 'Runs')[['Player', 'Team', 'Runs', 'Average', 'Strike_Rate']]
            print(top.to_string(index=False))

        elif category.lower() == 'bowling':
            top = self.bowling_df.nlargest(n, 'Wickets')[['Player', 'Team', 'Wickets', 'Economy', 'Average']]
            print(top.to_string(index=False))

        elif category.lower() == 'fielding':
            top = self.fielding_df.nlargest(n, 'Catches')[['Player', 'Team', 'Catches', 'Matches']]
            print(top.to_string(index=False))

    def visualize_top_batsmen(self, n=10):
        """Create visualization for top batsmen"""
        top_batsmen = self.batting_df.nlargest(n, 'Runs')

        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('IPL 2025 - Top Batsmen Analysis', fontsize=16, fontweight='bold')

        # Runs bar chart
        axes[0,0].bar(range(len(top_batsmen)), top_batsmen['Runs'], color='skyblue')
        axes[0,0].set_title('Total Runs')
        axes[0,0].set_xlabel('Players')
        axes[0,0].set_ylabel('Runs')
        axes[0,0].set_xticks(range(len(top_batsmen)))
        axes[0,0].set_xticklabels(top_batsmen['Player'], rotation=45, ha='right')

        # Strike Rate vs Average scatter
        axes[0,1].scatter(top_batsmen['Average'], top_batsmen['Strike_Rate'], 
                         s=top_batsmen['Runs']/10, alpha=0.7, color='orange')
        axes[0,1].set_title('Strike Rate vs Average')
        axes[0,1].set_xlabel('Average')
        axes[0,1].set_ylabel('Strike Rate')

        # Boundaries analysis
        axes[1,0].bar(range(len(top_batsmen)), top_batsmen['Fours'], 
                     width=0.4, label='Fours', alpha=0.8)
        axes[1,0].bar([x+0.4 for x in range(len(top_batsmen))], top_batsmen['Sixes'], 
                     width=0.4, label='Sixes', alpha=0.8)
        axes[1,0].set_title('Boundaries Hit')
        axes[1,0].set_xlabel('Players')
        axes[1,0].set_ylabel('Count')
        axes[1,0].set_xticks([x+0.2 for x in range(len(top_batsmen))])
        axes[1,0].set_xticklabels(top_batsmen['Player'], rotation=45, ha='right')
        axes[1,0].legend()

        # Team distribution
        team_counts = top_batsmen['Team'].value_counts()
        axes[1,1].pie(team_counts.values, labels=team_counts.index, autopct='%1.1f%%')
        axes[1,1].set_title('Team Distribution (Top Batsmen)')

        plt.tight_layout()
        plt.show()

    def visualize_bowling_analysis(self, n=10):
        """Create visualization for bowling analysis"""
        top_bowlers = self.bowling_df.nlargest(n, 'Wickets')

        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('IPL 2025 - Bowling Analysis', fontsize=16, fontweight='bold')

        # Wickets bar chart
        axes[0,0].bar(range(len(top_bowlers)), top_bowlers['Wickets'], color='purple', alpha=0.7)
        axes[0,0].set_title('Total Wickets')
        axes[0,0].set_xlabel('Bowlers')
        axes[0,0].set_ylabel('Wickets')
        axes[0,0].set_xticks(range(len(top_bowlers)))
        axes[0,0].set_xticklabels(top_bowlers['Player'], rotation=45, ha='right')

        # Economy vs Wickets
        axes[0,1].scatter(top_bowlers['Economy'], top_bowlers['Wickets'], 
                         color='red', s=100, alpha=0.7)
        axes[0,1].set_title('Economy Rate vs Wickets')
        axes[0,1].set_xlabel('Economy Rate')
        axes[0,1].set_ylabel('Wickets')

        # Average comparison
        axes[1,0].barh(range(len(top_bowlers)), top_bowlers['Average'], color='green', alpha=0.7)
        axes[1,0].set_title('Bowling Average')
        axes[1,0].set_xlabel('Average')
        axes[1,0].set_ylabel('Bowlers')
        axes[1,0].set_yticks(range(len(top_bowlers)))
        axes[1,0].set_yticklabels(top_bowlers['Player'])

        # Team distribution
        team_counts = top_bowlers['Team'].value_counts()
        axes[1,1].pie(team_counts.values, labels=team_counts.index, autopct='%1.1f%%')
        axes[1,1].set_title('Team Distribution (Top Bowlers)')

        plt.tight_layout()
        plt.show()

    def team_analysis(self):
        """Comprehensive team analysis visualization"""
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('IPL 2025 - Team Performance Analysis', fontsize=16, fontweight='bold')

        # Points table
        axes[0,0].bar(self.team_df['Team'], self.team_df['Points'], color='gold', alpha=0.8)
        axes[0,0].set_title('Points Table')
        axes[0,0].set_xlabel('Teams')
        axes[0,0].set_ylabel('Points')
        axes[0,0].tick_params(axis='x', rotation=45)

        # Net Run Rate
        colors = ['green' if nrr > 0 else 'red' for nrr in self.team_df['NRR']]
        axes[0,1].bar(self.team_df['Team'], self.team_df['NRR'], color=colors, alpha=0.7)
        axes[0,1].set_title('Net Run Rate')
        axes[0,1].set_xlabel('Teams')
        axes[0,1].set_ylabel('NRR')
        axes[0,1].tick_params(axis='x', rotation=45)
        axes[0,1].axhline(y=0, color='black', linestyle='-', alpha=0.3)

        # Total Runs
        axes[0,2].bar(self.team_df['Team'], self.team_df['Total_Runs'], color='orange', alpha=0.8)
        axes[0,2].set_title('Total Runs Scored')
        axes[0,2].set_xlabel('Teams')
        axes[0,2].set_ylabel('Runs')
        axes[0,2].tick_params(axis='x', rotation=45)

        # Win-Loss ratio
        axes[1,0].bar(self.team_df['Team'], self.team_df['Won'], 
                     width=0.4, label='Won', color='green', alpha=0.8)
        axes[1,0].bar([x+0.4 for x in range(len(self.team_df))], self.team_df['Lost'], 
                     width=0.4, label='Lost', color='red', alpha=0.8)
        axes[1,0].set_title('Wins vs Losses')
        axes[1,0].set_xlabel('Teams')
        axes[1,0].set_ylabel('Matches')
        axes[1,0].set_xticks([x+0.2 for x in range(len(self.team_df))])
        axes[1,0].set_xticklabels(self.team_df['Team'], rotation=45)
        axes[1,0].legend()

        # Highest totals
        axes[1,1].bar(self.team_df['Team'], self.team_df['Highest_Total'], color='cyan', alpha=0.8)
        axes[1,1].set_title('Highest Team Total')
        axes[1,1].set_xlabel('Teams')
        axes[1,1].set_ylabel('Runs')
        axes[1,1].tick_params(axis='x', rotation=45)

        # Final positions pie chart
        playoff_teams = self.team_df[self.team_df['Position'] <= 4]['Team']
        non_playoff = self.team_df[self.team_df['Position'] > 4]['Team']

        labels = ['Playoff Teams', 'Non-Playoff Teams']
        sizes = [len(playoff_teams), len(non_playoff)]
        colors = ['lightgreen', 'lightcoral']

        axes[1,2].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        axes[1,2].set_title('Playoff Qualification')

        plt.tight_layout()
        plt.show()

    def compare_players(self, player1, player2, category='batting'):
        """Compare two players performance"""
        if category.lower() == 'batting':
            df = self.batting_df
            metrics = ['Runs', 'Average', 'Strike_Rate', 'Fours', 'Sixes']
        elif category.lower() == 'bowling':
            df = self.bowling_df
            metrics = ['Wickets', 'Economy', 'Average', 'Strike_Rate']
        else:
            print("Category must be 'batting' or 'bowling'")
            return

        try:
            p1_data = df[df['Player'] == player1].iloc[0]
            p2_data = df[df['Player'] == player2].iloc[0]
        except IndexError:
            print("One or both players not found in the dataset")
            return

        p1_values = [p1_data[metric] for metric in metrics]
        p2_values = [p2_data[metric] for metric in metrics]

        x = np.arange(len(metrics))
        width = 0.35

        fig, ax = plt.subplots(figsize=(12, 6))
        bars1 = ax.bar(x - width/2, p1_values, width, label=f"{player1} ({p1_data['Team']})", alpha=0.8)
        bars2 = ax.bar(x + width/2, p2_values, width, label=f"{player2} ({p2_data['Team']})", alpha=0.8)

        ax.set_xlabel('Metrics')
        ax.set_ylabel('Values')
        ax.set_title(f'{category.capitalize()} Comparison: {player1} vs {player2}')
        ax.set_xticks(x)
        ax.set_xticklabels(metrics)
        ax.legend()

        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height:.1f}',
                           xy=(bar.get_x() + bar.get_width() / 2, height),
                           xytext=(0, 3),
                           textcoords="offset points",
                           ha='center', va='bottom', fontsize=8)

        plt.tight_layout()
        plt.show()

    def generate_report(self, filename='ipl_2025_analysis_report.txt'):
        """Generate a comprehensive text report"""
        with open(filename, 'w') as f:
            f.write("IPL 2025 COMPREHENSIVE ANALYSIS REPORT\n")
            f.write("="*50 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            # Tournament Summary
            f.write("TOURNAMENT SUMMARY\n")
            f.write("-" * 20 + "\n")
            f.write("Champion: Royal Challengers Bengaluru\n")
            f.write("Runner-up: Punjab Kings\n")
            f.write("Total Teams: 10\n")
            f.write("Total Matches: 74\n\n")

            # Individual Awards
            orange_cap = self.batting_df.loc[self.batting_df['Runs'].idxmax()]
            purple_cap = self.bowling_df.loc[self.bowling_df['Wickets'].idxmax()]
            best_fielder = self.fielding_df.loc[self.fielding_df['Catches'].idxmax()]

            f.write("INDIVIDUAL AWARDS\n")
            f.write("-" * 20 + "\n")
            f.write(f"Orange Cap: {orange_cap['Player']} ({orange_cap['Team']}) - {orange_cap['Runs']} runs\n")
            f.write(f"Purple Cap: {purple_cap['Player']} ({purple_cap['Team']}) - {purple_cap['Wickets']} wickets\n")
            f.write(f"Best Fielder: {best_fielder['Player']} ({best_fielder['Team']}) - {best_fielder['Catches']} catches\n\n")

            # Team Standings
            f.write("FINAL POINTS TABLE\n")
            f.write("-" * 20 + "\n")
            for _, team in self.team_df.iterrows():
                f.write(f"{team['Position']:2d}. {team['Team']:<4} - {team['Points']:2d} pts | "
                       f"W: {team['Won']:2d} L: {team['Lost']:2d} | NRR: {team['NRR']:+.3f}\n")

            # Top Performers
            f.write("\nTOP 5 BATSMEN\n")
            f.write("-" * 20 + "\n")
            top_batsmen = self.batting_df.nlargest(5, 'Runs')
            for _, player in top_batsmen.iterrows():
                f.write(f"{player['Player']:<20} ({player['Team']}) - "
                       f"{player['Runs']:3d} runs @ {player['Average']:.2f} avg, SR: {player['Strike_Rate']:.2f}\n")

            f.write("\nTOP 5 BOWLERS\n")
            f.write("-" * 20 + "\n")
            top_bowlers = self.bowling_df.nlargest(5, 'Wickets')
            for _, player in top_bowlers.iterrows():
                f.write(f"{player['Player']:<20} ({player['Team']}) - "
                       f"{player['Wickets']:2d} wickets @ {player['Average']:.2f} avg, Econ: {player['Economy']:.2f}\n")

        print(f"📄 Report generated: {filename}")

def main():
    """Main function to run the IPL Analyzer"""
    print("🏏 Welcome to IPL 2025 Statistics Analyzer!")
    print("=" * 50)

    # Initialize analyzer
    analyzer = IPLAnalyzer()

    # Interactive menu
    while True:
        print("\n📋 MENU OPTIONS:")
        print("1. Tournament Summary")
        print("2. Top Batting Performers")
        print("3. Top Bowling Performers")
        print("4. Top Fielding Performers")
        print("5. Visualize Top Batsmen")
        print("6. Visualize Bowling Analysis")
        print("7. Team Analysis")
        print("8. Compare Players")
        print("9. Generate Report")
        print("0. Exit")

        choice = input("\nEnter your choice (0-9): ").strip()

        if choice == '1':
            analyzer.display_summary()
        elif choice == '2':
            analyzer.top_performers('batting')
        elif choice == '3':
            analyzer.top_performers('bowling')
        elif choice == '4':
            analyzer.top_performers('fielding')
        elif choice == '5':
            analyzer.visualize_top_batsmen()
        elif choice == '6':
            analyzer.visualize_bowling_analysis()
        elif choice == '7':
            analyzer.team_analysis()
        elif choice == '8':
            print("Available categories: batting, bowling")
            category = input("Enter category: ").strip()
            player1 = input("Enter first player name: ").strip()
            player2 = input("Enter second player name: ").strip()
            analyzer.compare_players(player1, player2, category)
        elif choice == '9':
            analyzer.generate_report()
        elif choice == '0':
            print("🙏 Thank you for using IPL 2025 Statistics Analyzer!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
