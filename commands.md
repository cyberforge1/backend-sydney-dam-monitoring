# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt


# Run App

python run.py


# Scripts

python scripts/db_connection_check.py

python scripts/collect_data.py

python scripts/test_env.py

python scripts/export_table_records.py

python scripts/insert_dam_analysis_data.py



# Documentation

{base_url}/api/docs


# Scripts

python scripts/data_collection_and_export.py

python scripts/test_api_endpoints.py
