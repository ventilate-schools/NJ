import os
import pandas as pd

# Load the data

trenton_schools = [
    {"school_name": "Trenton Central High School", "address": "400 Chambers St+Trenton+NJ 08609", "students": 2089, "website": "https://www.trenton.k12.nj.us/TrentonCentral.cfm", "phone": "TODO"},
    {"school_name": "Trenton Ninth Grade Academy", "address": "500 Perry Street+Trenton+NJ 08609", "students": 830, "website": "https://www.trenton.k12.nj.us/NinthGradeAcademy.cfm", "phone": "TODO"},
    {"school_name": "Daylight/Twilight High School", "address": "135 E Hanover St+Trenton+NJ 08618", "students": 400, "website": "https://www.trenton.k12.nj.us/DaylightTwilight.cfm", "phone": "TODO"},
    {"school_name": "Hedgepeth-Williams Middle School", "address": "301 Gladstone Ave+Trenton+NJ 08629", "students": 822, "website": "https://www.trenton.k12.nj.us/HedgepethWilliams.cfm", "phone": "TODO"},
    {"school_name": "Grace A. Dunn Middle School", "address": "401 Dayton St+Trenton+NJ 08610", "students": 921, "website": "https://www.trenton.k12.nj.us/DunnMiddle.cfm", "phone": "TODO"},
    {"school_name": "Dr. Martin Luther King Jr. Middle School", "address": "401 N Montgomery St+Trenton+NJ 08618", "students": 800, "website": "https://www.trenton.k12.nj.us/MLKJrMiddle.cfm", "phone": "TODO"},
    {"school_name": "Robeson Elementary School", "address": "212 S Logan Ave+Trenton+NJ 08609", "students": 400, "website": "https://www.trenton.k12.nj.us/Robeson.cfm", "phone": "TODO"},
    {"school_name": "Gregory Elementary School", "address": "500 Rutherford Ave+Trenton+NJ 08618", "students": 447, "website": "https://www.trenton.k12.nj.us/Gregory.cfm", "phone": "TODO"},
    {"school_name": "Franklin Elementary School", "address": "200 William St+Trenton+NJ 08610", "students": 374, "website": "https://www.trenton.k12.nj.us/Franklin.cfm", "phone": "TODO"},
    {"school_name": "Mott Elementary School", "address": "45 Stokely Ave+Trenton+NJ 08611", "students": 486, "website": "https://www.trenton.k12.nj.us/Mott.cfm", "phone": "TODO"},
    {"school_name": "Parker Elementary School", "address": "333 Fairgrounds Rd+Trenton+NJ 08618", "students": 500, "website": "https://www.trenton.k12.nj.us/Parker.cfm", "phone": "TODO"},
    {"school_name": "Wilson Elementary School", "address": "175 Girard Ave+Trenton+NJ 08638", "students": 466, "website": "https://www.trenton.k12.nj.us/Wilson.cfm", "phone": "TODO"},
    {"school_name": "Grant Elementary School", "address": "159 N Clinton Ave+Trenton+NJ 08609", "students": 574, "website": "https://www.trenton.k12.nj.us/Grant.cfm", "phone": "TODO"},
    {"school_name": "Harrison Elementary School", "address": "461 Genesee St+Trenton+NJ 08611", "students": 223, "website": "https://www.trenton.k12.nj.us/Harrison.cfm", "phone": "TODO"},
    {"school_name": "Robbins Elementary School", "address": "283 Tyler St+Trenton+NJ 08609", "students": 515, "website": "https://www.trenton.k12.nj.us/Robbins.cfm", "phone": "TODO"},
    {"school_name": "Washington Elementary School", "address": "331 Emory Ave+Trenton+NJ 08611", "students": 375, "website": "https://www.trenton.k12.nj.us/Washington.cfm", "phone": "TODO"},
    {"school_name": "Joyce Kilmer School", "address": "1300 Stuyvesant Ave+Trenton+NJ 08618", "students": 754, "website": "https://www.trenton.k12.nj.us/JoyceKilmer.cfm", "phone": "TODO"},
    {"school_name": "Columbus Elementary School", "address": "1200 Brunswick Ave+Trenton+NJ 08638", "students": 356, "website": "https://www.trenton.k12.nj.us/Columbus.cfm", "phone": "TODO"},
    {"school_name": "P.J. Hill Elementary School", "address": "1010 E State St+Trenton+NJ 08609", "students": 758, "website": "https://www.trenton.k12.nj.us/PJHill.cfm", "phone": "TODO"},
    {"school_name": "Luis Munoz-Rivera Middle School", "address": "400 N Montgomery St+Trenton+NJ 08618", "students": 500, "website": "https://www.trenton.k12.nj.us/MunozRivera.cfm", "phone": "TODO"}
]

