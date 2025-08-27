# Installation and Setup Guide for IPL 2025 Statistics Analyzer

## System Requirements

- **Python**: 3.7 or higher
- **Operating System**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 100MB free space

## Required Libraries

Install the following Python packages using pip:

```bash
pip install pandas matplotlib seaborn numpy
```

Or install all at once:
```bash
pip install pandas matplotlib seaborn numpy
```

For Anaconda users:
```bash
conda install pandas matplotlib seaborn numpy
```

## Installation Steps

### Step 1: Download Project Files
Ensure you have all the following files in your project directory:
- `ipl_analyzer.py` (main application)
- `ipl_2025_batting_stats.csv` (batting data)
- `ipl_2025_bowling_stats.csv` (bowling data)
- `ipl_2025_fielding_stats.csv` (fielding data)
- `ipl_2025_team_stats.csv` (team data)
- `example_usage.py` (example script)

### Step 2: Verify Installation
Run this command to verify all dependencies are installed:

```python
python -c "import pandas, matplotlib, seaborn, numpy; print('All dependencies installed successfully!')"
```

### Step 3: Run the Application
```bash
python ipl_analyzer.py
```

## Usage Instructions

### Interactive Mode
When you run `ipl_analyzer.py`, you'll see a menu with options:

1. **Tournament Summary** - View overall tournament statistics
2. **Top Batting Performers** - See leading run scorers
3. **Top Bowling Performers** - See leading wicket takers
4. **Top Fielding Performers** - See best fielders
5. **Visualize Top Batsmen** - Create batting charts
6. **Visualize Bowling Analysis** - Create bowling charts
7. **Team Analysis** - Comprehensive team performance
8. **Compare Players** - Side-by-side player comparison
9. **Generate Report** - Create detailed text report
0. **Exit** - Close the application

### Programmatic Usage
```python
from ipl_analyzer import IPLAnalyzer

# Initialize
analyzer = IPLAnalyzer()

# Get summary
analyzer.display_summary()

# View top performers
analyzer.top_performers('batting', 10)
analyzer.top_performers('bowling', 10)

# Create visualizations
analyzer.visualize_top_batsmen()
analyzer.team_analysis()

# Compare players
analyzer.compare_players('Virat Kohli', 'Sai Sudharsan', 'batting')
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Error
**Error**: `ModuleNotFoundError: No module named 'pandas'`
**Solution**: Install missing packages using pip:
```bash
pip install pandas matplotlib seaborn numpy
```

#### 2. File Not Found Error
**Error**: `FileNotFoundError: [Errno 2] No such file or directory: 'ipl_2025_batting_stats.csv'`
**Solution**: Ensure all CSV files are in the same directory as the Python script.

#### 3. Display Issues
**Error**: Charts not displaying properly
**Solution**: Install additional backend for matplotlib:
```bash
pip install tkinter
```
For Linux users:
```bash
sudo apt-get install python3-tk
```

#### 4. Memory Issues
**Error**: Out of memory errors
**Solution**: Close other applications and ensure you have at least 4GB RAM available.

### Performance Tips

1. **Close unused applications** before running large visualizations
2. **Use smaller datasets** for testing (modify n parameter in functions)
3. **Save plots to files** instead of displaying for better performance:
   ```python
   plt.savefig('chart.png')
   plt.close()
   ```

## Advanced Configuration

### Customizing Visualizations
You can modify the chart styles in the `IPLAnalyzer` class:

```python
# Change color scheme
sns.set_palette("viridis")

# Modify figure size
plt.figure(figsize=(15, 10))

# Change plot style
plt.style.use('seaborn')
```

### Adding New Features
To add new analysis functions, extend the `IPLAnalyzer` class:

```python
def your_custom_analysis(self):
    # Your analysis code here
    pass
```

## Data Sources and Updates

The project uses real IPL 2025 statistics from:
- ESPNCricinfo
- NDTV Sports  
- Cricbuzz
- Official IPL sources

To update with newer data:
1. Replace the CSV files with updated statistics
2. Ensure column names match the existing format
3. Re-run the analyzer

## File Structure
```
ipl-2025-analyzer/
├── ipl_analyzer.py              # Main application
├── example_usage.py             # Example usage script
├── ipl_2025_batting_stats.csv   # Batting statistics
├── ipl_2025_bowling_stats.csv   # Bowling statistics
├── ipl_2025_fielding_stats.csv  # Fielding statistics
├── ipl_2025_team_stats.csv      # Team statistics
└── README.md                    # Documentation
```

## Support

For issues or questions:
1. Check this setup guide
2. Verify all files are present
3. Ensure Python and required packages are properly installed
4. Check that CSV files contain valid data

## Version Information
- **Project Version**: 1.0
- **Python Compatibility**: 3.7+
- **Last Updated**: August 2025
- **Data Coverage**: IPL 2025 complete season