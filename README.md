
<body>
  
<h1>Sales Data Analysis Project</h1>
<h2>Overview</h2>

<p>Welcome to the Sales Data Analysis project for a self-assumed Apparel selling store. This project utilizes a self-generated dataset, created using the <code>DatasetGen.py</code> file, to perform in-depth analysis on the sales data of the store. The primary focus is on gaining valuable insights into customer behavior, item performance, and overall financial trends.</p>

<h2>Project Structure</h2>

<ul>
<li><strong>Sales Data Analysis.ipynb:</strong> This Jupyter Notebook serves as the core of the project, containing a comprehensive analysis of the sales data. The notebook covers various aspects, including mathematical (probabilistic) analyses, relational studies (Market Basket Algorithm), and the application of machine learning models to predict probabilities and expected values. Additionally, the code provides insights into overperforming and underperforming items and item types.</li>
<li><strong>Presentation.pdf:</strong> This PDF file includes a presentation that walks through the execution of the data science pipeline. It highlights correlations within the sales data and provides a visual representation of key findings. The presentation is designed to make the complex analysis accessible to a broader audience.</li>
<li><strong>Report.pdf:</strong> The report contains a detailed overview of the Sales Data Analysis project. It includes explanations of methodologies, key insights, and recommendations based on the analysis. This document is intended for a more in-depth understanding of the project and its implications.</li>
</ul>

<h2>Dataset Overview</h2>

<p>The dataset consists of the following columns:</p>

<table>
<thead>
<tr>
<th>Column</th>
<th>Non-Null Count</th>
<th>Dtype</th>
</tr>
</thead>
<tbody>
<tr>
<td>Customer ID</td>
<td>300000 non-null</td>
<td>int64</td>
</tr>
<tr>
<td>Customer Name</td>
<td>300000 non-null</td>
<td>object (String)</td>
</tr>
<tr>
<td>Email</td>
<td>300000 non-null</td>
<td>object (String)</td>
</tr>
<tr>
<td>Order Date</td>
<td>300000 non-null</td>
<td>object (Datetime)</td>
</tr>
<tr>
<td>Ordered Items</td>
<td>300000 non-null</td>
<td>object (List of Strings)</td>
</tr>
<tr>
<td>Item Type</td>
<td>300000 non-null</td>
<td>object (String)</td>
</tr>
<tr>
<td>Total Bill</td>
<td>300000 non-null</td>
<td>float64</td>
</tr>
<tr>
<td>Actual Cost</td>
<td>300000 non-null</td>
<td>float64</td>
</tr>
<tr>
<td>Tax</td>
<td>300000 non-null</td>
<td>float64</td>
</tr>
<tr>
<td>Net Profit</td>
<td>300000 non-null</td>
<td>float64</td>
</tr>
<tr>
<td>Mode of Shopping</td>
<td>285776 non-null</td>
<td>object (String)</td>
</tr>
<tr>
<td>Coupon Code</td>
<td>285776 non-null</td>
<td>object (String)</td>
</tr>
<tr>
<td>Product Prices</td>
<td>300000 non-null</td>
<td>object (List of float64)</td>
</tr>
<tr>
<td>Ratings</td>
<td>300000 non-null</td>
<td>object (List of float64)</td>
</tr>
</tbody>
</table>

<br>
<p>Note that the Non-null values in some columns can vary than the provided values since the DatasetGen.py generates data at Random and can set more or less null values</p>
<h2>Key Analysis Points</h2>

<ul>
<li><strong>Probabilistic Analysis:</strong> Probability models are employed to understand the likelihood of specific events occurring, contributing to a deeper understanding of customer behavior.</li>
<li><strong>Market Basket Algorithm:</strong> Relational analysis is conducted using the Market Basket Algorithm, revealing associations between purchased items and guiding recommendations for item placement.</li>
<li><strong>Machine Learning Models:</strong> Predictive models are implemented to forecast probabilities and expected values of certain events, providing valuable insights for strategic decision-making.</li>
<li><strong>Financial Policy Deduction:</strong> The analysis includes the derivation of a financial policy with expectations for net profits, growth patterns, and the impact of coupon usage.</li>
</ul>

<h2>Usage</h2>

<p>Feel free to explore the Sales Data Analysis notebook and accompanying presentation and report to gain a comprehensive understanding of the insights derived from the sales data.</p>

<p><strong>Note:</strong> Ensure that you have the required dependencies installed to run the Jupyter Notebook successfully.</p>

<p>Happy analyzing!</p>


</body>