west_windsor_plainsboro_schools = [
    {"school_name": "West Windsor-Plainsboro High School South", "address": "346 Clarksville Rd+Princeton Junction+NJ 08550", "students": 1600, "website": "https://www.west-windsor-plainsboro.k12.nj.us/south", "phone": "TODO"},
    {"school_name": "West Windsor-Plainsboro High School North", "address": "90 Grovers Mill Rd+Plainsboro+NJ 08536", "students": 1500, "website": "https://www.west-windsor-plainsboro.k12.nj.us/north", "phone": "TODO"},
    {"school_name": "Community Middle School", "address": "95 Grovers Mill Rd+Plainsboro+NJ 08536", "students": 1000, "website": "https://www.west-windsor-plainsboro.k12.nj.us/community", "phone": "TODO"},
    {"school_name": "Grover Middle School", "address": "10 Southfield Rd+Princeton Junction+NJ 08550", "students": 900, "website": "https://www.west-windsor-plainsboro.k12.nj.us/grover", "phone": "TODO"},
    {"school_name": "Dutch Neck Elementary School", "address": "392 Village Rd E+West Windsor+NJ 08550", "students": 700, "website": "https://www.west-windsor-plainsboro.k12.nj.us/dutchneck", "phone": "TODO"},
    {"school_name": "Millstone River School", "address": "75 Grovers Mill Rd+Plainsboro+NJ 08536", "students": 800, "website": "https://www.west-windsor-plainsboro.k12.nj.us/millstone", "phone": "TODO"},
    {"school_name": "Maurice Hawk Elementary School", "address": "303 Clarksville Rd+Princeton Junction+NJ 08550", "students": 600, "website": "https://www.west-windsor-plainsboro.k12.nj.us/hawk", "phone": "TODO"},
    {"school_name": "Town Center Elementary School", "address": "700 Wyndhurst Dr+Plainsboro+NJ 08536", "students": 500, "website": "https://www.west-windsor-plainsboro.k12.nj.us/towncenter", "phone": "TODO"}
]

ewing_schools = [
    {"school_name": "Ewing High School", "address": "900 Parkway Ave+Ewing+NJ 08618", "students": 1100, "website": "https://www.ewing.k12.nj.us/EHS", "phone": "TODO"},
    {"school_name": "Fisher Middle School", "address": "1325 Lower Ferry Rd+Ewing+NJ 08618", "students": 800, "website": "https://www.ewing.k12.nj.us/Fisher", "phone": "TODO"},
    {"school_name": "Antheil Elementary School", "address": "339 Ewingville Rd+Ewing+NJ 08638", "students": 700, "website": "https://www.ewing.k12.nj.us/Antheil", "phone": "TODO"},
    {"school_name": "Lore Elementary School", "address": "13 Westwood Dr+Ewing+NJ 08618", "students": 600, "website": "https://www.ewing.k12.nj.us/Lore", "phone": "TODO"},
    {"school_name": "Parkway Elementary School", "address": "446 Parkway Ave+Ewing+NJ 08618", "students": 500, "website": "https://www.ewing.k12.nj.us/Parkway", "phone": "TODO"}
]

hopewell_valley_schools = [
    {"school_name": "Hopewell Valley Central High School", "address": "259 Pennington Titusville Rd+Pennington+NJ 08534", "students": 1200, "website": "https://www.hvrsd.org/CentralHS", "phone": "TODO"},
    {"school_name": "Timberlane Middle School", "address": "51 S Timberlane Dr+Pennington+NJ 08534", "students": 1000, "website": "https://www.hvrsd.org/Timberlane", "phone": "TODO"},
    {"school_name": "Bear Tavern Elementary School", "address": "1162 Bear Tavern Rd+Titusville+NJ 08560", "students": 600, "website": "https://www.hvrsd.org/BearTavern", "phone": "TODO"},
    {"school_name": "Hopewell Elementary School", "address": "35 Princeton Ave+Hopewell+NJ 08525", "students": 500, "website": "https://www.hvrsd.org/Hopewell", "phone": "TODO"},
    {"school_name": "Stony Brook Elementary School", "address": "20 Stephenson Rd+Pennington+NJ 08534", "students": 450, "website": "https://www.hvrsd.org/StonyBrook", "phone": "TODO"},
    {"school_name": "Toll Gate Grammar School", "address": "275 S Main St+Pennington+NJ 08534", "students": 400, "website": "https://www.hvrsd.org/TollGate", "phone": "TODO"}
]

