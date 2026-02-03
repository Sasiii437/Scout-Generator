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
├── app.py                         # Main entry point
│
├── event_processing/
│   ├── loader.py                  # Loads raw GRID JSON files
│   ├── normalizer.py              # Normalizes GRID events
│   ├── rounds.py                  # Groups events by round
│   ├── round_stats.py             # Round + player statistics
│   ├── strategy.py                # Strategy & playstyle detection
│├── data/
│   └── raw/
│       └── events_2629390/         # Sample GRID event data
│
├── requirements.txt
└── README.md
</pre>

# ⚙️ Setup Instructions
1️⃣ Clone the Repository
<pre>
git clone <your-github-repo-url>
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
pip install -r requirements.txt

# 🔐 Environment Variables
<pre>
Create a .env file in the project root:

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
