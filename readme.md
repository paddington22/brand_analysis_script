### Для запуска скрипты выполните команды в терминале
```commandline
git clone https://github.com/paddington22/brand_analysis_script.git
```
```commandline
cd brand_analysis_script
```
```commandline
python -m venv venv

```

```commandline
venv\Scripts\activate
```
```commandline
pip install -r requirements.txt
```
```commandline
python main.py --files test_data/products1.csv test_data/products2.csv --report average-rating
```
### Пример запуска
run.png
### Показатель покрытия тестами
coverage.png

### Для добавления дополнительнх отчетов
- в src/reports/reports.py реализовать класс с необходимым отчетом
- в main.py обновить словарь REPORT_TYPES