east_windsor_schools = [
    {"school_name": "Hightstown High School", "address": "25 Leshin Lane+Hightstown+NJ 08520", "students": 1500, "website": "https://www.ewrsd.org/HHS", "phone": "TODO"},
    {"school_name": "Kreps Middle School", "address": "5 Kent Lane+East Windsor+NJ 08520", "students": 1200, "website": "https://www.ewrsd.org/Kreps", "phone": "TODO"},
    {"school_name": "Perry L. Drew Elementary School", "address": "70 Twin Rivers Dr+East Windsor+NJ 08520", "students": 800, "website": "https://www.ewrsd.org/Drew", "phone": "TODO"},
    {"school_name": "Melvin H. Kreps School", "address": "5 Kent Lane+East Windsor+NJ 08520", "students": 900, "website": "https://www.ewrsd.org/Kreps", "phone": "TODO"},
    {"school_name": "Ethel McKnight Elementary School", "address": "58 Twin Rivers Dr+East Windsor+NJ 08520", "students": 700, "website": "https://www.ewrsd.org/McKnight", "phone": "TODO"},
    {"school_name": "Grace N. Rogers Elementary School", "address": "380 Stockton St+Hightstown+NJ 08520", "students": 600, "website": "https://www.ewrsd.org/Rogers", "phone": "TODO"},
    {"school_name": "Walter C. Black Elementary School", "address": "371 Stockton St+Hightstown+NJ 08520", "students": 500, "website": "https://www.ewrsd.org/Black", "phone": "TODO"}
]

lawrence_township_schools = [
    {"school_name": "Lawrence High School", "address": "2525 Princeton Pike+Lawrenceville+NJ 08648", "students": 1100, "website": "https://www.ltps.org/LHS", "phone": "TODO"},
    {"school_name": "Lawrence Middle School", "address": "2455 Princeton Pike+Lawrenceville+NJ 08648", "students": 900, "website": "https://www.ltps.org/LMS", "phone": "TODO"},
    {"school_name": "Lawrence Intermediate School", "address": "66 Eggerts Crossing Rd+Lawrenceville+NJ 08648", "students": 800, "website": "https://www.ltps.org/LIS", "phone": "TODO"},
    {"school_name": "Ben Franklin Elementary School", "address": "2939 Princeton Pike+Lawrenceville+NJ 08648", "students": 600, "website": "https://www.ltps.org/BenFranklin", "phone": "TODO"},
    {"school_name": "Eldridge Park Elementary School", "address": "55 Lawn Park Ave+Lawrenceville+NJ 08648", "students": 500, "website": "https://www.ltps.org/EldridgePark", "phone": "TODO"},
    {"school_name": "Lawrenceville Elementary School", "address": "40 Craven Ln+Lawrenceville+NJ 08648", "students": 400, "website": "https://www.ltps.org/Lawrenceville", "phone": "TODO"},
    {"school_name": "Slackwood Elementary School", "address": "2060 Princeton Pike+Lawrenceville+NJ 08648", "students": 300, "website": "https://www.ltps.org/Slackwood", "phone": "TODO"}
]

princeton_schools = [
    {"school_name": "Princeton High School", "address": "151 Moore St+Princeton+NJ 08540", "students": 1600, "website": "https://www.princetonk12.org/PHS", "phone": "TODO"},
    {"school_name": "John Witherspoon Middle School", "address": "217 Walnut Ln+Princeton+NJ 08540", "students": 800, "website": "https://www.princetonk12.org/JohnWitherspoon", "phone": "TODO"},
    {"school_name": "Community Park Elementary School", "address": "372 Witherspoon St+Princeton+NJ 08540", "students": 400, "website": "https://www.princetonk12.org/CommunityPark", "phone": "TODO"},
    {"school_name": "Littlebrook Elementary School", "address": "39 Magnolia Ln+Princeton+NJ 08540", "students": 350, "website": "https://www.princetonk12.org/Littlebrook", "phone": "TODO"},
    {"school_name": "Riverside Elementary School", "address": "58 Riverside Dr+Princeton+NJ 08540", "students": 375, "website": "https://www.princetonk12.org/Riverside", "phone": "TODO"},
    {"school_name": "Johnson Park Elementary School", "address": "285 Rosedale Rd+Princeton+NJ 08540", "students": 450, "website": "https://www.princetonk12.org/JohnsonPark", "phone": "TODO"}
]

