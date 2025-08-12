from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

app = Flask(__name__)

@app.route('/')
def index():
    if not os.path.exists('gold_price.csv'):
        return "File not found."

    df = pd.read_csv('gold_price.csv')
    df['Date'] = pd.to_datetime(df['Date'], format="%d.%m.%Y")
    df = df.sort_values(by='Date')


    plt.figure(figsize=(8, 4))
    plt.plot(df['Date'], df['Price'], marker='o', color="gold")
    plt.title('Gold Price (USD).', fontsize=12, fontweight="bold")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.DayLocator())  # jen celé dny, žádné duplikáty
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))

    plt.tight_layout()

    # Uložení grafu
    path = os.path.join('static', 'graf.png')
    plt.savefig(path)
    plt.close()

    return render_template('index.html')  # Zobrazí HTML stránku s obrázkem

if __name__ == '__main__':
    app.run(debug=True)




