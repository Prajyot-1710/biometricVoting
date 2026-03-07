# 🗳️ BioVoting - Biometric Voting System

**BioVoting** is a secure, modern, and user-friendly biometric voting application built with **Python (Flask)** and **SQLite**. It features a stunning **Glassmorphic Dark Mode UI** and integrates with the **Mantra MFS100** fingerprint scanner for robust voter authentication.

---

## 🚀 Features

### 👔 Election Officer (Admin)
- **Candidate Management**: Add and remove candidates with their name, party, and symbol.
- **Voter Management**: Maintain the voter database and view the complete voter list.
- **Results & Reports**: View real-time voting charts, declare the winner, and reset voting data.
- **Secure Access**: Dedicated login for election officials.

### 🏢 Booth Officer
- **Voter Authentication**: Verify voters using biometric fingerprint scanning (MFS100).
- **Process Control**: Start and manage the voting process at a specific booth.

### 🗳️ Voter
- **Biometric Security**: Cast votes only after successful biometric authentication.
- **Intuitive UI**: Simple and responsive interface to cast votes for chosen candidates.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3 (Glassmorphism), JavaScript (jQuery)
- **Database**: SQLite3
- **Biometric Integration**: Mantra MFS100 Sensor (using `mfs100.js`)

---

## 📋 Prerequisites

Before running the application, ensure you have the following installed:
1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **MFS100 Drivers**: Ensure the Mantra MFS100 driver and client service are installed on your system.
3. **Web Browser**: Chrome or Edge (recommended for sensor compatibility).

---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Prajyot-1710/biometric_voting.git
   cd biometric_voting/BioVoting
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize the Database**:
   The app uses `vote.db`. Ensure it is present in the `BioVoting` directory. (If not, run `debug_schema.py` or `check_db.py` to initialize).

---

## 🖥️ Usage

1. **Start the Flask Server**:
   ```bash
   python voting.py
   ```
   *By default, the server runs on `http://127.0.0.1:8000`.*

2. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000`.

3. **Login Credentials**:
   - Check the `eofficer` and `boothofficer` tables in `vote.db` for the latest login credentials.

---

## 🎨 UI Highlight: Glassmorphism

The application features a premium **Glassmorphic** design with:
- Semi-transparent, frosted-glass backgrounds.
- Vibrant gradients and subtle shadows.
- Fully responsive layout for all screen sizes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Developed by [Prajyot-1710](https://github.com/Prajyot-1710)*
