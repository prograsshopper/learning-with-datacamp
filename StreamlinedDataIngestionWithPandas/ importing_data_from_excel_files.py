# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel("fcc_survey.xlsx")

# View the head of the dataframe
print(survey_responses[:5])

# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows=2,
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

# Create df from second worksheet by referencing its position
responses_2017 = pd.read_excel(
    "fcc_survey.xlsx",
    sheet_name=1
    )

responses_2017 = pd.read_excel(
    "fcc_survey.xlsx",
    sheet_name="2017")

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=["2016", "2017"])
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0, "2017"])
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=None)

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for sheet_name, df in responses.items():
    # Print the number of rows being added
    print("Adding {0} rows".format(sheet_name))
    # Append df to all_responses, assign result
    all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

