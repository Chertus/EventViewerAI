import sys
import json
import xml.etree.ElementTree as ET

def parse_event_log(file_path):
    # Assuming the file is in XML format
    tree = ET.parse(file_path)
    root = tree.getroot()

    logs = []
    for event in root.findall('.//Event'):
        logs.append({
            "TimeCreated": event.find('.//TimeCreated').attrib.get('SystemTime'),
            "EventID": event.find('.//EventID').text,
            "Level": event.find('.//Level').text,
            "Source": event.find('.//Provider').attrib.get('Name'),
            "Message": event.find('.//Message').text if event.find('.//Message') is not None else ""
        })

    return logs

def main():
    if len(sys.argv) != 2:
        print("Usage: Drag and drop an Event Viewer XML file onto this script.")
        return

    file_path = sys.argv[1]
    log_data = parse_event_log(file_path)

    if log_data:
        output_file = "parsed_event_logs.json"
        with open(output_file, "w") as file:
            json.dump(log_data, file, indent=4)
        print(f"Event logs saved to {output_file}")
    else:
        print("Failed to parse event logs.")

if __name__ == "__main__":
    main()