hamilton_township_schools = [
    {"school_name": "Hamilton High School West", "address": "2720 S Clinton Ave+Hamilton+NJ 08610", "students": 1200, "website": "https://www.htsdnj.org/West", "phone": "TODO"},
    {"school_name": "Nottingham High School North", "address": "1055 Klockner Rd+Hamilton+NJ 08619", "students": 1300, "website": "https://www.htsdnj.org/North", "phone": "TODO"},
    {"school_name": "Steinert High School East", "address": "2900 Klockner Rd+Hamilton+NJ 08690", "students": 1400, "website": "https://www.htsdnj.org/East", "phone": "TODO"},
    {"school_name": "Grice Middle School", "address": "901 White Horse Hamilton Square Rd+Hamilton+NJ 08610", "students": 800, "website": "https://www.htsdnj.org/Grice", "phone": "TODO"},
    {"school_name": "Reynolds Middle School", "address": "2145 Yardville Hamilton Square Rd+Hamilton+NJ 08690", "students": 850, "website": "https://www.htsdnj.org/Reynolds", "phone": "TODO"},
    {"school_name": "Emily C. Reynolds Middle School", "address": "2145 Yardville Hamilton Square Rd+Hamilton+NJ 08690", "students": 850, "website": "https://www.htsdnj.org/Reynolds", "phone": "TODO"},
    {"school_name": "Albert E. Grice Middle School", "address": "901 White Horse Hamilton Square Rd+Hamilton+NJ 08610", "students": 800, "website": "https://www.htsdnj.org/Grice", "phone": "TODO"},
    {"school_name": "Richard C. Crockett Middle School", "address": "2631 Kuser Rd+Hamilton+NJ 08691", "students": 900, "website": "https://www.htsdnj.org/Crockett", "phone": "TODO"},
    {"school_name": "Alexander Elementary School", "address": "20 Robert Frost Dr+Hamilton+NJ 08690", "students": 500, "website": "https://www.htsdnj.org/Alexander", "phone": "TODO"},
    {"school_name": "Greenwood Elementary School", "address": "2069 Greenwood Ave+Hamilton+NJ 08609", "students": 450, "website": "https://www.htsdnj.org/Greenwood", "phone": "TODO"},
    {"school_name": "Klockner Elementary School", "address": "830 Klockner Rd+Hamilton+NJ 08619", "students": 400, "website": "https://www.htsdnj.org/Klockner", "phone": "TODO"},
    {"school_name": "Kuser Elementary School", "address": "70 Newkirk Ave+Hamilton+NJ 08629", "students": 350, "website": "https://www.htsdnj.org/Kuser", "phone": "TODO"},
    {"school_name": "Langtree Elementary School", "address": "2080 Whatley Rd+Hamilton+NJ 08690", "students": 300, "website": "https://www.htsdnj.org/Langtree", "phone": "TODO"},
    {"school_name": "Lalor Elementary School", "address": "25 Barnt Deklyn Rd+Hamilton+NJ 08610", "students": 320, "website": "https://www.htsdnj.org/Lalor", "phone": "TODO"},
    {"school_name": "Mercerville Elementary School", "address": "60 Regina Ave+Hamilton+NJ 08619", "students": 370, "website": "https://www.htsdnj.org/Mercerville", "phone": "TODO"},
    {"school_name": "Morgan Elementary School", "address": "38 Princeton Ave+Hamilton+NJ 08619", "students": 360, "website": "https://www.htsdnj.org/Morgan", "phone": "TODO"},
    {"school_name": "Robinson Elementary School", "address": "494 Donald Dr+Hamilton+NJ 08610", "students": 340, "website": "https://www.htsdnj.org/Robinson", "phone": "TODO"},
    {"school_name": "Sayen Elementary School", "address": "3333 Nottingham Way+Hamilton+NJ 08690", "students": 310, "website": "https://www.htsdnj.org/Sayen", "phone": "TODO"},
    {"school_name": "Sunnybrae Elementary School", "address": "166 Elton Ave+Hamilton+NJ 08620", "students": 300, "website": "https://www.htsdnj.org/Sunnybrae", "phone": "TODO"},
    {"school_name": "University Heights Elementary School", "address": "645 Paxson Ave+Hamilton+NJ 08619", "students": 450, "website": "https://www.htsdnj.org/UniversityHeights", "phone": "TODO"},
    {"school_name": "Yardville Elementary School", "address": "450 Yardville Allentown Rd+Hamilton+NJ 08620", "students": 410, "website": "https://www.htsdnj.org/Yardville", "phone": "TODO"},
    {"school_name": "Yardville Heights Elementary School", "address": "3880 S Broad St+Hamilton+NJ 08620", "students": 390, "website": "https://www.htsdnj.org/YardvilleHeights", "phone": "TODO"}
]

