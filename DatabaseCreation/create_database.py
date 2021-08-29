import sqlite3

connection = sqlite3.connect('../miracle.db')

cursor = connection.cursor()

# Add campaign Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    campaign (
        _pk_campaign INTEGER PRIMARY KEY AUTOINCREMENT,
        campaign_name TEXT
        )""")

# Add facebook_account_type Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_account_type (
        _pk_fb_ac_type INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_ac_type_name TEXT
        )""")

# Add facebook_account Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_account (
        _pk_facebook_account INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_ac_name TEXT,
        _fk_fb_ac_type INTEGER,
        FOREIGN KEY(_fk_fb_ac_type) REFERENCES fb_gp_life_circle(_pk_fb_ac_type)
        )""")


# Add fb_gp_life_circle Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    fb_gp_life_circle (
        _pk_fb_gp_life_circle INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_group_post_details TEXT
        )""")

# Add facebook_group_post Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_group_post (
        _pk_facebook_post INTEGER PRIMARY KEY AUTOINCREMENT,
        fb_group_post_name TEXT,
        _fk_fb_gp_life_circle INTEGER,
        FOREIGN KEY(_fk_fb_gp_life_circle) REFERENCES fb_gp_life_circle(_pk_fb_gp_life_circle)
        )""")

# Add profile_life_circle Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_life_circle (
        _pk_profile_life_circle INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_life_circle TEXT
        )""")

# Add profile_country Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_country (
        _pk_profile_country INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_country TEXT
        )""")

# Add profile_gender Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_gender (
        _pk_profile_gender INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_gender TEXT
        )""")

# Add profile_name Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_name (
        _pk_profile_name INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_name TEXT
        )""")

# Add facebook_profile Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_profile(
        _pk_facebook_profile INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_link TEXT,
        profile_id TEXT,
        _fk_profile_name INTEGER,
        _fk_profile_gender INTEGER,
        _fk_profile_country INTEGER,
        _fk_profile_life_circle INTEGER,    
        FOREIGN KEY(_fk_profile_name) REFERENCES profile_name(_pk_profile_name),    
        FOREIGN KEY(_fk_profile_gender) REFERENCES profile_gender(_pk_profile_gender),
        FOREIGN KEY(_fk_profile_country) REFERENCES profile_country(_pk_profile_country),
        FOREIGN KEY(_fk_profile_life_circle) REFERENCES profile_life_circle(_pk_profile_life_circle)  
        )""")

# Add profile_message Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_message (
        _pk_message_table INTEGER,
        _pk_facebook_profile INTEGER,
        FOREIGN KEY(_pk_message_table) REFERENCES message_table(_pk_message_table),
        FOREIGN KEY(_pk_facebook_profile) REFERENCES facebook_profile(_pk_facebook_profile)
        )""")

# Add message_table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    message_table (
        _pk_message_table INTEGER PRIMARY KEY AUTOINCREMENT,
        message TEXT,
        _fk_fb_profile_id INTEGER,
        _fk_message_ca_table INTEGER,
        FOREIGN KEY(_fk_fb_profile_id) REFERENCES facebook_profile(_pk_facebook_profile)
        FOREIGN KEY(_fk_message_ca_table) REFERENCES message_category_table(_pk_message_ca_table)
        )""")

# Add message_category_table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    message_category (
        _pk_message_category INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TEXT
        )""")

# Add facebook_group
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_group (
        _pk_facebook_group INTEGER PRIMARY KEY AUTOINCREMENT,
        group_link TEXT,
        _fk_group_name_id INTEGER,
        _fk_group_category_id INTEGER,
        FOREIGN KEY(_fk_group_name_id) REFERENCES facebook_group_name(_pk_fb_group_name)
        FOREIGN KEY(_fk_group_category_id) REFERENCES facebook_group_category(_pk_fb_gp_category)
        )""")

# Add facebook_group_name Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_group_name (
        _pk_fb_group_name INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT
        )""")

# Add facebook_group_category Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_group_category (
        _pk_fb_gp_category INTEGER PRIMARY KEY AUTOINCREMENT,
        gp_category_name TEXT
        )""")

# Add facebook_group_test Test_Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    facebook_group_test (
        _pk_facebook_group INTEGER PRIMARY KEY AUTOINCREMENT,
        group_link TEXT,
        _fk_group_name_id INTEGER,
        _fk_group_category_id INTEGER,
        FOREIGN KEY(_fk_group_name_id) REFERENCES facebook_group_name(_pk_fb_group_name)
        FOREIGN KEY(_fk_group_category_id) REFERENCES facebook_group_category(_pk_fb_gp_category)
        )""")

# Add profile_group_link Table
cursor.execute("""CREATE TABLE IF NOT EXISTS
    profile_group_link (
        _pk_profile_gp_link INTEGER PRIMARY KEY AUTOINCREMENT,
        profile_group_link TEXT
        )""")

connection.commit()
connection.close()

print("Database created successfully")
