# WineSense
A Comprehensive Dashboard for Assessing Wine Quality

## Author

-   Ashwin Babu

## Link to the app

https://winesense.onrender.com/

## Overview 

This repository hosts the dashboard for Wine data released by [*Kaggle*](https://www.kaggle.com/datasets/zynicide/wine-reviews). The motivation, purpose, description of data and research question can be found in our [proposal](https://github.com/ashwin2507/WineSense/blob/main/docs/proposal.md).

## Usage 

This dashboard is designed to help wine enthusiasts and industry professionals gain valuable insights into the world of wine. With its three visualizations, users can explore the following questions:

1. What is the percentage of wines produced in a specific province and how does it compare to other provinces? This information can help users understand the relative importance of each province in terms of wine production and identify provinces that may be worth exploring further.

2. Which countries produce the most wines in the dataset and how does their production volume compare to other countries? This visualization provides a high-level view of wine production around the world and can help users identify regions that are particularly important in the industry.

3. How does the price distribution of wines vary across different provinces and wine varieties? This information can help users understand the price ranges for different types of wines and identify wines that may be overpriced or under priced relative to other wines in the same category.

The dashboard also provides users with various filtering options, including the ability to select a specific province of interest and specific wine variety of interest. This feature can help users identify patterns in the data that may not be immediately obvious and gain a deeper understanding of the industry.

Overall, this dashboard provides a user-friendly interface that enables users to explore wine production data easily and gain valuable insights into the industry. It is a useful tool for anyone who is interested in wine, from casual enthusiasts to industry professionals.

The 3 types of visualizations included are:
- A line plot showing the percentage of wines by variety that comes from the selected province. 
- A world map that shows the number of wines coming from different countries that are contained in our dataset.
- A box plot of the price of wine according to the selected type of wine and province by the user.

*The brief questions answered by this dashboard would be:* 
- As a wine connoisseur any user would be curious to know about the price distribution of type of wine given a province user is interested in.
- Which countries produce the most wines.
- How does the price distribution of wines vary between different provinces.

<br>

## Get involved 

**How to run the app locally and make contributions**

If you would like to contribute to our project, please read the CONTRIBUTING.md file and then follow these steps: 
- Ensure that you have python3 installed on your computer.
- Fork the repository and [clone](https://github.com/ashwin2507/WineSense.git) it onto your computer.
- Create a new branch (named according to the specifications in the CONTRIBUTING.md file).

 *To run the app locally:* 

- Navigate to the source directory of the repository on the location machine.
- Ensure all the necessary packages are installed:

    `pip3 install -r requirements.txt`

- Execute the following command in a bash terminal:

    `python3 app.py`

*To propose new changes:* 
- Fork the repository
- Make your changes to the code and adhere to best coding practices. 
- Commit your changes (with an informative commit message).
- Push your changes to your fork - Submit a pull request.

**Places for improvement** 
- Build upon the current map plot and add interactive elements to the plot, work on the wine distribution given province plot this could be improved in the future. 

## Contributing 

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License 

`WineSense` was created using Dash visualization by Jenit Jain. It is licensed under the terms of the [MIT license](LICENSE).

## References

- [Dataset](https://www.kaggle.com/datasets/zynicide/wine-reviews)