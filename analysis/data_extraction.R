################################################################################
# Author: Eleonora Racca
# Mail:   e.racca@unito.it
# Aim of the script: Convert the xls files to a unique csv for each sensor.
################################################################################

# Debug and progress prints
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Conversion from xls to csv files")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

print("-----------------------------------------------------------------------")
print(" Inizialisation and loading of libraries and global variables")
print("-----------------------------------------------------------------------\n")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Required libraries -----------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Debug and progress prints
print(" Loading the libraries")

# Libraries vector, to be installed or loaded
lib <- c ("readxl", "dplyr", "readr")

# Install missing and load libraries
for (i in lib) {
  if (i %in% installed.packages () [,"Package"] == F) {
    install.packages (i)
  }
  library (i, character.only = TRUE)
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Settings and global variables ------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print di debug e avanzamento
print(" Creation of global variables")

## Paths -----------------------------------------------------------------------
path_in <- "../scraping"
path_out <- "../data"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Custom function --------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function to read the data and convert string columns to string
fun_read <- function(file) {
  df <- read_excel(file)
  
  # Check if there are at least 6 columns
  if (ncol(df) >= 6) {
    df <- df %>%
      # Convert the first 6 columns to string
      mutate(across(1:6, as.character))  
  }
  
  return(df)
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Files conversion -------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Obtaining sensors' subfolders in the main directory
path_list <- list.dirs(path_in, recursive = FALSE)

# Creating the output folder if it does not exist
if (!dir.exists(path_out)) {
  dir.create(path_out)
}

# For each subfolder, read the xls files and include them into a dataframe to be saved as csv
for (path_subfolder in path_list) {
  
  # Find each xls file
  file_list <- list.files(path_subfolder, pattern = "\\.xls[x]?$", full.names = TRUE)
  
  # If files exist, read and concatenate them
  if (length(file_list) > 0) {
    # Use custom function to read the files and convert the strings to strings
    df_list <- lapply(file_list, fun_read)
    # Concatenate the dataframes
    df_all <- bind_rows(df_list)
    
    # File name based on the subfolder's name
    name_out <- paste0(basename(path_subfolder), "_complete.csv")
    path_fileout <- file.path(path_out, name_out)
    
    # Save complete dataframe to csv
    write_csv(df_all, path_fileout)
    
    cat("Saved:", path_fileout, "\n")
  }
}