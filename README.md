# Housing-Price-Python-EDA-

The code starts by importing the necessary libraries, such as pandas, numpy, matplotlib.pyplot, and seaborn. It then reads in the data from a CSV file named 'kc_house_data.csv' using pandas and assigns it to a variable named 'df'. The head() method is then used to display the first few rows of the dataframe.

The info() method is then used to print information about the dataframe, such as the number of rows and columns, the data types of the columns, and the memory usage.

The describe() method is then used to display a statistical summary of the data, including the count, mean, standard deviation, minimum, and maximum values of each numerical column.

The 'id' column is then dropped from the dataframe using the drop() method with the 'axis=1' parameter to indicate that we want to drop a column. The 'inplace=True' parameter is also used to indicate that the changes should be made to the dataframe in place.

The code then creates a heatmap using the seaborn library to visualize the correlations between different features of the data. The heatmap shows the correlation coefficients between all pairs of features in the data. The 'annot=True' parameter is used to display the correlation coefficients on the heatmap.

The duplicated() method is then used to check for any duplicate rows in the dataframe. The method returns a boolean array indicating whether each row is a duplicate or not. The sum() method is then used to count the number of True values in the array, which gives us the total number of duplicate rows in the dataframe.

The seaborn library is then used to create boxplots to visualize the relationship between the price and other features such as the number of bedrooms and bathrooms. The y-axis represents the price, while the x-axis represents the number of bedrooms or bathrooms.

Finally, the code creates a bar plot using the matplotlib library to compare the average price of waterfront and non-waterfront properties. The value_counts() method is then used to count the frequency of the number of bedrooms in the dataframe, and the result is printed to the console.
