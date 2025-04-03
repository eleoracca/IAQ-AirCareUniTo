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
# Loading the virtual environment ----------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Debug and progress prints
print(" Activating the virtual environment")

# Libraries vector, to be installed or loaded
lib <- c ("renv", "rprojroot")

# Install missing and load libraries
for (i in lib) {
  if (i %in% installed.packages () [,"Package"] == F) {
    install.packages (i)
  }
  suppressPackageStartupMessages(library (i, character.only = TRUE))
}

# Activating the virtual environment
path_workdir <- rprojroot::find_root(rprojroot::has_file("renv.lock"))
renv::load(path_workdir)

# Set working directory
setwd(path_workdir)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Required libraries -----------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Debug and progress prints
print(" Loading the libraries")

# Libraries vector, to be installed or loaded
lib <- c ("readxl", "tidyr", "dplyr", "readr")

# Install missing and load libraries
for (i in lib) {
  if (i %in% installed.packages () [,"Package"] == F) {
    install.packages (i)
  }
  library (i, character.only = TRUE)
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Custom functions -------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function to read the data and convert string columns to string
fun_read <- function(file) {
  df <- read_excel(file)
  
  # Check if there are at least 6 columns
  if (ncol(df) >= 6) {
    df <- df %>%
      # Convert the first 6 columns to string and the epoch time to number
      # Epoch time should be numeric, but better be safe as the ordering will use the epoch time
      mutate(
        across(1:6, as.character),
        across(7, as.numeric)
      )
  }
  
  return(df)
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Settings and global variables ------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Begin time
time_begin <- Sys.time()

# Print di debug e avanzamento
print(" Creation of global variables")

## Paths -----------------------------------------------------------------------
# Path are given based on the current working directory, which is path_workdir
path_in <- "scraping"
path_out <- "data"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Files conversion -------------------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("-----------------------------------------------------------------------")
print(" Reading and export of xls files to csv")
print("-----------------------------------------------------------------------\n")
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
    
    # Concatenate the dataframes and order by epoch time
    df_all <- bind_rows(df_list)
    df_all <- df_all %>% 
      distinct() %>%      # Remove duplicates line
      arrange(across(7))  # Order by epoch time
    
    # File name based on the subfolder's name
    name_out <- paste0(basename(path_subfolder), "_complete.csv")
    path_fileout <- file.path(path_out, name_out)
    
    # Save complete dataframe to csv
    write_csv(df_all, path_fileout)
    
    cat("Saved:", path_fileout, "\n")
  }
}



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Final prints and execution time ----------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("-----------------------------------------------------------------------")
print(" Elapsed time")
print("-----------------------------------------------------------------------\n")
# Ending time
time_end <- Sys.time()

# Elapsed time
time_last <- as.numeric(difftime(time_end, time_begin, units = "secs"))
time_hours <- floor(time_last / 3600)
time_min <- floor((time_last %% 3600) / 60)
time_sec <- round(time_last %% 60)

# Print duration
cat(" Begin time:    ", format(time_begin, "%Y-%m-%d %H:%M:%S"), "\n")
cat(" End time:      ", format(time_end, "%Y-%m-%d %H:%M:%S"), "\n")
cat(sprintf(" Elapsed time: %02d:%02d:%02d\n", time_hours, time_min, time_sec))

print("Execution has ended. Thank you for your patience!")

# Deactivating the virtual environment
renv::deactivate()