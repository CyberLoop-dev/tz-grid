<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:0f766e&height=160&section=header&text=TZ%20Grid&fontSize=38&fontColor=ffffff" width="100%" alt="TZ Grid banner" />
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=700&color=0F766E&center=true&vCenter=true&width=820&lines=Compare+meeting+times+across+time+zones" alt="Animated project title" />
<p>Convert a meeting date and time across IANA time zones, showing UTC offsets and day changes with daylight-saving support.</p>
<p><img src="https://img.shields.io/github/license/CyberLoop-dev/tz-grid?style=for-the-badge" alt="MIT license" /> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/tz-grid?style=for-the-badge" alt="Top language" /> <img src="https://img.shields.io/github/stars/CyberLoop-dev/tz-grid?style=for-the-badge" alt="Stars" /> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/tz-grid?style=for-the-badge" alt="Last commit" /></p>
<img src="assets/illustration.svg" width="92%" alt="Timezone conversion illustration" /></div>

## 🎯 Overview

TZ Grid converts one local meeting time into several target time zones using Python's IANA timezone database. It shows each local date, time, UTC offset, and whether the conversion lands on the previous or next day. Daylight-saving transitions are handled by zoneinfo.

## ✨ Features

- 🌍 Converts one source time into multiple target zones.
- 🕰️ Uses IANA timezone names such as Europe/Berlin and Asia/Tehran.
- 📆 Shows date changes across time zones.
- ☀️ Applies daylight-saving offsets for the selected date.
- ⚠️ Detects nonexistent local times and explains ambiguous ones.

## 🎬 Demo

<pre><code>python main.py --date 2026-11-16 --time 09:00 --from-zone Asia/Tehran --to-zones Europe/Berlin,America/New_York,Asia/Tokyo</code></pre>

## 🚀 Quick Start

<pre><code>python main.py --date YYYY-MM-DD --time HH:MM --from-zone Asia/Tehran --to-zones Europe/Berlin,America/New_York</code></pre>

## 🧰 Tech Stack

- Python 3.10+ standard library
- zoneinfo and datetime
- IANA timezone database available on the host system

## 🗂️ Folder Structure

<pre><code>tz-grid/
├── main.py
├── requirements.txt
└── assets/
    └── illustration.svg</code></pre>

## 🧭 Roadmap

- [ ] Add a multi-date weekly meeting grid.
- [ ] Add CSV output for sharing with teams.
- [ ] Add a small interactive local web view.

## 🤝 Contributing

Issues and pull requests are welcome. Include the source date, time, timezone names, and expected conversion when reporting a bug.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f766e,100:111827&height=110&section=footer" width="100%" alt="Animated wave footer" /></div>
