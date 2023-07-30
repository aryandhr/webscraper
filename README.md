# webscraper

## Motivation

The inspiration for this project stems from a practical need to address a specific challenge encountered during the spring semester of my junior year in college. In a course where attendance was a significant component of the final grade, students were required to bring their laptops to class and log into a website that tracked their presence through location data. Additionally, multiple-choice questions were presented at various intervals during the lecture through this website, and a minimum of 75% questions asked that had to be answered to obtain attendance points. Luckily, the answers did not need to be correct; mere participation demonstrated one's presence.

Unfortunately, my laptop's battery health was not optimal, and it unexpectedly shut down during my first lecture, leaving me unable to participate in the attendance tracking process. Attempting to switch to my phone as an alternative proved futile due to the website's non-responsive nature, resulting in a loss of attendance points for that particular day.

This sparked a realization that there had to be a more reliable and efficient approach to fulfill the attendance requirement while still attending the lectures.

Thus, through the utilization of the Selenium library, the script allowed for custom geolocation data to be passed to the website and automated the processes of logging into the website, parse the html elements to recognize answer tags when they appeared, and pick a random multiple-choice option to emulate human-like guessing, providing a fully automated solution.

## Requirements

1. Python 3.x: The script requires Python 3.x to be installed on the system.
2. Selenium: The project utilizes the Selenium library, so users need to have it installed in their Python environment.
3. Web Drivers: Since Selenium interacts with web browsers, users need to have the appropriate web drivers installed for the browsers they wish to automate (e.g., ChromeDriver for Chrome, GeckoDriver for Firefox).

## License

This project is licensed under the Apache License. Feel free to use, modify, and distribute the code as per the terms of the license.

## Disclaimer

The project is intended for educational and personal use only. This script was used ethically as the author diligently attended every lecture, a commitment exemplified by the attainment of a perfect 4.0 grade in the class. It is essential to underscore that this outstanding academic achievement would not have been conceivable without regular attendance, dedicated effort in studying, and earnest attention during the lectures.

## Acknowledgments

The author expresses their gratitude to the developers of the Selenium library and the open-source community for their valuable contributions.

## Contact

For any inquiries or questions regarding the project, please contact dhararya@msu.edu.

