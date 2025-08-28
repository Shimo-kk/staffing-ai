import os
import sys
import traceback
from dotenv import load_dotenv
from db.seeds.seed import seed_data

load_dotenv()

if __name__ == "__main__":
    try:
        print("Starts seeding data.")
        seed_data.seed(url=os.getenv("DATABASE_URL", ""))
        print("Data seeding is complete.")
    except Exception as e:
        print("Data seeding failed.")
        print(str(e), file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
