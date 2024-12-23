# Zara Clothing Analysis

This project performs an exploratory data analysis (EDA) on Zara clothing data using **Pandas** and provides an interactive dashboard created with **Streamlit** for visualization and insights.

---

## Features
- **EDA with Pandas**: Cleaned, processed, and analyzed Zara clothing dataset to uncover key insights about product sales, pricing, and trends.
- **Interactive Dashboard**: Built with Streamlit to allow users to dynamically explore:
  - Sales by product category and sub-category.
  - Gender-specific sales trends.
  - Price distributions across products.
  - Top-selling products with detailed metrics.
- **Customizable Filters**: Dropdowns and sliders to filter data by category, gender, and price range.

---

## Tech Stack
- **Python**: Data manipulation and processing.
- **Pandas**: For EDA and data wrangling.
- **Streamlit**: For creating the interactive dashboard.

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/zara-clothing-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd zara-clothing-analysis
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and visit `http://localhost:8501` to view the dashboard.

---

## Dataset
The dataset contains the following columns:
- **Product ID**
- **Gender**
- **Product Category**
- **Sub Category**
- **Sales Volume**
- **URL**
- **SKU**
- **Name**
- **Description**
- **Price**
- **Currency**

> **Note**: The dataset is proprietary and not included in this repository. Replace `data.csv` with your dataset.

---

## Usage
- Explore sales trends across categories and gender.
- Identify high-performing products.
- Analyze pricing and revenue distributions.

---

## Example Insights
1. **Sales by Category**:
   - Dresses have the highest sales volume.
2. **Gender Trends**:
   - Female-oriented products contribute 65% of sales.
3. **Top Products**:
   - The top-selling product is SKU: `XYZ123` with 10,000 units sold.

---

## Streamlit Demo
Check out the live demo here: [Streamlit App](https://share.streamlit.io/yourusername/zara-clothing-analysis/main/app.py)

---

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- **Pandas** for powerful data manipulation.
- **Streamlit** for an easy and effective way to create dashboards.
- Zara for inspiring the analysis.

