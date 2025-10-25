# EPE-PredictorPath-AI

**Hackathon UTEP 2025**

Web-based platform to address an AI-driven solution to optimize patch scheduling in regulated OT environments for El Paso Electric Company.  
Uses a decision tree model to predict patch priority and a REST API to provide recommendations.

## Team
- Melanie Torres
- Vianney Diaz-Barraza
- Karl Prasuhn

## Data
Synthetic data is used to simulate system status and patching conditions.

- `data/patches.tsv` – synthetic dataset with system status, patching info, and computed patch priority.

## Architecture
- **Decision Tree AI model** (`train_model.py`)  
- **REST API** (Python/Flask, planned for integration)  
- **Web demo** (`app/index.html`) using Bootstrap 5

## Tools
- **Python 3.x** – for data generation and model training  
- **Pandas & NumPy** – for data manipulation  
- **scikit-learn** – for Decision Tree model training  
- **joblib** – save/load trained model  
- **Bootstrap 5** – responsive layout and web styling  

## Execution

### Online
Visit the website: [EPE Predictor Web Demo](https://vianneydb.github.io/EPE-PredictorPath-AI/)  
Upload a CSV file to get predicted patch priorities.

### Local
1. Clone the repository:
   ```bash
   git clone https://github.com/vianneydb/EPE-PredictorPath-AI.git
   cd EPE-PredictorPath-AI
    ```

2. Generate synthetic data:
   ```bash
   python data_generator.py
    ```

3. Train the model:
   ```bash
   python train_model.py
    ```

4. Open the web demo:
   ```bash
   open app/index.html, or double-click the file in your file browser
    ```

**Date**: October 2025.
