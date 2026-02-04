import os
import requests


def download_data():
    data_files = {
        "lpgrs_high1_elem_abundance_5deg.tab": "https://pds-geosciences.wustl.edu/lunar/lp-l-grs-5-elem-abundance-v1/lp_9001/data/lpgrs_high1_elem_abundance_5deg.tab",
        "lpgrs_high1_elem_abundance_5deg.lbl": "https://pds-geosciences.wustl.edu/lunar/lp-l-grs-5-elem-abundance-v1/lp_9001/data/lpgrs_high1_elem_abundance_5deg.lbl",
        "lpgrs_high1_elem_abundance_5deg.xml": "https://pds-geosciences.wustl.edu/lunar/lp-l-grs-5-elem-abundance-v1/lp_9001/data/lpgrs_high1_elem_abundance_5deg.xml",
    }

    os.makedirs("data", exist_ok=True)

    for filename, url in data_files.items():
        filepath = os.path.join("data", filename)
        if not os.path.exists(filepath):
            print(f"Downloading {filename}...")
            response = requests.get(url)
            with open(filepath, 'wb') as f:
                f.write(response.content)
        else:
            print(f"{filename} already exists, skipping download.")


if __name__ == "__main__":
    download_data()
