import matplotlib.pyplot as plt
import numpy as np
tablets_compact = [
    {
        "model": "iPad Pro 12.9",
        "screen_size_in": 12.9,
        "resolution_px": "2732x2048",
        "ram_gb": 16,
        "storage_gb": 256,
        "battery_mah": 10758,
        "weight_g": 682,
        "stylus_support": True,
        "price_rub": 119990,
    },
    {
        "model": "Samsung Galaxy Tab S9 Ultra",
        "screen_size_in": 14.6,
        "resolution_px": "2960x1848",
        "ram_gb": 12,
        "storage_gb": 256,
        "battery_mah": 11200,
        "weight_g": 732,
        "stylus_support": True,
        "price_rub": 99990,
    },
    {
        "model": "Microsoft Surface Pro 9",
        "screen_size_in": 13.0,
        "resolution_px": "2880x1920",
        "ram_gb": 16,
        "storage_gb": 512,
        "battery_mah": 5070,
        "weight_g": 891,
        "stylus_support": True,
        "price_rub": 129990,
    },
    {
        "model": "Xiaomi Pad 6",
        "screen_size_in": 11.0,
        "resolution_px": "2880x1800",
        "ram_gb": 8,
        "storage_gb": 256,
        "battery_mah": 8840,
        "weight_g": 490,
        "stylus_support": False,
        "price_rub": 39990,
    },
]

models = [t["model"] for t in tablets_compact]

name_char = [
    "Диагональ экрана",
    "Оперативная память",
    "Накопитель",
    "Батарея",
    "Вес (обратная)",
    "Цена (обратная)",
]
char = [
    [t["screen_size_in"], t["ram_gb"], t["storage_gb"], t["battery_mah"], 
     1000/t["weight_g"], 100000/t["price_rub"]] 
    for t in tablets_compact
]


def get_normal(char):
    normal = []
    for item in char:
        normal.append([a / b if b!= 0 else 0 for a, b in zip(item, char[0])])
    return normal


def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result


def create_bar(name, values):
    plt.figure(figsize=(10, 6))
    plt.bar(name, values, color=['#3498db', '#e74c3c', '#2ecc71', '#f39c12'])
    plt.xlabel("Модель планшета")
    plt.ylabel("Kту (коэффициент качества)")
    plt.title("Сравнение планшетов по интегральному показателю")
    plt.xticks(rotation=15, ha='right')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


def create_radial(models, name, values):

    for item in values:
        item += item[:1]

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']

    for i in range(len(values)):
        ax.plot(angles, values[i], "o-", linewidth=2, label=models[i],
                color=colors[i % len(colors)])
        ax.fill(angles, values[i], alpha=0.15, color=colors[i % len(colors)])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=11)
    ax.set_ylim(0, 2)
    ax.grid(True, alpha=0.3)

    # Легенда и заголовок
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик планшетов", pad=20)
    plt.tight_layout()
    plt.show()


data = get_quality(get_normal(char))
create_bar(models, data)
create_radial(models, name_char, get_normal(char))
