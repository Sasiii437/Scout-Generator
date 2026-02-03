🧠 Automated Scouting Report Generator (VAL / LoL)

An analytics pipeline that processes GRID event-level match data to automatically generate scouting insights such as player tendencies, round strategies, and team playstyles.
Designed for esports analysts, coaches, and tournament scouting.

🚀 What This Project Does

Given raw GRID match event data, the app:

Normalizes event-level data (VAL / LoL ready)

Groups events by rounds

Computes player-level stats (kills, abilities, plants, defuses)

Detects round strategies (utility-heavy, slow default, etc.)

Produces scouting-ready summaries
(AI scouting report layer planned with fallback support)

📁 Project Structure
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
│
├── data/
│   └── raw/
│       └── events_2629390/         # Sample GRID event data
│
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd scout_generator

2️⃣ Create & Activate Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate


Mac / Linux

python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


(Only standard Python libraries used so far)

Add Environment variables
create .env file and use the below pattern in the file
GRID_API_KEY="***************************" ( Your API key )

▶️ How to Run the App
python app.py


You will see:

Total normalized events

Rounds detected

Player-level stats

Match strategy summary

Sample round strategies
