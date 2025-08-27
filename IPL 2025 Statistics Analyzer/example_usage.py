# Example usage of IPL 2025 Statistics Analyzer
import pandas as pd
import matplotlib.pyplot as plt

# Quick start example
from ipl_analyzer import IPLAnalyzer

# Initialize the analyzer
analyzer = IPLAnalyzer()

# Show tournament summary
analyzer.display_summary()

# Display top performers
analyzer.top_performers('batting', 5)
analyzer.top_performers('bowling', 5)

# Create visualizations
analyzer.visualize_top_batsmen(10)
analyzer.visualize_bowling_analysis(10)
analyzer.team_analysis()

# Compare players
analyzer.compare_players('Sai Sudharsan', 'Virat Kohli', 'batting')
analyzer.compare_players('Prasidh Krishna', 'Josh Hazlewood', 'bowling')

# Generate comprehensive report
analyzer.generate_report()

print("Analysis complete!")
