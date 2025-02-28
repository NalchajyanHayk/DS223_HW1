# DS223_HW1

# Homework on Bass Model

This project analyzes global consumer spending on smart home technology and implements the **Bass Diffusion Model** to study adoption trends.

## 📂 Project Structure

- `statistic_id693303_consumer_smart_home_spending_worldwide_2015_2025.xlsx` - The dataset containing consumer spending data from 2015 to 2025.
- `images/`
  - `bass_model_adopters.png` - Plot of estimated adopters over time.
  - `bass_model_plot.png` - Plot of the Bass Model fit.
- `report/`
  - `DS223_HW1_Hayk_Nalchajyan.pdf` - Final report submission.
  - `report.pdf` - Additional report document.
- `scripts/`
  - `utility_functions.py` - Contains data processing and modeling functions.
- `venv/` - Virtual environment directory.
- `README.md` - This file.
- `requirements.txt` - List of dependencies required to run the project.
- `DS223_HW1_Hayk_Nalchajyan.ipynb` - A Jupyter Notebook implementing the analysis and modeling.

---

## ⚙️ Installation

To set up the project, create a virtual environment and install dependencies:

```sh
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```python
from utility_functions import load_smart_home_spending

df = load_smart_home_spending("statistic_id693303_consumer_smart_home_spending_worldwide_2015_2025.xlsx")
print(df.head())
```

```python
from utility_functions import bass_model
import numpy as np

t = np.arange(0, 11)  # Time in years
p, q, M = 0.03, 0.38, 100  # Example parameters
adoption = bass_model(t, p, q, M)
print(adoption)
```