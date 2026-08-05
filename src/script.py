import numpy as np
import pandas as pd
import random

# -----------------------------
# Configuration
# -----------------------------
ROWS = 10000
np.random.seed(42)
random.seed(42)

# -----------------------------
# Basic Columns
# -----------------------------
patient_id = np.arange(1, ROWS + 1)

age = np.clip(np.random.normal(50, 18, ROWS), 18, 90).astype(int)

gender = np.random.choice(
    ["Male", "Female"],
    ROWS,
    p=[0.52, 0.48]
)

smoking_status = np.random.choice(
    ["Never", "Former", "Current"],
    ROWS,
    p=[0.55, 0.20, 0.25]
)

alcohol_use = np.random.choice(
    ["None", "Occasional", "Frequent"],
    ROWS,
    p=[0.40, 0.45, 0.15]
)

# -----------------------------
# Lifestyle
# -----------------------------

exercise_frequency = np.clip(
    np.random.normal(3,2,ROWS),0,7
).round()

sleep_hours = np.clip(
    np.random.normal(7,1.2,ROWS),3,10
)

stress_level = np.random.randint(1,11,ROWS)

diet_quality = np.random.randint(1,11,ROWS)

steps_per_day = np.random.randint(
    500,
    20000,
    ROWS
)

# -----------------------------
# BMI
# -----------------------------

bmi = (
    24
    + age*0.05
    - exercise_frequency*0.8
    + stress_level*0.25
    + np.random.normal(0,2.5,ROWS)
)

bmi = np.clip(bmi,16,55)

# -----------------------------
# Diseases
# -----------------------------

diabetes = (
    (bmi>30).astype(int)
    |
    (np.random.rand(ROWS)<0.08)
).astype(int)

hypertension = (
    ((age>55)&(bmi>28)).astype(int)
    |
    (np.random.rand(ROWS)<0.12)
).astype(int)

heart_disease = (
    (
        (age>60)
        &
        (hypertension==1)
    ).astype(int)
    |
    (np.random.rand(ROWS)<0.05)
).astype(int)

# -----------------------------
# Lab Values
# -----------------------------

cholesterol = (
    150
    + bmi*2
    + age*0.5
    + diabetes*18
    + np.random.normal(0,18,ROWS)
)

cholesterol = np.clip(
    cholesterol,
    100,
    450
)

glucose = (
    80
    + diabetes*55
    + bmi*1.4
    + np.random.normal(0,12,ROWS)
)

glucose = np.clip(
    glucose,
    60,
    400
)

# -----------------------------
# Blood Pressure
# -----------------------------

systolic_bp = (
    95
    + age*0.45
    + bmi*0.8
    + hypertension*18
    + np.random.normal(0,8,ROWS)
)

diastolic_bp = (
    60
    + age*0.18
    + bmi*0.4
    + hypertension*10
    + np.random.normal(0,5,ROWS)
)

heart_rate = (
    72
    + stress_level
    - exercise_frequency
    + np.random.normal(0,6,ROWS)
)

oxygen_saturation = np.where(
    smoking_status=="Current",
    np.random.normal(94,2,ROWS),
    np.random.normal(98,1,ROWS)
)

oxygen_saturation = np.clip(
    oxygen_saturation,
    80,
    100
)

# -----------------------------
# Hospital Information
# -----------------------------

hospital_visits = np.random.poisson(
    2,
    ROWS
)

icu_admission = (
    (
        (heart_disease==1)
        &
        (oxygen_saturation<92)
    ).astype(int)
)

length_of_stay = (
    2
    + icu_admission*6
    + diabetes*2
    + np.random.poisson(2,ROWS)
)

length_of_stay = np.clip(
    length_of_stay,
    1,
    40
)

readmission = (
    (
        (length_of_stay>8)
        |
        (heart_disease==1)
    ).astype(int)
)

# -----------------------------
# Mortality Risk
# -----------------------------

mortality_risk = (
      diabetes*0.20
    + hypertension*0.20
    + heart_disease*0.35
    + (age/100)*0.20
    + np.random.normal(0,0.05,ROWS)
)

mortality_risk = np.clip(
    mortality_risk,
    0,
    1
)

# -----------------------------
# Disease Outbreak
# -----------------------------

disease_outbreak_index = np.random.uniform(
    0,
    100,
    ROWS
)

# -----------------------------
# Treatment
# -----------------------------

treatment_type = np.random.choice(
    [
        "Medication",
        "Therapy",
        "Surgery",
        "Observation"
    ],
    ROWS,
    p=[0.55,0.15,0.10,0.20]
)

drug_name = np.random.choice(
    [
        "Drug_A",
        "Drug_B",
        "Drug_C",
        "Drug_D",
        "Drug_E"
    ],
    ROWS
)

drug_efficacy = np.clip(
    np.random.normal(78,10,ROWS),
    40,
    100
)

side_effect_score = np.clip(
    np.random.normal(3,1.5,ROWS),
    0,
    10
)
# -------------------------------------------------------
# Insurance
# -------------------------------------------------------

insurance_plan = np.random.choice(
    ["Basic","Silver","Gold","Premium"],
    ROWS,
    p=[0.30,0.35,0.25,0.10]
)

annual_premium = (
    5000
    + age*120
    + heart_disease*4000
    + diabetes*2500
    + np.random.normal(0,2000,ROWS)
)

