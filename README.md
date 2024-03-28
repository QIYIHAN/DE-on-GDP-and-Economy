# Economic and Data Engineering: A GDP-Focused Study

## Division of labor
Our team will divide the task based on the data acquisition methods (Groups A, B, C, D) before integration. 

**Group A** will work on a paper found in our chat group, extracting data from four specified sources for sub-analysis under our main theme, such as the economic analysis of Chinese rural areas. 

**Group B** is tasked with finding articles related to China's economy, performing OCR, and extracting information; data in graphical form like line charts is also acceptable. The goal is not the volume but the diversity of data sources, culminating in a CSV file compilation, which may include numerical and textual columns citing specific articles. 

**Group C** will scrape textual reports from websites, perform basic sentiment analysis using NLP or direct API like ChatGPT's, and record the findings in a CSV file with URL, content, and sentiment analysis results. 

**Group D** will use APIs like yfinance to gather recent stock market data from China, processing and visualizing it to show trends, such as market cap by year, with the possibility of including data from other countries if Chinese stock data is insufficient.

## Post-Data Acquisition Processes:

Convert, cleanse, and process the data into a format suitable for analysis and modeling. Initially, store it on personal computers, then upload it to the assigned Alibaba Cloud. Direct uploads through code are also acceptable.

### Data Cleansing:
- **Missing Value Treatment**: Identify and address missing data by deletion, imputation, or interpolation.
- **Outlier Handling**: Detect and rectify outliers through business rules or statistical methods.
- **Data Standardization**: Ensure uniform formats and units, such as date formats and text case normalization.

### Data Transformation:
- **Data Type Conversion**: Adapt data into formats appropriate for analysis, like changing strings to numerical types or dates to timestamps.
- **Merging & Splitting**: Combine sources or segment datasets for further analysis.
- **Aggregation & Reshaping**: Aggregate data as needed (sum, count, average) and reshape for pivot tables and analysis.

### Data Processing:
- **Feature Engineering**: Perform feature extraction, selection, and transformation to highlight the most representative predictive attributes.
- **Sampling & Splitting**: Execute data sampling (over/under-sampling) and split data into training, validation, and test sets.
- **Normalization & Standardization**: Apply these to numerical features to maintain scale uniformity and avoid bias in model training.

### Data Quality Verification:
- **Consistency Checks**: Ensure data consistency across systems or tables, maintaining key integrity and referential completeness.
- **Legality Verification**: Confirm data adherence to business rules and constraints.
- **Quality Metrics**: Measure and monitor data quality with defined metrics (accuracy, completeness, consistency, timeliness).
