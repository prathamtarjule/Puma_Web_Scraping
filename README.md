# Puma_Web_Scraping

I dont know why my output data is not written in the csv file. The code is running successfully. Any suggestions ?

Challenges one can face while webscraping .

1.Website changes: The website's HTML structure or CSS classes could change, making it difficult to extract the data using the existing code. In this case, you would need to update the code to reflect the new HTML structure.

2.JavaScript content: If the website uses JavaScript to load or modify the content, you might need to use a tool like Selenium or Splash to simulate a web browser and extract the data. This can add complexity to the code and slow down the scraping process.

3.Data cleaning: The extracted data might contain extra whitespace, special characters, or other formatting issues that need to be cleaned up before saving to a CSV file. You would need to add additional code to handle these data cleaning tasks.

4.Error handling: The code should handle errors gracefully, such as when the website is down or when there is a network error. The code should also check that the extracted data is valid before saving it to a CSV file.

5.File permissions: The code might not have permission to write to the desired CSV file location, especially if running on a shared network drive or in a Docker container. You would need to ensure that the code has the necessary permissions to write to the file location.