annual_premium = np.clip(
    annual_premium,
    3000,
    120000
)

# -------------------------------------------------------
# Claims
# -------------------------------------------------------

claim_frequency = np.random.poisson(
    1.5,
    ROWS
)

claim_amount = (
    length_of_stay*9000
    + icu_admission*150000
    + heart_disease*45000
    + diabetes*18000
    + np.random.normal(0,12000,ROWS)
)

claim_amount = np.clip(
    claim_amount,
    1000,
    1200000
)

# -------------------------------------------------------
# Fraud Risk
# -------------------------------------------------------

fraud_risk = (
    claim_amount/1000000
    + claim_frequency*0.15
    + np.random.normal(0,0.08,ROWS)
)

fraud_risk = np.clip(
    fraud_risk,
    0,
    1
)

# -------------------------------------------------------
# Hospital Finance
# -------------------------------------------------------

hospital_revenue = (
    claim_amount
    + np.random.randint(20000,500000,ROWS)
)

hospital_expense = (
    hospital_revenue*np.random.uniform(
        0.55,
        0.95,
        ROWS
    )
)

hospital_credit_score = np.clip(
    np.random.normal(
        720,
        60,
        ROWS
    ),
    300,
    900
)

# -------------------------------------------------------
# Pharma Market
# -------------------------------------------------------

pharma_stock_return = np.random.normal(
    12,
    18,
    ROWS
)

pharma_volatility = np.clip(
    np.random.normal(
        22,
        7,
        ROWS
    ),
    5,
    60
)

esg_score = np.clip(
    np.random.normal(
        70,
        12,
        ROWS
    ),
    20,
    100
)

investment_risk = (
    pharma_volatility*0.9
    - pharma_stock_return*0.4
    - esg_score*0.25
    + np.random.normal(0,5,ROWS)
)

investment_risk = np.clip(
    investment_risk,
    0,
    100
)

portfolio_return = (
    pharma_stock_return
    - investment_risk*0.15
    + np.random.normal(0,3,ROWS)
)

# -------------------------------------------------------
# Final Scores
# -------------------------------------------------------

overall_health_risk = (
      mortality_risk*40
    + diabetes*12
    + hypertension*10
    + heart_disease*18
    + bmi*0.4
    + np.random.normal(0,3,ROWS)
)

overall_health_risk = np.clip(
    overall_health_risk,
    0,
    100
)

financial_risk_score = (
      fraud_risk*40
    + investment_risk*0.4
    + claim_frequency*4
    + claim_amount/60000
    + np.random.normal(0,4,ROWS)
)

financial_risk_score = np.clip(
    financial_risk_score,
    0,
    100
)

# -------------------------------------------------------
# DataFrame
# -------------------------------------------------------

df = pd.DataFrame({

"patient_id":patient_id,
"age":age,
"gender":gender,
"bmi":bmi,
"smoking_status":smoking_status,
"alcohol_use":alcohol_use,
"diabetes":diabetes,
"hypertension":hypertension,
"heart_disease":heart_disease,
"cholesterol":cholesterol,
"glucose":glucose,
"systolic_bp":systolic_bp,
"diastolic_bp":diastolic_bp,
"heart_rate":heart_rate,
"oxygen_saturation":oxygen_saturation,
"hospital_visits":hospital_visits,
"icu_admission":icu_admission,
"length_of_stay":length_of_stay,
"readmission":readmission,
"mortality_risk":mortality_risk,
"disease_outbreak_index":disease_outbreak_index,
"treatment_type":treatment_type,
"drug_name":drug_name,
"drug_efficacy":drug_efficacy,
"side_effect_score":side_effect_score,
"insurance_plan":insurance_plan,
"annual_premium":annual_premium,
"claim_amount":claim_amount,
"claim_frequency":claim_frequency,
"fraud_risk":fraud_risk,
"hospital_revenue":hospital_revenue,
"hospital_expense":hospital_expense,
"hospital_credit_score":hospital_credit_score,
"pharma_stock_return":pharma_stock_return,
"pharma_volatility":pharma_volatility,
"esg_score":esg_score,
"investment_risk":investment_risk,
"portfolio_return":portfolio_return,
"overall_health_risk":overall_health_risk,
"financial_risk_score":financial_risk_score

})

# -------------------------------------------------------
# Missing Values (2%)
# -------------------------------------------------------

for col in [
    "bmi",
    "cholesterol",
    "glucose",
    "claim_amount",
    "drug_efficacy"
]:
    idx = np.random.choice(
        df.index,
        int(ROWS*0.02),
        replace=False
    )
    df.loc[idx,col] = np.nan

# -------------------------------------------------------
# Outliers (1%)
# -------------------------------------------------------

idx = np.random.choice(
    df.index,
    int(ROWS*0.01),
    replace=False
)

df.loc[idx,"bmi"] *= 1.8
df.loc[idx,"cholesterol"] *= 2
df.loc[idx,"claim_amount"] *= 4
df.loc[idx,"hospital_revenue"] *= 5
df.loc[idx,"financial_risk_score"] = 100

# -------------------------------------------------------
# Save Dataset
# -------------------------------------------------------

df.to_csv(
    "health_finance_dataset.csv",
    index=False
)

print(df.head())
print(df.shape)
print("\nDataset Saved Successfully!")