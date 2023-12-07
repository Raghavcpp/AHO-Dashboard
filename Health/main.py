import pandas as pd
import plotly.express as px
import os

# Load the dataset (replace with your path to the dataset)
data = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Impute missing BMI values
data['bmi'].fillna(data['bmi'].median(), inplace=True)

# 1. Distribution of Age among stroke and non-stroke patients
fig_age_distribution = px.histogram(data, x='age', color='stroke', nbins=30,
                                    labels={'stroke': 'Had Stroke'},
                                    title='Distribution of Age Based on Stroke Occurrence',
                                    color_discrete_map={0: 'blue', 1: 'red'},
                                    marginal='box')

# Bar chart of work types and their count
work_type_data = data['work_type'].value_counts().reset_index()
work_type_data.columns = ['Work_Type', 'Count']
fig_work_type = px.bar(work_type_data, x='Work_Type', y='Count', title='Distribution of Work Types')

# 3. Pie chart of smoking status
fig_smoking_status = px.pie(data, names='smoking_status', title='Distribution of Smoking Status')

# 4. Histogram of average glucose level
fig_avg_glucose = px.histogram(data, x='avg_glucose_level', nbins=30,
                               title='Distribution of Average Glucose Level')

# 5. Bar chart of stroke cases based on gender
stroke_gender = data.groupby('gender')['stroke'].sum().reset_index()
fig_gender_stroke = px.bar(stroke_gender, x='gender', y='stroke',
                           labels={'stroke': 'Number of Stroke Cases'},
                           title='Number of Stroke Cases Based on Gender')

# Save figures to the plotly_figs directory
plotly_folder = "./plotly_figs"
if not os.path.exists(plotly_folder):
    os.makedirs(plotly_folder)

fig_age_distribution.write_html(f"{plotly_folder}/fig_age_distribution.html")
fig_work_type.write_html(f"{plotly_folder}/fig_work_type.html")
fig_smoking_status.write_html(f"{plotly_folder}/fig_smoking_status.html")
fig_avg_glucose.write_html(f"{plotly_folder}/fig_avg_glucose.html")
fig_gender_stroke.write_html(f"{plotly_folder}/fig_gender_stroke.html")
