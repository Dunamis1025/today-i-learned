import pickle  # Module for saving and loading Python objects using serialization

# ===============================
# 1️⃣ Save an object to a file
# ===============================

# "wb" = write + binary
# Pickle stores data in binary format, so binary mode is required
profile_file = open("profile.pickle", "wb")

# Dictionary object
# A dictionary value can also be a list
# → You can nest a list [] inside a dictionary {} like this
profile = {
    "name": "Brad Pitt",
    "age": 60,
    "notable_works": ["Legends of the Fall", "Troy", "Fight Club"]
}

print(profile)  # Check data before saving

# pickle.dump(object, file)
# → Saves the Python object directly into the file
pickle.dump(profile, profile_file)

profile_file.close()  # Always close the file after writing

# ===============================
# 2️⃣ Load an object from a file
# ===============================

# "rb" = read + binary
# Binary mode is also required when reading pickle files
profile_file = open("profile.pickle", "rb")

# pickle.load(file)
# → Restores the object exactly as it was saved
profile = pickle.load(profile_file)

print(profile)  # Verify loaded data

profile_file.close()
