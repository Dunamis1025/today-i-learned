Quiz: Real Estate Listing Manager

Create a program to manage real estate listings using a class.

Requirements:

Create a House class.

The constructor (__init__) should receive:

location, house type, deal type, price, year built

Implement a show_detail() method that prints the listing information in one line.

Create at least three different house listings.

Store all listings in a list.

Print the total number of listings and display the details of each one using a loop.


# ==================================================
# Quiz: Real Estate Listing Manager (OOP Practice)
#
# Goal:
# - Practice creating a class
# - Store multiple objects in a list
# - Use a loop to display object information
# ==================================================

class House:
    # --------------------------------------------------
    # Constructor: initializes a real estate listing
    #
    # location:     City or area where the house is located
    # house_type:   Type of property (Apartment, Condo, House)
    # deal_type:    Type of deal (For Sale, For Rent)
    # price:        Price or rent information
    # year_built:   Year the building was completed
    # --------------------------------------------------
    def __init__(self, location, house_type, deal_type, price, year_built):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year_built = year_built

    # --------------------------------------------------
    # Display listing details in a single line
    # --------------------------------------------------
    def show_detail(self):
        print(
            self.location,
            self.house_type,
            self.deal_type,
            self.price,
            self.year_built
        )


# --------------------------------------------------
# Store multiple house listings in a list
# --------------------------------------------------
houses = []

# Create house listing objects
house1 = House("Gangnam, Seoul", "Apartment", "For Sale", "$800,000", 2015)
house2 = House("Brooklyn, New York", "Condo", "For Rent", "$3,200/month", 2012)
house3 = House("Sydney CBD", "Studio", "For Rent", "$550/week", 2008)

# Add listings to the list
houses.append(house1)
houses.append(house2)
houses.append(house3)

# --------------------------------------------------
# Print total number of listings
# --------------------------------------------------
print(f"Total {len(houses)} property listings available.")

# Print details of each listing
for house in houses:
    house.show_detail()


Total 3 property listings available.
Gangnam, Seoul Apartment For Sale $800,000 2015
Brooklyn, New York Condo For Rent $3,200/month 2012
Sydney CBD Studio For Rent $550/week 2008

