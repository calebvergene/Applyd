import json

def fix_locations():
        """
        Function to replace job applications that contain multiple locations with a single string
        """
        with open('server/application_data/extracted_swe_jobs.json', 'r') as file:
                all_applications = json.load(file)
                for app in all_applications:
                        if '\n' in app['location']:
                                app['location'] = 'Multi Location'
                
        with open('server/application_data/extracted_swe_jobs.json', 'w') as file:
                json.dump(all_applications, file, indent=4)

def add_swe_field():
        """
        Added "SWE" tag to all SWE jobs to scale for the future
        """
        with open('server/application_data/extracted_swe_jobs.json', 'r') as file:
                all_applications = json.load(file)
                for app in all_applications:
                        app['field'] = 'software_engineer'
                
        with open('server/application_data/extracted_swe_jobs.json', 'w') as file:
                json.dump(all_applications, file, indent=4)
