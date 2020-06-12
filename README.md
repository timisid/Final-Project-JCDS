# Womens E-commerce Clothing Reviews 
dataset source:https://www.kaggle.com/nicapotato/womens-ecommerce-clothing-reviews

![gambar1](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/about.jpg)

This is a Women’s Clothing E-Commerce dataset revolving around the reviews written by customers. Its nine supportive features offer a great environment to parse out the text through its multiple dimensions. Because this is real commercial data, it has been anonymized, and references to the company in the review text and body have been replaced with “retailer”.
This dataset includes 23486 rows and 10 feature variables. Each row corresponds to a customer review, and includes the variables:

- Clothing ID: Integer Categorical variable that refers to the specific piece being reviewed.
- Age: Positive Integer variable of the reviewers age.
- Title: String variable for the title of the review.
- Review Text: String variable for the review body.
- Rating: Positive Ordinal Integer variable for the product score granted by the customer from 1 Worst, to 5 Best.
- Recommended IND: Binary variable stating where the customer recommends the product where 1 is recommended, 0 is not recommended.
- Positive Feedback Count: Positive Integer documenting the number of other customers who found this review positive.
- Division Name: Categorical name of the product high level division.
- Department Name: Categorical name of the product department name.
- Class Name: Categorical name of the product class name.

## Goals:
based on the data source i want to make 2 prediction of classification
1. predict the customer recommendation, if they want to recommend the product or not
2. predict the customer reviews into sentiment analysis

## Steps: 
### 1. Data Extraction, Data Cleaning and Exploratory Data Analysis (EDA)
extract the data : read the data source, seeing the data type, decribe the data source and counting the unique value since i want to predict in classification

![gambar2](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/1.Data%20Extraction.JPG)

cleaning data : dropping and filling based on missing value percentage. if the data have significant value and information or have more than 40% missing value i'll try to fill it. but if the value are not significant, choose to drop it. also detect the outlier to find the normal distribution of the data and drop the anomalies

>dropna : features of 'Division Name' is part of 'Department Name', 'Department Name' is tiny part of 'Class Name'. since the 'Class Name' isNaN 14 over the 20.000 data, the target value at 'Recommend IND' and 'Rating' will not reduce the variance data, we just need to delete it

![gambar3](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/2.Data%20Cleaning_Dropna.JPG)

>fillna : 'Review Text' total isNaN == 845. the only feature can get hint to fillna 'Review Text' is 'title', but title have been dropded, other features not relatable to fill this. rather than delete the data, i prefer to fill the nan review with 'No Reviews' to keep the variation of the data

![gambar4](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/2.Data%20Cleaning_Fillna.JPG)

>Detect Outlier : from the describe features 'Age' has a outlier up to age 99 that makes us think twice for the e-commerce usage

![gambar5](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/2.Data%20Cleaning_Detect%20Outlier.JPG)

Exploratory Data Analysis (EDA) : 
>Target with Age Distribution
the target (Rating and Recommendation) we want to see our customer based on 'Age' section to know customer distribution

![gambar6](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/3.EDA_1.JPG)

based on the graph, most of the given rating 1 (worst) and rating 5 (best) comes from 50 above in average

>Top Selling Product Classification

![gambar7](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/3.EDA_2.JPG)

based on the product most selling product are Dresses, Knits, and Blouses

>Coefficient between features

![gambar8](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/3.EDA_3.JPG)

based on the heatmap the top 3 that affected between features is 'Recommendation", "Rating", "Age"

>The Target

![gambar9](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/3.EDA_4.JPG)

based on the graph, the recommended from the dataset is dominant and the not recommended is between 17%. it's imbalance and the target needs to be balance using 3 different ways.

![gambar9](https://github.com/timisid/Final-Project-JCDS/blob/master/Dashboard%20Final%20Project/static/3.EDA_5.JPG)

### 2. 




