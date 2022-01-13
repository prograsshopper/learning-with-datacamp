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



survey_data = pd.read_excel("fcc_survey_subset.xlsx")
# Count NA values in each column
survey_data.isna().sum()
# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("fcc_survey_subset.xlsx",
                            dtype={'HasDebt': bool})
# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel(
    "fcc_survey_yn_data.xlsx",
    dtype={
        "HasDebt": bool,
        "AttendedBootCampYesNo": bool
        },
    true_values=["Yes"],
    false_values=["No"],
                            )

# View the data
print(survey_subset.head())

# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel("fcc_survey.xlsx", parse_dates=["Part1StartTime"])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

# Create dict of columns to combine into new datetime column
datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}
# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel("fcc_survey_dts.xlsx",
                            parse_dates=datetime_cols)
# View summary statistics about Part2Start
print(survey_data.Part2Start.describe())

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                   format="%m%d%Y %H:%M:%S")