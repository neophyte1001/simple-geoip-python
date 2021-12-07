# Importing tkinter
from tkinter import *

# Importing <simple-geoip> module to get geolocation using ip address via API call.
from simple_geoip import GeoIP

from simple_geoip.exceptions import ServiceError

# Creating main window

root = Tk()               # Creating the window
root.geometry("400x450")  # Setting main window
root.title("GeoIp v2.4")  # Setting window title


# Sample Data returned by the API call
# {'ip': '120.138.121.205',
# 'location': {
# 'country': 'IN',
# 'region': 'State of Maharashtra',
# 'city': 'Andheri East',
# 'lat': 19.11446,
# 'lng': 72.8712,
# 'postalCode': '',
# 'timezone': '+05:30',
# 'geonameId': 7798655
# },
#  'as': {
#  'asn': 45194,
#  'name': 'Syscon Infoway',
#  'route': '120.138.121.0/24',
#  'domain': 'http://www.sysconinfoway.com',
#  'type': 'Cable/DSL/ISP'
#  },
#  'isp': 'Syscon Infoway Pvt. Ltd.',
#  'connectionType': ''
#  }

# Purpose:
# 1. geo.lookup('ip address') this takes ip address as parameter and returns information in "dict" format.
# 2. <get_location()> first gets the ip address entered by the user and pass it to <geo.lookup()> to get <data>
# 3. Now, we will extract information needed to us like (ip,country,region,city) from the data using dictionary's get method
# 4. Finally creating the label with the parameters and displaying it.

# ----------Using own written logic

def isValid(ip):
    """
    Checks if ip address is valid or not
    :param ip: Takes ip as string
    :return: True if ip valid hence not
    """

    # Check dots and null
    no_of_dots = ip.count(".")   # Counts no of dots in string
    if ip == '' or no_of_dots != 3:  # If ip is blank or  dots!=3 returns False
        return False

    # Check alphabet
    for i in ip:
        if i.isalpha():
            return False

    ip_separated = ip.split(".")   # Splits string to list
    print(len(ip_separated))

    # Check if the individual numbers of ip is in the range (0 < ip < 255)
    for i in range(len(ip_separated)):
        if int(ip_separated[i]) < 0 or int(ip_separated[i]) > 255:
            return False
    return True


def get_location():
    """
    Takes user's entered ip and returns geolocation data
    :return: Prints data if ip valid hence prints errors
    """
    # Checking
    user_ip = ip_input.get()  # Getting ip-address entered by user
    if isValid(user_ip):
        error_msg.configure(text="")
        print(user_ip)
        API_KEY = "at_FjxPOnVGsA9Yfu4keSODAdBSgPqvS"  # Private API key
        geo = GeoIP(API_KEY)
        try:
            data = geo.lookup(user_ip)  # Getting the data
            print(data)

            # Parameters
            ip = user_ip
            country = data.get('location').get('country')
            region = data.get('location').get('region')
            city = data.get('location').get('city')

            ip_info.configure(text=f"Your ip Address is {ip}", font=("Poppins", 8))
            location_info.configure(text=f"Location: {city}, {region}, {country}", font=("Poppins", 8))

        except ServiceError or ConnectionError:
            error_msg.configure("Please connect to the internet!")

    else:
        error_msg.configure(text="Invalid IP address, Check once again")


# Colors
bgColor = '#03001e'
fgColor = '#fff'
btnBg = '#7303c0'
btnFg = '#fff'
detailsBg = '#fdeff9'

if __name__ == '__main__':

    # Background Canvas (Main)
    main_canvas = Canvas(root, bg=bgColor, height=450, width=400)
    main_canvas.place(x=0, y=0)

    # Project Title
    main_title = Label(text="Geo-IP Lookup", font=("Poppins", 24), bg=bgColor, fg=fgColor)
    main_title.place(x=90, y=30)

    # Ip Address Label
    ip_label = Label(root, text="Enter your ip", bg=bgColor, fg=fgColor, font=('Poppins', 12))
    ip_label.place(x=80, y=100)

    # Ip Address Entry
    ip_input = Entry(root, borderwidth=0, font=('Poppins', 14))
    ip_input.place(x=80, y=125)

    # Submit Button
    submit = Button(root, text="Get Location", command=get_location, bg="#7303c0", fg="#fff", padx=10, pady=8,
                    font=('Poppins', 10))
    submit.place(x=150, y=160)

    # Details Canvas
    show_canvas = Canvas(root, width=300, height=180, bg="#fdeff9")
    show_canvas.place(x=50, y=220)

    # To show
    ip_info = Label(root, text=f"Your ip Address is 1.1.1.1", font=("Poppins", 8))
    ip_info.place(x=60, y=230)
    location_info = Label(root, text=f"Location: XY, ABC, HIK", font=("Poppins", 8))
    location_info.place(x=60, y=250)

    # Error messages
    error_msg = Label(root, text="", font=("Poppins", 8), bg=bgColor, fg='red')
    error_msg.place(x=215, y=105)

    # Exit Button
    exit_btn = Button(text="Exit", font=("Poppins", 10), bg='grey', fg='#fff', borderwidth=0, command=root.destroy)
    exit_btn.place(x=190, y=410)

    # Running the window
    root.mainloop()
