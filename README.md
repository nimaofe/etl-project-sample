# etl-project-sample
 ETL Project Sample repository! This project demonstrates the process of Extracting, Transforming, and Loading data, providing a foundational framework for any ETL tasks.


---

# پروژه نمونه ETL 🌟

سلام! به مخزن **پروژه نمونه ETL** خوش اومدید. این پروژه یه نمونه کامل از فرآیند **استخراج**، **تغییر شکل** و **بارگذاری** داده‌ها رو نشون می‌ده که می‌تونید ازش برای یادگیری و پیاده‌سازی استفاده کنید.

## 🎯 درباره پروژه

توی این مخزن، یه خط لوله ETL داریم که داده‌های فروش رو استخراج می‌کنه، به فرمت قابل استفاده تبدیل می‌کنه و توی یه دیتابیس برای تحلیل بارگذاری می‌کنه. این پروژه یه شروع عالی برای کساییه که می‌خوان با فرآیندهای ETL آشنا بشن.

## 📁 ساختار پروژه

```
etl-project-sample/
│
├── data/
│   └── products.csv          # فایل نمونه داده‌ها
│
├── scripts/
│   └── etl.py                # اسکریپت ETL
│
├── dags/
│   └── etl_dag.py            # تعریف DAG برای Apache Airflow
│
├── requirements.txt          # وابستگی‌های پروژه
└── README.md                 # مستندات پروژه
```

## 🚀 شروع کار

برای راه‌اندازی پروژه روی کامپیوتر خودتون، مراحل زیر رو دنبال کنید.

### ۱. کلون کردن مخزن

```sh
git clone https://github.com/YOUR_USERNAME/etl-project-sample.git
cd etl-project-sample
```

### ۲. نصب وابستگی‌ها

مطمئن بشید که پایتون نصب شده، سپس پکیج‌های مورد نیاز رو نصب کنید:

```sh
pip install -r requirements.txt
```

### ۳. اجرای اسکریپت ETL

اسکریپت ETL رو برای پردازش داده‌ها اجرا کنید:

```sh
python scripts/etl.py
```

### ۴. (اختیاری) راه‌اندازی Apache Airflow

برای خودکارسازی فرآیند ETL، می‌تونید Apache Airflow رو راه‌اندازی کنید:

1. دیتابیس Airflow رو مقداردهی اولیه کنید:

    ```sh
    airflow db init
    ```

2. فایل DAG رو به دایرکتوری DAG های Airflow کپی کنید:

    ```sh
    cp dags/etl_dag.py $AIRFLOW_HOME/dags/
    ```

3. وب‌سرور و Scheduler رو راه‌اندازی کنید:

    ```sh
    airflow webserver --port 8080
    airflow scheduler
    ```

## 🔧 وابستگی‌ها

- `pandas`
- `sqlalchemy`
- `requests`
- `apache-airflow`

## 📊 جریان داده

1. **استخراج**: کشیدن داده‌ها از فایل‌های CSV، دیتابیس‌ها و API ها.
2. **تغییر شکل**: پاکسازی، تغییر شکل و ادغام داده‌ها.
3. **بارگذاری**: بارگذاری داده‌های پردازش‌شده به دیتابیس مقصد.

## 📈 نمونه داده‌ها

اینجا یه نگاهی به داده‌های نمونه داریم:

### products.csv

| product_id | product_name | price |
|------------|---------------|-------|
| 1          | Product A     | 10.99 |
| 2          | Product B     | 12.49 |
| 3          | Product C     | 8.99  |

### orders

| order_id | customer_id | product_id | quantity | order_date |
|----------|-------------|------------|----------|------------|
| 1        | 101         | 1          | 1        | 2023-07-01 |
| 2        | 102         | 2          | 2        | 2023-07-02 |
| 3        | 103         | 3          | 3        | 2023-07-03 |

## 🛠️ این پروژه چطوری کار می‌کنه

اسکریپت ETL مراحل زیر رو انجام می‌ده:

1. **استخراج سفارش‌ها**: تولید داده‌های نمونه سفارش‌ها.
2. **استخراج محصولات**: خواندن داده‌های محصولات از CSV.
3. **استخراج تراکنش‌ها**: کشیدن داده‌های تراکنش از یه API نمونه.
4. **تغییر شکل داده‌ها**: پاکسازی و ادغام داده‌ها.
5. **بارگذاری داده‌ها**: بارگذاری داده‌های پردازش‌شده به یه دیتابیس SQLite.

## 🎉 مشارکت

خوشحال می‌شیم اگه توی پروژه مشارکت کنید! می‌تونید مسائل رو گزارش بدید، مخزن رو فورک کنید و Pull Request بفرستید.

## 📄 لایسنس

این پروژه تحت مجوز MIT منتشر شده.
