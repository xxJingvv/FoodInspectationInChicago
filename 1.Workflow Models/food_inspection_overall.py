# @BEGIN Food_Inspection_Overall
# @PARAM db_pth
# @IN Food_Inspections @URI file:{db_pth}\openrefine\Food_Inspections.csv
# @OUT Food_Inspections_cleaned  @URI file:{db_pth}\Food_Inspections_cleaned.pdf
    # @BEGIN Input:Food_inspection.csv
    # @IN Food_Inspections
    # @END Input:Food_inspection.csv

    # @BEGIN Data_Cleaning_Process_with_OpenRefine
    # @IN Input:Food_inspection.csv
    # @END Data_Cleaning_Process_with_OpenRefine

    # @BEGIN OpenRefine:Trim_Spaces
    # @IN Data_Cleaning_Process_with_OpenRefine
    # @OUT Dataset_Spaces_Trimmed
    # @END OpenRefine:Trim_Spaces

    # @BEGIN OpenRefine:Transform_Uppercase
    # @IN Data_Cleaning_Process_with_OpenRefine
    # @OUT Dataset_Transformed
    # @END OpenRefine:Transform_Uppercase

    # @BEGIN OpenRefine:Merge_Similar
    # @IN Data_Cleaning_Process_with_OpenRefine
    # @OUT Dataset_Value_Custered
    # @END OpenRefine:Merge_Similar

    # @BEGIN OpenRefine:AddColomn
    # @IN Data_Cleaning_Process_with_OpenRefine
    # @OUT Dataset_Column_added
    # @END OpenRefine:AddColomn


    # @BEGIN OpenRefine:JoinResults
    # @IN Dataset_Spaces_Trimmed
    # @IN Dataset_Transformed
    # @IN Dataset_Value_Custered
    # @IN Dataset_Column_added
    # @OUT Food_Inspections_openrefine.csv
    # @END OpenRefine:JoinResults

    # @BEGIN Data_Cleaning_Process_with_Python
    # @IN Data_Cleaning_Process_with_OpenRefine
    # @END Data_Cleaning_Process_with_Python

    # @BEGIN Python:DealingWithMissingData
    # @IN Data_Cleaning_Process_with_Python
    # @OUT Dataset_Missing_Cleaned
    # @END Python:DealingWithMissingData

    # @BEGIN Python:DealingWithIncorrectFormat
    # @IN Data_Cleaning_Process_with_Python
    # @OUT Dataset_Format_Cleaned
    # @END Python:DealingWithIncorrectFormat

    # @BEGIN Python:CheckInconsistencyOnResult
    # @IN Data_Cleaning_Process_with_Python
    # @OUT Dataset_Inconsistency_Cleaned
    # @END Python:CheckInconsistencyOnResult

    # @BEGIN Python:DiscoveringIntegrityConstraintViolation
    # @IN Data_Cleaning_Process_with_Python
    # @OUT Dataset_Constraint_Cleaned
    # @END Python:DiscoveringIntegrityConstraintViolation

    # @BEGIN Python:JoinResults
    # @IN Dataset_Missing_Cleaned
    # @IN Dataset_Format_Cleaned
    # @IN Dataset_Inconsistency_Cleaned
    # @IN Dataset_Constraint_Cleaned
    # @OUT Food_Inspections_py.csv
    # @END Python:JoinResults

    # @BEGIN Data_Cleaning_Process_with_SQL
    # @IN Data_Cleaning_Process_with_Python
    # @END Data_Cleaning_Process_with_SQL

    # @BEGIN SQL:Discover_Integrity_Constraint_Violation
    # @IN Data_Cleaning_Process_with_SQL
    # @OUT Food_Inspections_sql.csv
    # @END SQL:Discover_Integrity_Constraint_Violation

# @END Food_Inspection_Overall