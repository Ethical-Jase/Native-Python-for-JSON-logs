import json

# List of file paths
file_paths = [r"C:\Users\jason\Desktop\Native Python\Insights.json",
              r"C:\Users\jason\Desktop\Native Python\Mary.json",
              r"C:\Users\jason\Desktop\Native Python\Mateo.json",
              r"C:\Users\jason\Desktop\Native Python\Nikki.json",
              r"C:\Users\jason\Desktop\Native Python\Paulo.json",
              r"C:\Users\jason\Desktop\Native Python\Saanvi.json",
              r"C:\Users\jason\Desktop\Native Python\Terry.json"]


# Iterate through each JSON log file
for file_path in file_paths:
    with open(file_path, 'r') as file:
        log_dict = json.load(file)

        # Process the data for the current file
        for log_list in log_dict.values():
            for log_entry in log_list:
                # Example to print eventTime
                print(log_entry["eventTime"])

                # Example to print specific awsRegion
                if log_entry["awsRegion"] == "us-east-1":
                    print(log_entry["awsRegion"])

                # Example to print the whole dict if specific eventID is found
                if log_entry["eventID"] == "9357a8cc-a0eb-46a1-b67e-EXAMPLE19b14":
                    print(log_entry)
