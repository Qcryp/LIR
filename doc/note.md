Scoring
🔴 1. Severity (dari Wazuh)

Wazuh rule level: 1–15

Mapping langsung:

1–5   → Low
6–9   → Medium
10–12 → High
13–15 → Critical

🟠 2. Asset Criticality (INI PEMBEDA)

Kamu harus punya asset inventory sederhana.

Contoh klasifikasi asset:
Asset Type	Criticality
Domain Controller	40
Database Server	35
Production App	30
Bastion / Jump Host	30
User Laptop	15
Test Server	5

📌 Bisa statis dulu (hardcode / table).

🟡 3. Context Bonus (Real World Touch)

Tambahan nilai berdasarkan konteks:

Kondisi	Bonus
Alert berulang (≥3x)	+10
User privileged	+10
Internet-facing asset	+15
Ransomware keyword	+20
Detected off-hours	+5

👉 Ini bikin scoring terlihat matang & berpengalaman.

3️⃣ Final Risk Level Mapping
Risk Score	Level	Action
≥80	🔥 Critical	Auto / Immediate response
60–79	🔴 High	Analyst action
40–59	🟠 Medium	Investigate
<40	🟢 Low	Monitor