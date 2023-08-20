# @BEGIN Food_Inspection_Python_Datacleaning
# @PARAM db_pth
# @IN Food_Inspections @URI file:{db_pth}\openrefine\Food_Inspections.csv
# @IN Food_Inspections_OpenRefine_cleaned  @URI file:{db_pth}\openrefine\Food_Inspections_openrefine.csv
# @OUT Food_Inspections_Python_cleaned  @URI file:{db_pth}\Food_Inspections_Python_cleaned.pdf

    # @BEGIN LoadDirtyDataToPandasDF
    # @IN Food_Inspections
    # @OUT Food_Inspections_Dataset
    # @END LoadDirtyDataToPandasDF

    # @BEGIN LoadFirstStepCleanedDataToPandasDF
    # @IN Food_Inspections_OpenRefine_cleaned
    # @OUT Food_Inspections_OR_Dataset
    # @END LoadFirstStepCleanedDataToPandasDF

    # @BEGIN CompareChangesOnDataset
    # @IN Food_Inspections_Dataset
    # @IN Food_Inspections_OR_Dataset
    # @OUT Food_Inspections_Initial
    # @END CompareChangesOnDataset

    # @BEGIN Phrase1-DealingWithMissingData
    # @IN Food_Inspections_Initial
    # @END Phrase1-DealingWithMissingData

    # @BEGIN Phrase1a-DropNullValueRecords:License #, Risk, Address,Zip, Inspection Type, Facility Type
    # @IN Phrase1-DealingWithMissingData
    # @OUT Missing_Dropped
    # @END Phrase1a-DropNullValueRecords:License #, Risk, Address,Zip, Inspection Type, Facility Type

    # @BEGIN Phrase1b-FillNullinCity
    # @IN Phrase1-DealingWithMissingData
    # @OUT City_Filled_Updated
    # @END Phrase1b-FillNullinCity

    # @BEGIN Phrase1:JoinResults
    # @IN Missing_Dropped
    # @IN City_Filled_Updated
    # @OUT Food_Inspections_Missing_Cleaned
    # @END Phrase1:JoinResults 

    # @BEGIN Phrase2-DealingWithIncorrectFormat
    # @IN Food_Inspections_Missing_Cleaned
    # @END Phrase2-DealingWithIncorrectFormat

    # @BEGIN Phrase2a-floatToInt(License#)
    # @IN Phrase2-DealingWithIncorrectFormat
    # @OUT License#_Updated
    # @End Phrase2a-floatToInt(License#)

    # @BEGIN Phrase2b-floatToInt(Zip)
    # @IN Phrase2-DealingWithIncorrectFormat
    # @OUT Zip_Updated
    # @End Phrase2b-floatToInt(Zip)

    # @BEGIN Phrase2c-objectToDate(InspectionDate)
    # @IN Phrase2-DealingWithIncorrectFormat
    # @OUT InspectionDate_Updated
    # @End Phrase2c-objectToDate(InspectionDate)

    # @BEGIN Phrase2:JoinResults
    # @IN License#_Updated
    # @IN Zip_Updated
    # @IN InspectionDate_Updated
    # @OUT Food_Inspections_Format_Cleaned
    # @END Phrase2:JoinResults 

    # @BEGIN Phrase3-DealingWithDataInconsistency
    # @IN Food_Inspections_Format_Cleaned
    # @END Phrase3-DealingWithDataInconsistency

    # @BEGIN Phrase3a-CheckInconsistencyOnResult
    # @IN Phrase3-DealingWithDataInconsistency
    # @OUT Result_Updated
        # @BEGIN Update:'null' in Violations and 'Pass with conditions'/'Fail' in Results
        # @End Update:'null' in Violations and 'Pass with conditions'/'Fail' in Results
    # @End Phrase3a-CheckInconsistencyOnResult

    # @BEGIN Phrase3b-CheckInconsistencyOnRisk
    # @IN Phrase3-DealingWithDataInconsistency
    # @OUT Risk_Updated
        # @BEGIN removeRecord(df['Risk']=='all')
        # @End removeRecord(df['Risk']=='all')
    # @END Phrase3b-CheckInconsistencyOnRisk

    # @BEGIN Phrase3:JoinResults
    # @IN Result_Updated
    # @IN Risk_Updated
    # @OUT Food_Inspections_Inconsistency_Cleaned
    # @END Phrase3:JoinResults 

    # @BEGIN Phrase4-DiscoveringIntegrityConstraintViolation
    # @IN Food_Inspections_Inconsistency_Cleaned
    # @END Phrase4-DiscoveringIntegrityConstraintViolation

    # @BEGIN Phrase4a:Constraint:Inspection_ID_isUnique
    # @IN Phrase4-DiscoveringIntegrityConstraintViolation
    # @OUT Violation_Num_Inspection_ID_isUnique
        # @BEGIN find_duplicated_id(df)
        # @END find_duplicated_id(df)
    # @END Phrase4a:Constraint:Inspection_ID_isUnique

    # @BEGIN Phrase4b:Constraint:License_#_isUnique
    # @IN Phrase4-DiscoveringIntegrityConstraintViolation
    # @OUT Violation_Num_License_#_isUnique
        # @BEGIN find_duplicated_license(df)
        # @END find_duplicated_license(df)
    # @END Phrase4b-Iterate:Constraint:License_#_isUnique

    # @BEGIN Phrase4b-FixDuplicatedPairs
    # @In Violation_Num_License_#_isUnique
    # @OUT Address_Updated
        # @BEGIN make_dic_license_address(df)
        # @END make_dic_license_address(df)
        # @BEGIN merge_dic_to_df(df1,df2)
        # @END merge_dic_to_df(df1,df2)
    # @END Phrase4b-FixDuplicatedPairs

    # @BEGIN Phrase4c-Iterate:Constraint:Longitude_inRange
    # @IN Phrase4-DiscoveringIntegrityConstraintViolation
    # @OUT Violation_Num_Longitude_inRange
        # @BEGIN check_longitude(df)
        # @END check_longitude(df)
    # @END Phrase4c-Iterate:Constraint:Longitude_inRange

    # @BEGIN Phrase4c-Iterate:Constraint:Latitude_inRange
    # @IN Phrase4-DiscoveringIntegrityConstraintViolation
    # @OUT Violation_Num_Latitude_inRange
        # @BEGIN check_latitude(df)
        # @END check_latitude(df)
    # @END Phrase4c-Iterate:Constraint:Latitude_inRange

    # @BEGIN Phrase4d-Iterate:Constraint:DBA_Name_Determine_AKA_Name
    # @IN Phrase4-DiscoveringIntegrityConstraintViolation
    # @OUT AKA_Name_Updated
        # @BEGIN make_dic_dba_aka(df)
        # @END make_dic_dba_aka(df)
        # @BEGIN merge_dic_to_df(df1,df2)
        # @END merge_dic_to_df(df1,df2)
    # @END Phrase4d-Iterate:Constraint:DBA_Name_Determine_AKA_Name

    # @BEGIN Phrase4:JoinResults
    # @IN Address_Updated
    # @IN AKA_Name_Updated
    # @OUT Food_Inspections_Constraint_Cleaned
    # @END Phrase4:JoinResults 

    # @BEGIN ExportToCSV
    # @IN Food_Inspections_Constraint_Cleaned
    # @OUT Food_Inspections_py.csv
    # @END ExportToCSV

# @END Food_Inspection_Python_Datacleaning   
    