# Combine all school lists into one DataFrame
all_schools = (trenton_schools + west_windsor_plainsboro_schools + ewing_schools + hopewell_valley_schools + east_windsor_schools + hamilton_township_schools + lawrence_township_schools + princeton_schools)
schools_data = pd.DataFrame(all_schools)

# Adjust the address column to replace "+" with ", "
schools_data['address'] = schools_data['address'].str.replace('+', ', ', regex=False)

# Define the output directory for the markdown files
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

# Adding district names to the DataFrame
districts = [
    ("Trenton Public Schools", trenton_schools),
    ("West Windsor-Plainsboro Regional School District", west_windsor_plainsboro_schools),
    ("Ewing Public Schools", ewing_schools),
    ("Hopewell Valley Regional School District", hopewell_valley_schools),
    ("East Windsor Regional School District", east_windsor_schools),
    ("Hamilton Township Schools", hamilton_township_schools),
    ("Lawrence Township Schools", lawrence_township_schools),
    ("Princeton School District", princeton_schools)
]

# Assign district names to each row in the DataFrame
schools_data['district_name'] = ""
for district_name, schools_list in districts:
    for school in schools_list:
        schools_data.loc[schools_data['school_name'] == school['school_name'], 'district_name'] = district_name


# Function to generate markdown files
def generate_markdown_by_index(row):
    # Simplify the school name for the directory and file
    district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
    path = os.path.join(output_dir, district_name_simple)
    os.makedirs(path, exist_ok=True)

    # Filename for the markdown
    file_path = os.path.join(path, f"{school_name_simple}.md")

    # Markdown content with front-matter and details
    with open(file_path, 'w') as file:
        file.write(f"---\nlayout: page\ntitle: {row['school_name']}\n---\n")  # School Name
        file.write(
            f"# Navigation\n\n[[All countries/states/provinces]](../../..) > [[All New Jersey Counties]](../..) > [[All schools in district]](..)\n\n")

        file.write(f"# {row['school_name']} ({row['district_name']})\n\n")  # School Name and area as header

        # Loop through keys per school
        for key, value in row.items():
            if key not in ['district_name', 'school_name']:
                file.write(f"**{key.replace('_', ' ').title()}**: {value}\n\n")

        file.write(f"**School's overall airborne virus protection grade (0-5)**: 0\n\n")
        file.write(f"**Discord, Facebook, or WhatsApp group for discovery/advocacy for THIS school**: TODO\n\n")
        file.write(f"**School's policy on Ventilation**: TODO\n\n")
        file.write(f"**School's Ventilation Work Completion**: TODO\n\n")
        file.write(f"**School's Air-Purification**: TODO\n\n")
        file.write(f"**School's CO2 monitoring to actively drive ventilation and filtration**: TODO\n\n")
        file.write(f"**School's Wikidata URL**: TODO")
        file.write(f"\n\n\n[Edit this page](https://github.com/ventilate-schools/NJ/edit/main/{file_path}).")
        file.write(f" See also [rules for contribution](../../../contribution-rules/)")


# Generate markdown files for each school
schools_data.apply(generate_markdown_by_index, axis=1)


