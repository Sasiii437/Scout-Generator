### 🧠 Automated Scouting Report Generator (VAL / LoL)

An analytics pipeline that processes GRID event-level match data to automatically generate scouting insights such as player tendencies, round strategies, and team playstyles.

Designed for esports analysts, coaches, and tournament scouting.

## 🚀 What This Project Does

Given raw GRID match event data, the app:

✅ Normalizes event-level data (VAL / LoL ready)

🔄 Groups events by rounds

📊 Computes player-level statistics

Kills

Ability usage

Bomb plants & defuses

🧠 Detects round strategies

Utility-heavy

Slow default

Standard pace

📝 Produces scouting-ready summaries

🔮 AI scouting report layer planned, with fallback support if credits expire.

## 📁 Project Structure
<pre>
scout_generator/
│
├── app.py                          # Main application entry point
│
├── ai_engine/                      # (Planned) AI-based scouting & insights layer
│
├── analytics/                      # Higher-level analytics & aggregations
│
├── config/                         # Static configuration & mappings
│   ├── grid_config.py              # GRID API & event configuration
│   ├── teams.py                    # Team metadata
│   └── tournaments.py              # Tournament metadata
│
├── data/                           # After execution, these will be created
│   └── raw/
│       ├── events_2629390/
│       │   └── events_2629390_grid.jsonl
│       ├── events_2629391/
│       ├── events_2629392/
│       ├── events_2629393/
│       ├── events_2629394/
│       └── events_2629395/
│
├── data_ingestion/                 # GRID data fetching & ingestion
│   ├── series_fetcher.py           # Fetch series data
│   ├── match_fetcher.py            # Fetch match data
│   ├── file_download.py            # Download raw GRID files
│   ├── event_parser.py             # Parse raw GRID event streams
│   └── central_data.py             # Central ingestion orchestration
│
├── event_processing/               # Core event-level processing
│   ├── base_parser.py              # Shared parsing logic
│   ├── val_parser.py               # VAL-specific event parsing
│   ├── lol_parser.py               # LoL-specific event parsing
│   ├── loader.py                   # Load raw JSONL events
│   ├── normalizer.py               # Normalize GRID events
│   ├── rounds.py                   # Group events by round
│   ├── round_stats.py              # Per-round statistics
│   ├── player_stats.py             # Player-level aggregations
│   └── strategy.py                 # Strategy & playstyle detection
│
├── intelligence/                   # Scouting logic & heuristics
│   ├── heuristics.py               # Pattern detection rules
│   ├── rules.py                    # Domain-specific scouting rules
│   └── scout_engine.py             # Scouting report generation engine
│
├── models/                         # Core data models
│   ├── event.py                    # Event data model
│   ├── series.py                   # Series-level model
│   └── scout_report.py             # Scouting report schema
│
├── reports/                        # Generated scouting reports (output)
│
├── scoring/                        # (Planned) Scoring & ranking logic
│
├── requirements.txt
└── README.md

</pre>

# ⚙️ Setup Instructions
1️⃣ Clone the Repository
<pre>
git clone https://github.com/Sasiii437/Scout-Generator.git
cd scout_generator
</pre>

# 2️⃣ Create & Activate Virtual Environment
🪟 Windows
<pre>
python -m venv .venv
.venv\Scripts\activate
</pre>

🐧 Mac / Linux
<pre>
python3 -m venv .venv
source .venv/bin/activate
</pre>

# 3️⃣ Install Dependencies
<pre>
pip install -r requirements.txt
</pre>

# 🔐 Environment Variables
Create a .env file in the project root:
<pre>
GRID_API_KEY="YOUR_GRID_API_KEY_HERE"
</pre>

# ▶️ How to Run the App
python app.py

## 📤 Output You Will See
<pre>
📦 Total normalized events

🔁 Rounds detected

👤 Player-level statistics

🧠 Match strategy summary

🎯 Sample round strategies
</pre>
