import pandas as pd

try:
    # Read and store the csv file into pokemon_df variable
    pokemon_df = pd.read_csv("pokemon_list.csv")
except FileNotFoundError:
    print("Error: The file was not found.")

# Print the first 5 rows of DataFrame
print("\nFirst 5 Rows of DataFrame:\n", pokemon_df.head(5))

# Print the last 5 rows of DataFrame
print("\nLast 5 Rows of DataFrame:\n", pokemon_df.tail(5))

# Print summary of df
print("\nSummary of DataFRame:\n")
pokemon_df.info()

# Print descriptive statistics
print("\nDescriptive Statistics:\n", pokemon_df.describe())

# Shape of df
print("\nDataFrame Shape:\n", pokemon_df.shape)

# Column names
print("\nColumn Names:\n", pokemon_df.columns)

# Select and display a single column by its name
pokemon_df_names = pokemon_df['Name']
print("\nPokemon Names List:\n", pokemon_df_names)

# Select and display multiple columns
pokemon_df_names_type = pokemon_df[['Name', 'Type']]
print("\nPokemon Name and Type:\n", pokemon_df_names_type)

# Filter and display rows based on a condition
pokemon_df_can_evolve = pokemon_df[pokemon_df['Evolves'] == True]
print("\nPokemon Who Evolve:\n", pokemon_df_can_evolve)

# Filter and display rows based on text condition
pokemon_df_fire_type = pokemon_df[pokemon_df['Type'] == 'Fire']
print("\nFire Type Pokemon:\n", pokemon_df_fire_type)

# Combine conditioning filters
pokemon_df_fire_evolve = pokemon_df[
    (pokemon_df['Type'] == 'Fire') & 
    (pokemon_df['Evolves'] == True)
]
print("\nFire Type Pokemon Who Evolve:\n", pokemon_df_fire_evolve)

# Simple Data Manipulation
# Sort by pokedex number
pokemon_df_sorted = pokemon_df.sort_values(by='Number', ascending=True)
print("\nPokemon Sorted by PokeDex Number:\n", pokemon_df_sorted)