def create_area_and_root_index():
    # Create a dictionary to keep track of schools in each district
    districts_dict = {}

    for index, row in schools_data.iterrows():
        district_name_simple = row['district_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")
        school_name_simple = row['school_name'].replace(" ", "_").replace("/", "_").replace("\\", "_")

        # Check if the district already exists in the dictionary
        if district_name_simple not in districts_dict:
            districts_dict[district_name_simple] = []

        # Append the school name to the district's list
        districts_dict[district_name_simple].append(school_name_simple)

    # Write an index markdown file for each district and gather data for root index
    root_index_content = "---\ntitle: Schools in New Jersey and their ventilation status\n---\n"

    root_index_content += (
        "\n# Navigation\n\n[[All countries/states/provinces]](..)\n\n# Purpose of site\n\nGiven **COVID-19 is Airborne** and the world is pushing to better ventilate "
        "schools for long term student and teacher health, we're tracking the "
        "progress for that in New Jersey. This is ahead of government effort to do the same. If government starts to "
        "track this work, this effort will continue because that effort might be weak."
        "We're guided by 33 profs and PhDs who are pushing for a policy change in a "
        "March 2024 article on **Science.org**: [Mandating indoor air quality for public buildings](https://drive.google.com/file/d/16l_IH47cQtC7fFuafvHca7ORNVGITxx8/view). "
        "Not only active ventilation (which should "
        "be mechanical heat recovery type in this age), but air filtration/purification "
        "too and CO2 monitoring to drive ventilation levels, as CO2 inside is a proxy indicator "
        "for COVID risk. As it happens the WHO also have a [2023 airborne risk assessment guide](https://iris.who.int/handle/10665/376346)\n\n"
        "Know that other diseases are airborne too: Measles "
        "(studies [1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2810934/pdf/10982072.pdf) "
        "[2](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3880795/pdf/nihms532643.pdf) "
        "[3](https://pubmed.ncbi.nlm.nih.gov/31257413/) "
        "[4](https://www.sciencedirect.com/science/article/pii/S0196655316305363)), "
        "Influenza, RSV and TB. The same "
        "ventilation and air filtration measures reduce transmission of those too.\n\n When we say "
        "student and teacher health, we're wanting absences to go down too. If we lower "
        "transmission in schools, we reduce multi-generation transmission too, as kids bring "
        "infections home to parents. With lowered transmission, we also reduce long COVID, "
        "where the worst sufferers have disappeared from education and the workplace.\n\n")

    root_index_content += (
        "\n## Leaderboard\n\n1. to be announced\n2. to be announced\n3. to be announced\n4. to be announced\n5. to be announced\n\n")

    root_index_content += ("{% include_relative grade.html %}\n\n")

    root_index_content += ("# New Jersey School Districts:\n\n")

    for district, schools in districts_dict.items():
        district_index_file_path = os.path.join(output_dir, district, "index.md")
        os.makedirs(os.path.join(output_dir, district), exist_ok=True)

        with open(district_index_file_path, 'w') as district_index_file:
            district_index_file.write(f"---\nlayout: page\ntitle: Schools in {district.replace('_', ' ')}\n---\n")
            district_index_file.write(
                f"# Navigation\n\n[[All countries/states/provinces]](../..) > [[All New Jersey Counties]](..)\n\n")
            district_index_file.write(f"# Schools in {district.replace('_', ' ')}\n\n")
            district_index_file.write("{% include_relative grade.html %}\n\n")
            district_index_file.write(f"**Schools:**\n\n")
            for school in schools:
                school_file_path = school
                district_index_file.write(f"- [{school.replace('_', ' ')}]({school_file_path}.md)\n")

        # Add to root index content with cleaner URLs
        root_index_content += f"- [{district.replace('_', ' ')}]({district}/): {len(schools)} schools\n"

    root_index_content += ("\n\n# Site ownership\n\nThis site is edited by volunteers who're "
                           "interested in accelerating the work to complete the adequate ventilation of New Jersey schools. "
                           "This effort was not commissioned by education authorities or government.\n\n"
                           "[Edit this page](https://github.com/ventilate-schools/NJ/edit/main/index.md). See also [rules for contribution](./contribution_rules/)")

    # Write the root index file
    root_index_path = os.path.join(output_dir, "index.md")
    with open(root_index_path, 'w') as root_index_file:
        root_index_file.write(root_index_content)


# Call the function to create index markdown files and root index
create_area_and_root_index()

# Print confirmation
print("Index markdown files with front matter and links have been created in each area directory and root directory.")
