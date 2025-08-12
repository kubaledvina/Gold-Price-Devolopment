# Gold Price Tracker

This project automatically fetches the current gold price from the internet, saves it into a CSV file, and displays a price trend chart using a Flask web application.

## 📌 Features
- **Scraper** – fetches the current gold price from [Business Insider](https://markets.businessinsider.com/commodities/gold-price)
- **Automatic Saving** – stores date and price in `gold_price.csv`
- **Flask Web Application** – displays a chart of gold price development
- **Automatic Execution** – `.bat` file for scheduled daily runs

## 📂 Project Structure
```
PythonProject/
│
├── graf.py              # Script for generating and saving the gold price chart
├── main.py              # Script for scraping the gold price and saving it to CSV
├── gold_price.csv       # Stored historical data (generated automatically)
├── static/
│   └── graf.png         # Generated chart image
├── templates/
│   └── index.html       # HTML template for the Flask app
├── run.bat              # Batch file to run the scraper automatically
├── requirements.txt     # Project dependencies
└── .venv/               # Virtual environment
```

## ⚙ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the scraper** (saves the price to CSV)
   ```bash
   python main.py
   ```

5. **Run the Flask app**
   ```bash
   python graf.py
   ```
   Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## 🔄 Automatic Execution
Use the `run.bat` file and Windows Task Scheduler to execute the scraper daily:
```bat
@echo off
cd /d "D:\Python\Projekty python\PythonProject"
call .venv\Scripts\activate
python main.py
```

## 📊 Chart Example
The chart is saved in the `static` folder as `graf.png` and displayed via Flask.
